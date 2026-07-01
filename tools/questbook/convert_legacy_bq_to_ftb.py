#!/usr/bin/env python3
"""Convert the trimmed legacy BetterQuesting JSON source to FTB Quests SNBT.

FTB Quests 2001.4.22 still stores quest data as SNBT under
config/ftbquests/quests. This converter intentionally starts from the same
legacy source and mapping rules as convert_legacy_bq.py, but emits native FTB
Quests tasks/rewards where there is a direct equivalent.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import convert_legacy_bq as legacy  # noqa: E402


FILE_ID = "0000000000000001"
FTB_VERSION = 13
COORD_SCALE = 24.0
VALID_FORMAT_CODES = set("0123456789abcdefklmnorABCDEFKLMNOR")


def ftb_id(kind: int, old_id: int, slot: int = 0) -> str:
    return f"{((kind & 0xFF) << 56) | ((old_id & 0xFFFFFF) << 16) | (slot & 0xFFFF):016X}"


STANDARD_RANDOM_REWARD_TABLE_ID = int(ftb_id(5, 1), 16)


def escape_literal_ampersands(value: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(value):
        char = value[i]
        if char != "&":
            out.append(char)
            i += 1
            continue
        if i > 0 and value[i - 1] == "\\":
            out.append(char)
        elif i + 1 < len(value) and value[i + 1] in VALID_FORMAT_CODES:
            out.append(char)
        else:
            out.append("\\&")
        i += 1
    return "".join(out)


def normalize_text(value: str) -> str:
    value = value.replace("\xa7", "&")
    # The legacy BQ book used black codes as a practical reset/default in many
    # descriptions. FTB renders &0 as true black, which is unreadable here.
    value = re.sub(r"&0", "&r", value)
    return escape_literal_ampersands(value)


def clean_name(value: str) -> str:
    value = re.sub(r"\s+", " ", normalize_text(value)).strip()
    return value or "Untitled"


def split_description(value: str) -> list[str]:
    value = normalize_text(value.replace("\r\n", "\n").replace("\r", "\n"))
    return [line.rstrip() for line in value.split("\n")]


def scale_coord(value: int) -> float:
    scaled = round(value / COORD_SCALE, 2)
    return int(scaled) if scaled.is_integer() else scaled


def props(source: dict[str, Any]) -> dict[str, Any]:
    return source.get("properties:10", {}).get("betterquesting:10", {})


def quest_title(source: dict[str, Any]) -> str:
    return clean_name(props(source).get("name:8", f"Quest {source.get('questID:3')}"))


def quest_desc(source: dict[str, Any]) -> list[str]:
    return split_description(props(source).get("desc:8", ""))


def chapter_title(source: dict[str, Any]) -> str:
    return clean_name(props(source).get("name:8", f"Chapter {source.get('lineID:3')}"))


def chapter_desc(source: dict[str, Any]) -> list[str]:
    return split_description(props(source).get("desc:8", ""))


def sanitize_filename(title: str, old_id: int) -> str:
    base = re.sub(r"[^a-z0-9_]+", "_", title.lower()).strip("_")
    return f"{old_id:02d}_{base or 'chapter'}"


def stack_damage(old: dict[str, Any]) -> int:
    return int(old.get("Damage:2", old.get("Damage:3", old.get("Damage", 0))))


def map_stack(old: dict[str, Any], audit: dict[str, Any], validate_item_id: bool = True) -> tuple[str, int] | None:
    item_id = old.get("id:8") or old.get("id") or "minecraft:air"
    damage = stack_damage(old)
    mapped = legacy.map_item_id(item_id, damage, audit, old)
    if mapped is None:
        return None
    count = int(old.get("Count:3", old.get("Count", old.get("count", 1))))
    if validate_item_id and mapped not in audit["item_ids"] and audit["item_ids"] and mapped != "minecraft:air":
        audit["missing_items"][mapped] += 1
    return mapped, max(count, 1)


def stack_values(source: dict[str, Any]) -> list[dict[str, Any]]:
    return [entry for entry in legacy.old_collection_to_list(source) if isinstance(entry, dict)]


def is_legacy_random_reward_stack(old_stack: dict[str, Any]) -> bool:
    return (old_stack.get("id:8") or old_stack.get("id")) == "bq_standard:loot_chest"


def random_reward(quest_old_id: int, slot: int, audit: dict[str, Any], reason: str) -> dict[str, Any]:
    audit["converted_random_rewards"][reason] += 1
    return {
        "id": ftb_id(4, quest_old_id, slot),
        "type": "random",
        "table_id": STANDARD_RANDOM_REWARD_TABLE_ID,
    }


def old_weight(source: dict[str, Any]) -> float:
    return float(source.get("weight:3", source.get("weight", 1)))


def fallback_random_reward_table() -> list[dict[str, Any]]:
    return [
        {"type": "item", "item": "minecraft:diamond", "count": 2, "weight": 1.0},
        {"type": "item", "item": "minecraft:emerald", "count": 4, "weight": 1.0},
        {"type": "item", "item": "minecraft:gold_ingot", "count": 8, "weight": 1.0},
        {"type": "item", "item": "minecraft:iron_ingot", "count": 16, "weight": 1.0},
        {"type": "item", "item": "minecraft:lapis_lazuli", "count": 16, "weight": 1.0},
        {"type": "item", "item": "minecraft:redstone", "count": 16, "weight": 1.0},
    ]


def load_random_reward_removals(path: Path | None) -> set[tuple[str, int]]:
    if path is None:
        return set()
    source = json.loads(path.read_text(encoding="utf-8"))
    removals: set[tuple[str, int]] = set()
    for entry in source.get("remove", []):
        if not isinstance(entry, dict):
            continue
        item_id = entry.get("item")
        if not item_id:
            continue
        removals.add((str(item_id), int(entry.get("count", 1))))
    return removals


def build_random_reward_table(path: Path | None, audit: dict[str, Any]) -> list[dict[str, Any]]:
    if path is None:
        audit["random_reward_table"]["fallback placeholder table"] += 1
        return fallback_random_reward_table()

    source = json.loads(path.read_text(encoding="utf-8"))
    rewards: list[dict[str, Any]] = []
    for group in legacy.old_collection_to_list(source.get("groups:9", {})):
        if not isinstance(group, dict):
            continue
        group_weight = old_weight(group)
        for reward in legacy.old_collection_to_list(group.get("rewards:9", {})):
            if not isinstance(reward, dict):
                continue
            reward_weight = old_weight(reward)
            stacks = stack_values(reward.get("items:9", {}))
            if not stacks:
                audit["dropped_random_reward_table_entries"]["empty stack list"] += 1
                continue
            for stack in stacks:
                mapped = map_stack(stack, audit, validate_item_id=False)
                if mapped is None:
                    item_id = stack.get("id:8") or stack.get("id") or "minecraft:air"
                    audit["dropped_random_reward_table_entries"][f"unmapped {item_id}"] += 1
                    continue
                item_id, count = mapped
                if audit["item_ids"] and item_id not in audit["item_ids"] and item_id != "minecraft:air":
                    audit["dropped_random_reward_table_entries"][f"missing {item_id}"] += 1
                    continue
                if (item_id, count) in audit["random_reward_removals"]:
                    audit["removed_random_reward_table_entries"][f"{item_id} x{count}"] += 1
                    continue
                entry: dict[str, Any] = {
                    "type": "item",
                    "item": item_id,
                    "weight": group_weight * reward_weight,
                }
                if count != 1:
                    entry["count"] = count
                rewards.append(entry)

    audit["random_reward_table"]["converted entries"] = len(rewards)
    if not rewards:
        audit["random_reward_table"]["fallback placeholder table"] += 1
        return fallback_random_reward_table()
    return rewards


def snbt_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def snbt_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    return snbt_string(str(value))


def snbt(value: Any, indent: int = 0) -> str:
    pad = " " * indent
    next_pad = " " * (indent + 2)
    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        entries = list(value.items())
        for idx, (key, item) in enumerate(entries):
            comma = "," if idx < len(entries) - 1 else ""
            lines.append(f"{next_pad}{key}: {snbt(item, indent + 2)}{comma}")
        lines.append(f"{pad}}}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return "[]"
        if all(not isinstance(v, (dict, list)) for v in value):
            return "[" + ", ".join(snbt(v, indent) for v in value) + "]"
        lines = ["["]
        for idx, item in enumerate(value):
            comma = "," if idx < len(value) - 1 else ""
            lines.append(f"{next_pad}{snbt(item, indent + 2)}{comma}")
        lines.append(f"{pad}]")
        return "\n".join(lines)
    return snbt_scalar(value)


def write_snbt(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(snbt(data) + "\n", encoding="utf-8")


def item_task(task: dict[str, Any], quest_old_id: int, slot: int, audit: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for stack_idx, old_stack in enumerate(stack_values(task.get("requiredItems:9", {}))):
        mapped = map_stack(old_stack, audit)
        if mapped is None:
            continue
        item_id, count = mapped
        task_nbt = {
            "id": ftb_id(3, quest_old_id, slot * 100 + stack_idx),
            "type": "item",
            "item": item_id,
        }
        if count > 1:
            task_nbt["count"] = count
        if task.get("consume:1", 0):
            task_nbt["consume_items"] = "true"
        out.append(task_nbt)
    return out


def checkmark_task(task: dict[str, Any], quest_old_id: int, slot: int, audit: dict[str, Any], reason: str) -> dict[str, Any]:
    audit["manual_tasks"][reason] += 1
    title = task.get("name:8") or reason
    return {
        "id": ftb_id(3, quest_old_id, slot),
        "type": "checkmark",
        "title": clean_name(title),
    }


def convert_tasks(source: dict[str, Any], quest_old_id: int, audit: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for slot, task in enumerate(legacy.old_collection_to_list(source.get("tasks:9", {}))):
        task_type = task.get("taskID:8", "unknown")
        audit["tasks"][task_type] += 1
        if task_type == "bq_standard:retrieval":
            out.extend(item_task(task, quest_old_id, slot, audit))
        elif task_type == "bq_standard:checkbox":
            out.append(checkmark_task(task, quest_old_id, slot, audit, "checkbox"))
        else:
            out.append(checkmark_task(task, quest_old_id, slot, audit, task_type))
    if not out:
        out.append({"id": ftb_id(3, quest_old_id, 0), "type": "checkmark", "title": "Complete"})
        audit["manual_tasks"]["empty task fallback"] += 1
    return out


def item_rewards(reward: dict[str, Any], quest_old_id: int, slot: int, audit: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for stack_idx, old_stack in enumerate(stack_values(reward.get("rewards:9", {}))):
        if is_legacy_random_reward_stack(old_stack):
            out.append(random_reward(quest_old_id, slot * 100 + stack_idx, audit, "loot_chest item reward"))
            continue
        mapped = map_stack(old_stack, audit)
        if mapped is None:
            continue
        item_id, count = mapped
        reward_nbt = {
            "id": ftb_id(4, quest_old_id, slot * 100 + stack_idx),
            "type": "item",
            "item": item_id,
        }
        if count > 1:
            reward_nbt["count"] = count
        out.append(reward_nbt)
    return out


def choice_rewards(reward: dict[str, Any], quest_old_id: int, slot: int, audit: dict[str, Any]) -> list[dict[str, Any]]:
    # FTB has a ChoiceReward type, but its data model points at other reward
    # IDs. Emitting each option as an item reward is playable and auditable.
    out = []
    for choice_idx, old_stack in enumerate(stack_values(reward.get("choices:9", {}))):
        if is_legacy_random_reward_stack(old_stack):
            out.append(random_reward(quest_old_id, slot * 100 + choice_idx, audit, "loot_chest choice reward"))
            continue
        mapped = map_stack(old_stack, audit)
        if mapped is None:
            continue
        item_id, count = mapped
        out.append({
            "id": ftb_id(4, quest_old_id, slot * 100 + choice_idx),
            "type": "item",
            "item": item_id,
            **({"count": count} if count > 1 else {}),
            "title": f"Choice option: {item_id}",
        })
    audit["flattened_choice_rewards"] += 1
    return out


def convert_rewards(source: dict[str, Any], quest_old_id: int, audit: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for slot, reward in enumerate(legacy.old_collection_to_list(source.get("rewards:9", {}))):
        reward_type = reward.get("rewardID:8", "unknown")
        if audit["rules"]["replace_missing_reward_stacks"]:
            missing_stack = legacy.reward_has_missing_stack(reward, audit)
            if missing_stack is not None:
                audit["rewards"][reward_type] += 1
                audit["replaced_rewards"][f"{quest_old_id}: {reward_type} missing {missing_stack}"] += 1
                out.append({
                    "id": ftb_id(4, quest_old_id, slot),
                    "type": "random",
                    "table_id": STANDARD_RANDOM_REWARD_TABLE_ID,
                })
                continue
        audit["rewards"][reward_type] += 1
        if reward_type == "bq_standard:item":
            out.extend(item_rewards(reward, quest_old_id, slot, audit))
        elif reward_type == "bq_standard:choice":
            out.extend(choice_rewards(reward, quest_old_id, slot, audit))
        elif reward_type == "bq_standard:xp":
            xp = int(reward.get("xp:3", reward.get("amount:3", 100)))
            out.append({"id": ftb_id(4, quest_old_id, slot), "type": "xp", "xp": xp})
        elif reward_type == "bq_standard:command":
            command = reward.get("command:8", "")
            if command:
                out.append({"id": ftb_id(4, quest_old_id, slot), "type": "command", "command": command})
            else:
                audit["dropped_rewards"][f"{quest_old_id}: empty command"] += 1
        else:
            audit["dropped_rewards"][f"{quest_old_id}: {reward_type}"] += 1
    return out


def build_audit(item_ids: set[str], rules: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_ids": item_ids,
        "rules": rules,
        "missing_items": Counter(),
        "mapped_items": Counter(),
        "tasks": Counter(),
        "rewards": Counter(),
        "manual_tasks": Counter(),
        "dropped_props": Counter(),
        "dropped_stacks": Counter(),
        "dropped_chapters": Counter(),
        "dropped_quests": Counter(),
        "dropped_prerequisites": Counter(),
        "replaced_prerequisites": Counter(),
        "replaced_rewards": Counter(),
        "converted_random_rewards": Counter(),
        "random_reward_table": Counter(),
        "dropped_random_reward_table_entries": Counter(),
        "removed_random_reward_table_entries": Counter(),
        "random_reward_removals": set(),
        "dropped_rewards": Counter(),
        "flattened_choice_rewards": 0,
    }


def kept_content(source: dict[str, Any], audit: dict[str, Any]) -> tuple[list[dict[str, Any]], set[int]]:
    kept_chapters = []
    allowed_quest_ids: set[int] = set()
    for chapter in source["questLines:9"].values():
        if legacy.should_drop_chapter(chapter, audit["rules"]):
            name = legacy.chapter_name(chapter)
            audit["dropped_chapters"][f"{chapter['lineID:3']}:{name}"] += len(chapter.get("quests:9", {}))
            continue
        kept_chapters.append(chapter)
        allowed_quest_ids.update(legacy.chapter_quest_ids(chapter))
    for quest in source["questDatabase:9"].values():
        quest_id = int(quest["questID:3"])
        if quest_id in allowed_quest_ids and legacy.should_drop_quest(quest, audit["rules"]):
            audit["dropped_quests"][f"{quest_id}:{legacy.quest_name(quest)}"] += 1
            allowed_quest_ids.remove(quest_id)
    return kept_chapters, allowed_quest_ids


def write_report(path: Path, audit: dict[str, Any], quest_count: int, chapter_count: int) -> None:
    lines = [
        "# FTB Quests Port Audit",
        "",
        f"- Converted quests: {quest_count}",
        f"- Converted chapters: {chapter_count}",
        f"- Missing item IDs referenced by stacks: {len(audit['missing_items'])}",
        f"- Flattened old BQ choice rewards: {audit['flattened_choice_rewards']}",
        "",
        "## Task Types",
        "",
    ]
    lines += [f"- `{k}`: {v}" for k, v in audit["tasks"].most_common()] or ["- None"]
    lines += ["", "## Reward Types", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["rewards"].most_common()] or ["- None"]
    lines += ["", "## Manual/Degraded Tasks", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["manual_tasks"].most_common()] or ["- None"]
    lines += ["", "## Dropped Rewards", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["dropped_rewards"].most_common()] or ["- None"]
    lines += ["", "## Replaced Rewards", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["replaced_rewards"].most_common()] or ["- None"]
    lines += ["", "## Converted Random Rewards", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["converted_random_rewards"].most_common()] or ["- None"]
    lines += ["", "## Random Reward Table", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["random_reward_table"].most_common()] or ["- None"]
    lines += ["", "## Removed Random Reward Table Entries", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["removed_random_reward_table_entries"].most_common()] or ["- None"]
    lines += ["", "## Dropped Random Reward Table Entries", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["dropped_random_reward_table_entries"].most_common()] or ["- None"]
    lines += ["", "## Dropped Chapters", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["dropped_chapters"].most_common()] or ["- None"]
    lines += ["", "## Dropped Quests", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["dropped_quests"].most_common()] or ["- None"]
    lines += ["", "## Dropped Prerequisites", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["dropped_prerequisites"].most_common()] or ["- None"]
    lines += ["", "## Applied Item Mappings", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["mapped_items"].most_common()] or ["- None"]
    lines += ["", "## Missing Item IDs", ""]
    lines += [f"- `{k}`: {v}" for k, v in audit["missing_items"].most_common()] or ["- None"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--item-ids", type=Path)
    parser.add_argument("--loot-source", type=Path)
    parser.add_argument("--random-reward-removals", type=Path)
    parser.add_argument("--rules", type=Path)
    args = parser.parse_args()

    source = json.loads(args.source.read_text(encoding="utf-8"))
    audit = build_audit(legacy.load_item_ids(args.item_ids), legacy.load_rules(args.rules))
    audit["random_reward_removals"] = load_random_reward_removals(args.random_reward_removals)
    kept_chapters, allowed_quest_ids = kept_content(source, audit)
    quest_by_id = {int(q["questID:3"]): q for q in source["questDatabase:9"].values()}
    quest_pos: dict[int, tuple[int, int]] = {}
    for chapter in kept_chapters:
        for entry in legacy.old_collection_to_list(chapter.get("quests:9", {})):
            quest_id = int(entry["id:3"])
            if quest_id in allowed_quest_ids:
                quest_pos[quest_id] = (int(entry.get("x:3", 0)), int(entry.get("y:3", 0)))

    if args.out.exists():
        shutil.rmtree(args.out)
    (args.out / "chapters").mkdir(parents=True, exist_ok=True)
    (args.out / "reward_tables").mkdir(parents=True, exist_ok=True)

    write_snbt(args.out / "data.snbt", {
        "version": FTB_VERSION,
        "default_reward_team": False,
        "default_consume_items": False,
        "default_autoclaim_rewards": "disabled",
        "default_quest_shape": "circle",
        "default_quest_disable_jei": False,
        "emergency_items": [],
        "emergency_items_cooldown": 300,
        "drop_loot_crates": False,
        "loot_crate_no_drop": {"passive": 4000, "monster": 600, "boss": 0},
        "disable_gui": False,
        "grid_scale": 0.5,
        "pause_game": False,
        "lock_message": "",
        "progression_mode": "linear",
        "detection_delay": 20,
        "drop_book_on_death": False,
        "show_lock_icons": True,
        "hide_excluded_quests": False,
    })
    write_snbt(args.out / "chapter_groups.snbt", {"chapter_groups": []})
    write_snbt(args.out / "reward_tables" / "standard_random_reward.snbt", {
        "id": f"{STANDARD_RANDOM_REWARD_TABLE_ID:016X}",
        "order_index": 0,
        "title": "Standard Random Reward",
        "loot_size": 1,
        "rewards": build_random_reward_table(args.loot_source, audit),
    })

    quest_count = 0
    for order, chapter in enumerate(kept_chapters):
        old_chapter_id = int(chapter["lineID:3"])
        filename = sanitize_filename(chapter_title(chapter), old_chapter_id)
        chapter_quests = []
        for entry in legacy.old_collection_to_list(chapter.get("quests:9", {})):
            quest_old_id = int(entry["id:3"])
            if quest_old_id not in allowed_quest_ids:
                continue
            quest = quest_by_id[quest_old_id]
            prerequisites = [int(v) for v in quest.get("preRequisites:11", [])]
            replacement = audit["rules"]["prerequisite_replacements"].get(quest_old_id)
            if replacement is not None:
                audit["replaced_prerequisites"][f"{quest_old_id}: {prerequisites} -> {replacement}"] += 1
                prerequisites = replacement
            deps = []
            for prerequisite in prerequisites:
                if prerequisite in allowed_quest_ids:
                    deps.append(ftb_id(2, prerequisite))
                else:
                    audit["dropped_prerequisites"][f"{quest_old_id} <- {prerequisite}"] += 1
            x, y = quest_pos.get(quest_old_id, (0, 0))
            quest_nbt: dict[str, Any] = {
                "id": ftb_id(2, quest_old_id),
                "title": quest_title(quest),
                "x": scale_coord(x),
                "y": scale_coord(y),
                "tasks": convert_tasks(quest, quest_old_id, audit),
            }
            desc = quest_desc(quest)
            if any(line.strip() for line in desc):
                quest_nbt["description"] = desc
            icon = map_stack(props(quest).get("icon:10", {}), audit) if isinstance(props(quest).get("icon:10"), dict) else None
            if icon:
                quest_nbt["icon"] = icon[0]
            if deps:
                quest_nbt["dependencies"] = deps
            rewards = convert_rewards(quest, quest_old_id, audit)
            if rewards:
                quest_nbt["rewards"] = rewards
            chapter_quests.append(quest_nbt)
            quest_count += 1
        chapter_nbt: dict[str, Any] = {
            "id": ftb_id(1, old_chapter_id),
            "group": "",
            "order_index": order,
            "filename": filename,
            "title": chapter_title(chapter),
            "default_quest_shape": "",
            "default_hide_dependency_lines": False,
            "quests": chapter_quests,
            "quest_links": [],
        }
        desc = chapter_desc(chapter)
        if any(line.strip() for line in desc):
            chapter_nbt["subtitle"] = desc
        icon = map_stack(props(chapter).get("icon:10", {}), audit) if isinstance(props(chapter).get("icon:10"), dict) else None
        if icon:
            chapter_nbt["icon"] = icon[0]
        write_snbt(args.out / "chapters" / f"{filename}.snbt", chapter_nbt)

    write_report(args.out / "ftb_questbook_port_audit.md", audit, quest_count, len(kept_chapters))
    print(f"Converted {quest_count} quests and {len(kept_chapters)} chapters into {args.out}")
    print(f"Missing item IDs: {len(audit['missing_items'])}")
    print(f"Manual/degraded task categories: {len(audit['manual_tasks'])}")


if __name__ == "__main__":
    main()
