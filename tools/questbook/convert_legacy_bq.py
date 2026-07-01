#!/usr/bin/env python3
"""Convert a BetterQuesting 1.12 typed JSON export into BQ 1.20 XBT files.

This is intentionally conservative. It preserves unknown item IDs as
BetterQuesting item stacks so the loader can turn them into placeholders, and
it emits an audit report for manual mapping work.
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import shutil
import struct
from collections import Counter
from pathlib import Path
from typing import Any


TAG_END = 0
TAG_BYTE = 1
TAG_SHORT = 2
TAG_INT = 3
TAG_LONG = 4
TAG_FLOAT = 5
TAG_DOUBLE = 6
TAG_BYTE_ARRAY = 7
TAG_SHORT_ARRAY = 8
TAG_INT_ARRAY = 9
TAG_LONG_ARRAY = 10
TAG_FLOAT_ARRAY = 11
TAG_DOUBLE_ARRAY = 12
TAG_STRING = 13
TAG_LIST = 14
TAG_MAP = 15

XBT_FLAGS_SIMPLE = 66  # varints + null-terminated UTF, gzip handled outside.
BQ_REF_OFFSET = 8
BQ_FULL_ID_SUFFIX = 1

TYPE_BY_OLD_SUFFIX = {
    "1": TAG_BYTE,
    "2": TAG_SHORT,
    "3": TAG_INT,
    "4": TAG_LONG,
    "5": TAG_FLOAT,
    "6": TAG_DOUBLE,
    "7": TAG_BYTE_ARRAY,
    "8": TAG_STRING,
    "9": TAG_MAP,
    "10": TAG_MAP,
    "11": TAG_INT_ARRAY,
}

PROP_KEY_MAP = {
    "issilent": "is_silent",
    "snd_complete": "snd_complete",
    "lockedprogress": "locked_progress",
    "tasklogic": "task_logic",
    "repeattime": "repeat_time",
    "visibility": "visibility",
    "simultaneous": "simultaneous",
    "icon": "icon",
    "globalshare": "global_share",
    "questlogic": "quest_logic",
    "snd_update": "snd_update",
    "autoclaim": "auto_claim",
    "ismain": "is_main",
    "repeat_relative": "repeat_relative",
    "name": "name",
    "desc": "desc",
    "bg_image": "bg_image",
    "bg_size": "bg_size",
    "party_enable": "party_enable",
    "hardcore": "hardcore",
    "lives": "lives",
    "lives_def": "lives_def",
    "lives_max": "lives_max",
    "pack_name": "pack_name",
    "pack_version": "pack_version",
}

DROP_PROP_KEYS = {
    "partysinglereward",
    "global",
}

STACK_ID_RENAMES = {
    "appliedenergistics2:certus_quartz_crystal": "ae2:certus_quartz_crystal",
    "appliedenergistics2:charged_certus_quartz_crystal": "ae2:charged_certus_quartz_crystal",
    "appliedenergistics2:fluix_crystal": "ae2:fluix_crystal",
    "appliedenergistics2:sky_stone_block": "ae2:sky_stone_block",
    "forestry:apatite": "thermal:apatite",
}


class XBTWriter:
    def __init__(self) -> None:
        self.buf = bytearray()

    def write_byte(self, value: int) -> None:
        self.buf.append(value & 0xFF)

    def write_varint(self, value: int, signed: bool = True) -> None:
        if signed:
            value = (value << 1) ^ (value >> 31)
        while True:
            out = value & 0x7F
            value >>= 7
            if value:
                self.write_byte(out | 0x80)
            else:
                self.write_byte(out)
                return

    def write_varlong(self, value: int, signed: bool = True) -> None:
        if signed:
            value = (value << 1) ^ (value >> 63)
        while True:
            out = value & 0x7F
            value >>= 7
            if value:
                self.write_byte(out | 0x80)
            else:
                self.write_byte(out)
                return

    def write_utf(self, value: str) -> None:
        self.buf.extend(value.replace("\x00", "").encode("utf-8"))
        self.write_byte(0)

    def write_root(self, tag: tuple[int, Any]) -> bytes:
        self.write_byte(0)
        self.write_varlong(XBT_FLAGS_SIMPLE, signed=False)
        self.write_byte(tag[0])
        self.write_payload(tag)
        return bytes(self.buf)

    def write_payload(self, tag: tuple[int, Any]) -> None:
        tag_type, value = tag
        if tag_type == TAG_BYTE:
            self.write_byte(int(value))
        elif tag_type == TAG_SHORT:
            self.buf.extend(struct.pack(">h", int(value)))
        elif tag_type == TAG_INT:
            self.write_varint(int(value), signed=True)
        elif tag_type == TAG_LONG:
            self.write_varlong(int(value), signed=True)
        elif tag_type == TAG_FLOAT:
            self.buf.extend(struct.pack(">f", float(value)))
        elif tag_type == TAG_DOUBLE:
            self.buf.extend(struct.pack(">d", float(value)))
        elif tag_type == TAG_STRING:
            self.write_utf(str(value))
        elif tag_type == TAG_INT_ARRAY:
            self.write_varint(len(value), signed=True)
            for entry in value:
                self.write_varint(int(entry), signed=True)
        elif tag_type == TAG_LIST:
            list_type, entries = value
            self.write_byte(list_type)
            self.write_varint(len(entries), signed=True)
            for entry in entries:
                self.write_payload(entry)
        elif tag_type == TAG_MAP:
            for key, entry in value.items():
                self.write_byte(entry[0])
                self.write_utf(key)
                self.write_payload(entry)
            self.write_byte(TAG_END)
        else:
            raise ValueError(f"Unsupported XBT tag type {tag_type}")


def split_typed_key(key: str) -> tuple[str, str | None]:
    if ":" not in key:
        return key, None
    base, suffix = key.rsplit(":", 1)
    if suffix.isdigit():
        return base, suffix
    return key, None


def natural_key(key: str) -> tuple[int, str]:
    base, _ = split_typed_key(key)
    return (int(base), base) if base.isdigit() else (10**9, base)


def typed_value(value: Any, suffix: str | None = None) -> tuple[int, Any]:
    if suffix in {"9", "10"}:
        return (TAG_MAP, typed_compound(value))
    if suffix == "11":
        return (TAG_INT_ARRAY, [int(v) for v in value])
    if suffix in TYPE_BY_OLD_SUFFIX:
        return (TYPE_BY_OLD_SUFFIX[suffix], value)
    if isinstance(value, dict):
        return (TAG_MAP, typed_compound(value))
    if isinstance(value, list):
        return (TAG_INT_ARRAY, [int(v) for v in value])
    if isinstance(value, str):
        return (TAG_STRING, value)
    if isinstance(value, bool):
        return (TAG_BYTE, 1 if value else 0)
    if isinstance(value, int):
        return (TAG_INT, value)
    if isinstance(value, float):
        return (TAG_DOUBLE, value)
    raise TypeError(f"Unsupported value {value!r}")


def typed_compound(source: dict[str, Any]) -> dict[str, tuple[int, Any]]:
    out: dict[str, tuple[int, Any]] = {}
    for raw_key, value in source.items():
        key, suffix = split_typed_key(raw_key)
        out[key] = typed_value(value, suffix)
    return out


def old_collection_to_list(source: dict[str, Any]) -> list[dict[str, Any]]:
    return [source[key] for key in sorted(source, key=natural_key)]


def old_collection_to_xbt_list(source: dict[str, Any], mapper) -> tuple[int, Any]:
    entries = [mapper(entry, idx) for idx, entry in enumerate(old_collection_to_list(source))]
    return (TAG_LIST, (TAG_MAP if entries else TAG_END, entries))


def stack_key(item_id: str, damage: int) -> str:
    return f"{item_id}|{damage}"


def old_tag_value(old: dict[str, Any], tag_key: str) -> Any:
    tag = old.get("tag:10", old.get("tag", {}))
    if not isinstance(tag, dict):
        return None
    return tag.get(f"{tag_key}:8", tag.get(tag_key))


def map_item_id(item_id: str, damage: int, audit: dict[str, Any], old: dict[str, Any] | None = None) -> str | None:
    rules = audit["rules"]
    exact_key = stack_key(item_id, damage)
    if exact_key in rules["drop_stacks"] or item_id in rules["drop_items"]:
        audit["dropped_stacks"][exact_key] += 1
        return None
    mapped = rules["stack_mappings"].get(exact_key)
    if mapped is None and old is not None:
        for tag_key in rules["tag_mapping_keys"]:
            tag_value = old_tag_value(old, tag_key)
            if tag_value is None:
                continue
            tag_mapping_key = f"{item_id}|{tag_key}|{tag_value}"
            mapped = rules["tag_mappings"].get(tag_mapping_key)
            if mapped is not None:
                break
    if mapped is None:
        mapped = rules["item_mappings"].get(item_id)
    if mapped is None:
        mapped = STACK_ID_RENAMES.get(item_id)
    if mapped is None and ":" in item_id:
        namespace, path = item_id.split(":", 1)
        target_namespace = rules["namespace_mappings"].get(namespace)
        if target_namespace:
            candidate = f"{target_namespace}:{path}"
            if candidate in audit["item_ids"]:
                mapped = candidate
    if mapped:
        audit["mapped_items"][f"{exact_key} -> {mapped}"] += 1
        return mapped
    return item_id


def preview_item_id(item_id: str, damage: int, rules: dict[str, Any], item_ids: set[str]) -> str | None:
    exact_key = stack_key(item_id, damage)
    if exact_key in rules["drop_stacks"] or item_id in rules["drop_items"]:
        return None
    mapped = rules["stack_mappings"].get(exact_key)
    if mapped is None:
        mapped = rules["item_mappings"].get(item_id)
    if mapped is None:
        mapped = STACK_ID_RENAMES.get(item_id)
    if mapped is None and ":" in item_id:
        namespace, path = item_id.split(":", 1)
        target_namespace = rules["namespace_mappings"].get(namespace)
        if target_namespace:
            candidate = f"{target_namespace}:{path}"
            if candidate in item_ids:
                mapped = candidate
    return mapped or item_id


def preview_stack_item_id(old: dict[str, Any], rules: dict[str, Any], item_ids: set[str]) -> str | None:
    item_id = old.get("id:8") or old.get("id") or "minecraft:air"
    damage = int(old.get("Damage:2", old.get("Damage", 0)))
    exact_key = stack_key(item_id, damage)
    if exact_key in rules["drop_stacks"] or item_id in rules["drop_items"]:
        return None
    mapped = rules["stack_mappings"].get(exact_key)
    if mapped is None:
        for tag_key in rules["tag_mapping_keys"]:
            tag_value = old_tag_value(old, tag_key)
            if tag_value is None:
                continue
            mapped = rules["tag_mappings"].get(f"{item_id}|{tag_key}|{tag_value}")
            if mapped is not None:
                break
    if mapped is None:
        mapped = rules["item_mappings"].get(item_id)
    if mapped is None:
        mapped = STACK_ID_RENAMES.get(item_id)
    if mapped is None and ":" in item_id:
        namespace, path = item_id.split(":", 1)
        target_namespace = rules["namespace_mappings"].get(namespace)
        if target_namespace:
            candidate = f"{target_namespace}:{path}"
            if candidate in item_ids:
                mapped = candidate
    return mapped or item_id


def old_stack_values(source: dict[str, Any]) -> list[dict[str, Any]]:
    return [entry for entry in old_collection_to_list(source) if isinstance(entry, dict)]


def item_stack(old: dict[str, Any], audit: dict[str, Any]) -> tuple[int, Any] | None:
    item_id = old.get("id:8") or old.get("id") or "minecraft:air"
    damage = int(old.get("Damage:2", old.get("Damage", 0)))
    item_id = map_item_id(item_id, damage, audit, old)
    if item_id is None:
        return None
    count = int(old.get("Count:3", old.get("Count", old.get("count", 1))))
    if item_id not in audit["item_ids"] and item_id != "minecraft:air":
        audit["missing_items"][item_id] += 1
    return (
        TAG_MAP,
        {
            "reg": (TAG_STRING, "minecraft:item"),
            "id": (TAG_STRING, item_id),
            "count": (TAG_INT, count),
        },
    )


def stack_list(source: dict[str, Any], audit: dict[str, Any]) -> tuple[int, Any]:
    entries = []
    for entry in old_stack_values(source):
        stack = item_stack(entry, audit)
        if stack is not None:
            entries.append(stack)
    return (TAG_LIST, (TAG_MAP if entries else TAG_END, entries))


def old_stack_is_missing(old: dict[str, Any], audit: dict[str, Any]) -> bool:
    item_id = old.get("id:8") or old.get("id") or "minecraft:air"
    mapped = preview_stack_item_id(old, audit["rules"], audit["item_ids"])
    return mapped is not None and mapped != "minecraft:air" and mapped not in audit["item_ids"]


def reward_has_missing_stack(source: dict[str, Any], audit: dict[str, Any]) -> str | None:
    for key in ("rewards:9", "choices:9", "rewards", "choices"):
        value = source.get(key)
        if not isinstance(value, dict):
            continue
        for entry in old_stack_values(value):
            if old_stack_is_missing(entry, audit):
                item_id = entry.get("id:8") or entry.get("id") or "minecraft:air"
                damage = int(entry.get("Damage:2", entry.get("Damage", 0)))
                return stack_key(item_id, damage)
    return None


def standard_random_reward(fallback_id: int, reason: str, audit: dict[str, Any]) -> tuple[int, Any]:
    reward_type = "bq_standard:loot_key"
    audit["rewards"][reward_type] += 1
    audit["replaced_rewards"][reason] += 1
    return (
        TAG_MAP,
        {
            "type": (TAG_STRING, reward_type),
            "id": (TAG_INT, bq_full_id(fallback_id)),
            "data": (
                TAG_MAP,
                {
                    "key": (
                        TAG_MAP,
                        {
                            "t": (TAG_STRING, "RANDOM"),
                            "c": (TAG_INT, 1),
                        },
                    )
                },
            ),
        },
    )


def convert_properties(source: dict[str, Any], audit: dict[str, Any]) -> tuple[int, Any]:
    out: dict[str, tuple[int, Any]] = {}
    for namespace_raw, values_raw in source.items():
        namespace, _ = split_typed_key(namespace_raw)
        values = {}
        for key_raw, value in values_raw.items():
            key, suffix = split_typed_key(key_raw)
            if key in DROP_PROP_KEYS:
                audit["dropped_props"][key] += 1
                continue
            key = PROP_KEY_MAP.get(key, key)
            if key == "icon" and isinstance(value, dict):
                values[key] = item_stack(value, audit) or item_stack({"id:8": "minecraft:book", "Count:3": 1, "Damage:2": 0}, audit)
            else:
                values[key] = typed_value(value, suffix)
        out[namespace] = (TAG_MAP, values)
    return (TAG_MAP, out)


def convert_task(source: dict[str, Any], fallback_id: int, audit: dict[str, Any]) -> tuple[int, Any]:
    task_type = source.get("taskID:8", "betterquesting:placeholder")
    audit["tasks"][task_type] += 1
    data: dict[str, tuple[int, Any]] = {}
    for raw_key, value in source.items():
        key, suffix = split_typed_key(raw_key)
        if key in {"taskID", "index", "groupDetect"}:
            continue
        if key == "requiredItems" and isinstance(value, dict):
            data[key] = stack_list(value, audit)
        else:
            data[key] = typed_value(value, suffix)
    return (
        TAG_MAP,
        {
            "type": (TAG_STRING, task_type),
            "id": (TAG_INT, bq_full_id(int(source.get("index:3", fallback_id)))),
            "data": (TAG_MAP, data),
        },
    )


def convert_reward(source: dict[str, Any], fallback_id: int, audit: dict[str, Any]) -> tuple[int, Any]:
    if audit["rules"]["replace_missing_reward_stacks"]:
        missing_stack = reward_has_missing_stack(source, audit)
        if missing_stack is not None:
            return standard_random_reward(fallback_id, f"{source.get('rewardID:8', 'unknown')} missing {missing_stack}", audit)
    reward_type = source.get("rewardID:8", "betterquesting:placeholder")
    audit["rewards"][reward_type] += 1
    data: dict[str, tuple[int, Any]] = {}
    for raw_key, value in source.items():
        key, suffix = split_typed_key(raw_key)
        if key in {"rewardID", "index"}:
            continue
        if key in {"rewards", "choices"} and isinstance(value, dict):
            data[key] = stack_list(value, audit)
        else:
            data[key] = typed_value(value, suffix)
    return (
        TAG_MAP,
        {
            "type": (TAG_STRING, reward_type),
            "id": (TAG_INT, bq_full_id(int(source.get("index:3", fallback_id)))),
            "data": (TAG_MAP, data),
        },
    )


def bq_full_id(reference_id: int) -> int:
    return (reference_id << BQ_REF_OFFSET) | BQ_FULL_ID_SUFFIX


def convert_quest(
    source: dict[str, Any],
    audit: dict[str, Any],
    quest_id_map: dict[int, int],
    allowed_quest_ids: set[int] | None = None,
) -> tuple[int, int, Any]:
    old_quest_id = int(source["questID:3"])
    quest_id = quest_id_map[old_quest_id]
    prerequisites = [int(v) for v in source.get("preRequisites:11", [])]
    replacement_prerequisites = audit["rules"]["prerequisite_replacements"].get(old_quest_id)
    if replacement_prerequisites is not None:
        audit["replaced_prerequisites"][f"{old_quest_id}: {prerequisites} -> {replacement_prerequisites}"] += 1
        prerequisites = replacement_prerequisites
    if allowed_quest_ids is not None:
        kept = []
        for prerequisite in prerequisites:
            if prerequisite in allowed_quest_ids:
                kept.append(prerequisite)
            else:
                audit["dropped_prerequisites"][f"{old_quest_id} <- {prerequisite}"] += 1
        prerequisites = kept
    prerequisites = [quest_id_map[prerequisite] for prerequisite in prerequisites]
    out = {
        "questID": (TAG_INT, quest_id),
        "preRequisites": (TAG_INT_ARRAY, prerequisites),
        "properties": convert_properties(source.get("properties:10", {}), audit),
        "tasks": old_collection_to_xbt_list(source.get("tasks:9", {}), lambda e, i: convert_task(e, i, audit)),
        "rewards": old_collection_to_xbt_list(source.get("rewards:9", {}), lambda e, i: convert_reward(e, i, audit)),
    }
    return old_quest_id, TAG_MAP, out


def convert_chapter(
    source: dict[str, Any],
    audit: dict[str, Any],
    quest_id_map: dict[int, int],
    chapter_id_map: dict[int, int],
    allowed_quest_ids: set[int] | None = None,
) -> tuple[int, int, Any]:
    old_chapter_id = int(source["lineID:3"])
    chapter_id = chapter_id_map[old_chapter_id]
    quest_entries = []
    for idx, entry in enumerate(old_collection_to_list(source.get("quests:9", {}))):
        old_quest_id = int(entry["id:3"])
        if allowed_quest_ids is not None and old_quest_id not in allowed_quest_ids:
            continue
        quest_entries.append(
            (
                TAG_MAP,
                {
                    "id": (TAG_INT, bq_full_id(len(quest_entries))),
                    "questID": (TAG_INT, quest_id_map[old_quest_id]),
                    "x": (TAG_INT, int(entry.get("x:3", 0))),
                    "y": (TAG_INT, int(entry.get("y:3", 0))),
                    "w": (TAG_INT, int(entry.get("sizeX:3", entry.get("w:3", 24)))),
                    "h": (TAG_INT, int(entry.get("sizeY:3", entry.get("h:3", 24)))),
                },
            )
        )
    out = {
        "chapterID": (TAG_INT, chapter_id),
        "lineID": (TAG_INT, chapter_id),
        "order": (TAG_INT, int(source.get("order:3", old_chapter_id))),
        "properties": convert_properties(source.get("properties:10", {}), audit),
        "quests": (TAG_LIST, (TAG_MAP if quest_entries else TAG_END, quest_entries)),
    }
    return old_chapter_id, TAG_MAP, out


def write_xbt(path: Path, tag: tuple[int, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = XBTWriter().write_root(tag)
    with gzip.GzipFile(filename="", mode="wb", fileobj=path.open("wb"), mtime=0) as handle:
        handle.write(raw)


def load_item_ids(path: Path | None) -> set[str]:
    if not path or not path.exists():
        return set()
    return {line.strip() for line in path.read_text().splitlines() if re.match(r"^[a-z0-9_.-]+:[a-z0-9_./-]+$", line.strip())}


def load_rules(path: Path | None) -> dict[str, Any]:
    rules = {
        "item_mappings": {},
        "stack_mappings": {},
        "tag_mappings": {},
        "tag_mapping_keys": set(),
        "namespace_mappings": {},
        "drop_items": set(),
        "drop_stacks": set(),
        "drop_chapter_ids": set(),
        "drop_chapter_names": set(),
        "drop_quest_ids": set(),
        "drop_quest_names": set(),
        "prerequisite_replacements": {},
        "replace_missing_reward_stacks": False,
    }
    if not path:
        return rules
    data = json.loads(path.read_text())
    rules["item_mappings"].update(data.get("item_mappings", {}))
    rules["stack_mappings"].update(data.get("stack_mappings", {}))
    rules["tag_mappings"].update(data.get("tag_mappings", {}))
    rules["tag_mapping_keys"].update(key.split("|", 2)[1] for key in rules["tag_mappings"] if key.count("|") >= 2)
    rules["namespace_mappings"].update(data.get("namespace_mappings", {}))
    rules["drop_items"].update(data.get("drop_items", []))
    rules["drop_stacks"].update(data.get("drop_stacks", []))
    rules["drop_chapter_ids"].update(int(v) for v in data.get("drop_chapter_ids", []))
    rules["drop_chapter_names"].update(data.get("drop_chapter_names", []))
    rules["drop_quest_ids"].update(int(v) for v in data.get("drop_quest_ids", []))
    rules["drop_quest_names"].update(data.get("drop_quest_names", []))
    rules["prerequisite_replacements"].update(
        {int(key): [int(value) for value in values] for key, values in data.get("prerequisite_replacements", {}).items()}
    )
    rules["replace_missing_reward_stacks"] = bool(data.get("replace_missing_reward_stacks", False))
    return rules


def write_report(path: Path, audit: dict[str, Any], quest_count: int, chapter_count: int) -> None:
    missing_namespaces = Counter(key.split(":", 1)[0] for key in audit["missing_items"])
    lines = [
        "# BetterQuesting Port Audit",
        "",
        f"- Converted quests: {quest_count}",
        f"- Converted chapters: {chapter_count}",
        f"- Missing item IDs referenced by stacks: {len(audit['missing_items'])}",
        "",
        "## Task Types",
        "",
    ]
    lines += [f"- `{key}`: {value}" for key, value in audit["tasks"].most_common()]
    lines += ["", "## Reward Types", ""]
    lines += [f"- `{key}`: {value}" for key, value in audit["rewards"].most_common()]
    lines += ["", "## Dropped Legacy Properties", ""]
    if audit["dropped_props"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["dropped_props"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Dropped Chapters", ""]
    if audit["dropped_chapters"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["dropped_chapters"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Dropped Quests", ""]
    if audit["dropped_quests"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["dropped_quests"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Dropped Prerequisites", ""]
    if audit["dropped_prerequisites"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["dropped_prerequisites"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Replaced Prerequisites", ""]
    if audit["replaced_prerequisites"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["replaced_prerequisites"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Replaced Rewards", ""]
    if audit["replaced_rewards"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["replaced_rewards"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Dropped Stacks", ""]
    if audit["dropped_stacks"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["dropped_stacks"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Applied Item Mappings", ""]
    if audit["mapped_items"]:
        lines += [f"- `{key}`: {value}" for key, value in audit["mapped_items"].most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Missing Item Namespaces", ""]
    if missing_namespaces:
        lines += [f"- `{key}`: {value} distinct IDs" for key, value in missing_namespaces.most_common()]
    else:
        lines.append("- None")
    lines += ["", "## Missing Item IDs", ""]
    if audit["missing_items"]:
        for key, value in audit["missing_items"].most_common():
            lines.append(f"- `{key}`: {value}")
    else:
        lines.append("- None")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def chapter_name(source: dict[str, Any]) -> str:
    props = source.get("properties:10", {}).get("betterquesting:10", {})
    return props.get("name:8", f"Chapter {source.get('lineID:3')}")


def should_drop_chapter(source: dict[str, Any], rules: dict[str, Any]) -> bool:
    chapter_id = int(source["lineID:3"])
    return chapter_id in rules["drop_chapter_ids"] or chapter_name(source) in rules["drop_chapter_names"]


def chapter_quest_ids(source: dict[str, Any]) -> set[int]:
    return {int(entry["id:3"]) for entry in source.get("quests:9", {}).values()}


def quest_name(source: dict[str, Any]) -> str:
    props = source.get("properties:10", {}).get("betterquesting:10", {})
    return props.get("name:8", f"Quest {source.get('questID:3')}")


def should_drop_quest(source: dict[str, Any], rules: dict[str, Any]) -> bool:
    quest_id = int(source["questID:3"])
    return quest_id in rules["drop_quest_ids"] or quest_name(source) in rules["drop_quest_names"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--item-ids", type=Path)
    parser.add_argument("--rules", type=Path)
    args = parser.parse_args()

    source = json.loads(args.source.read_text())
    audit = {
        "item_ids": load_item_ids(args.item_ids),
        "rules": load_rules(args.rules),
        "missing_items": Counter(),
        "mapped_items": Counter(),
        "tasks": Counter(),
        "rewards": Counter(),
        "dropped_props": Counter(),
        "dropped_stacks": Counter(),
        "dropped_chapters": Counter(),
        "dropped_quests": Counter(),
        "dropped_prerequisites": Counter(),
        "replaced_prerequisites": Counter(),
        "replaced_rewards": Counter(),
    }

    if args.out.exists():
        shutil.rmtree(args.out)

    kept_chapters = []
    allowed_quest_ids: set[int] = set()
    for chapter in source["questLines:9"].values():
        if should_drop_chapter(chapter, audit["rules"]):
            name = chapter_name(chapter)
            audit["dropped_chapters"][f"{chapter['lineID:3']}:{name}"] += len(chapter.get("quests:9", {}))
            continue
        kept_chapters.append(chapter)
        allowed_quest_ids.update(chapter_quest_ids(chapter))

    for quest in source["questDatabase:9"].values():
        quest_id = int(quest["questID:3"])
        if quest_id in allowed_quest_ids and should_drop_quest(quest, audit["rules"]):
            audit["dropped_quests"][f"{quest_id}:{quest_name(quest)}"] += 1
            allowed_quest_ids.remove(quest_id)

    quest_id_map = {quest_id: bq_full_id(quest_id) for quest_id in allowed_quest_ids}
    chapter_id_map = {int(chapter["lineID:3"]): bq_full_id(int(chapter["lineID:3"])) for chapter in kept_chapters}

    quest_dir = args.out / "data" / "quests"
    chapter_dir = args.out / "data" / "chapters"
    quest_count = 0
    for quest in source["questDatabase:9"].values():
        if int(quest["questID:3"]) not in allowed_quest_ids:
            continue
        quest_ref_id, tag_type, payload = convert_quest(quest, audit, quest_id_map, allowed_quest_ids)
        write_xbt(quest_dir / f"quest_{quest_ref_id}.xbt", (tag_type, payload))
        quest_count += 1

    chapter_count = 0
    for chapter in kept_chapters:
        chapter_ref_id, tag_type, payload = convert_chapter(
            chapter, audit, quest_id_map, chapter_id_map, allowed_quest_ids
        )
        write_xbt(chapter_dir / f"chapter_{chapter_ref_id}.xbt", (tag_type, payload))
        chapter_count += 1

    write_report(args.out / "questbook_port_audit.md", audit, quest_count, chapter_count)
    print(f"Converted {quest_count} quests and {chapter_count} chapters into {args.out}")
    print(f"Missing item IDs: {len(audit['missing_items'])}")


if __name__ == "__main__":
    main()
