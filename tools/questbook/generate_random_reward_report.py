#!/usr/bin/env python3
"""Generate an HTML review report for the FTB Quests random reward table."""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import convert_legacy_bq as legacy  # noqa: E402
import convert_legacy_bq_to_ftb as ftb  # noqa: E402


def title_for(item_id: str) -> str:
    name = item_id.split(":", 1)[-1]
    name = name.replace("/", " / ").replace("_", " ").replace("-", " ")
    return " ".join(part.capitalize() for part in name.split())


def pct(weight: float, total: float) -> str:
    value = weight / total * 100 if total else 0
    if value >= 1:
        return f"{value:.2f}%"
    if value >= 0.1:
        return f"{value:.3f}%"
    return f"{value:.4f}%"


def one_in(weight: float, total: float) -> str:
    if weight <= 0:
        return "never"
    value = total / weight
    if value < 10:
        return f"about 1 in {value:.1f}"
    return f"about 1 in {value:.0f}"


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def build_entries(
    loot_path: Path,
    item_ids_path: Path | None,
    rules_path: Path | None,
    remove_list_path: Path | None,
) -> tuple[list[dict[str, Any]], list[tuple[str, str, int, int, str]], int]:
    loot = json.loads(loot_path.read_text(encoding="utf-8"))
    audit = ftb.build_audit(legacy.load_item_ids(item_ids_path), legacy.load_rules(rules_path))
    removals = ftb.load_random_reward_removals(remove_list_path)
    entries: list[dict[str, Any]] = []
    skipped: list[tuple[str, str, int, int, str]] = []
    source_total = 0

    for group_idx, group in enumerate(legacy.old_collection_to_list(loot.get("groups:9", {}))):
        if not isinstance(group, dict):
            continue
        group_name = group.get("name:8", f"Group {group_idx}")
        group_weight = ftb.old_weight(group)
        for reward in legacy.old_collection_to_list(group.get("rewards:9", {})):
            if not isinstance(reward, dict):
                continue
            reward_weight = ftb.old_weight(reward)
            for stack in ftb.stack_values(reward.get("items:9", {})):
                source_total += 1
                original_id = stack.get("id:8") or stack.get("id") or "minecraft:air"
                original_damage = ftb.stack_damage(stack)
                original_count = int(stack.get("Count:3", stack.get("Count", stack.get("count", 1))))
                mapped = ftb.map_stack(stack, audit, validate_item_id=False)
                if mapped is None:
                    skipped.append((group_name, original_id, original_damage, original_count, "unmapped"))
                    continue
                item_id, count = mapped
                if audit["item_ids"] and item_id not in audit["item_ids"] and item_id != "minecraft:air":
                    skipped.append((group_name, original_id, original_damage, original_count, f"missing mapped item {item_id}"))
                    continue
                if (item_id, count) in removals:
                    skipped.append((group_name, original_id, original_damage, original_count, f"removed by review list as {item_id} x{count}"))
                    continue
                entries.append({
                    "group": group_name,
                    "group_weight": group_weight,
                    "entry_weight": reward_weight,
                    "weight": group_weight * reward_weight,
                    "item": item_id,
                    "count": count,
                    "original": original_id,
                    "damage": original_damage,
                    "original_count": original_count,
                })
    return entries, skipped, source_total


def aggregate(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: dict[tuple[str, int], dict[str, Any]] = {}
    for entry in entries:
        key = (entry["item"], entry["count"])
        if key not in rows:
            rows[key] = {
                "item": entry["item"],
                "title": title_for(entry["item"]),
                "count": entry["count"],
                "weight": 0.0,
                "entries": 0,
                "groups": Counter(),
            }
        row = rows[key]
        row["weight"] += entry["weight"]
        row["entries"] += 1
        row["groups"][entry["group"]] += entry["weight"]
    return sorted(rows.values(), key=lambda r: (-r["weight"], r["item"], r["count"]))


def group_mix(groups: Counter, total_weight: float) -> str:
    return ", ".join(f"{esc(group)} {pct(weight, total_weight)}" for group, weight in groups.most_common())


def render_report(entries: list[dict[str, Any]], skipped: list[tuple[str, str, int, int, str]], source_total: int, loot_path: Path, rules_path: Path | None) -> str:
    total_weight = sum(entry["weight"] for entry in entries)
    agg_rows = aggregate(entries)
    entry_rows = sorted(entries, key=lambda e: (-e["weight"], e["group"], e["item"], e["count"]))

    group_weights: Counter = Counter()
    group_entries: Counter = Counter()
    for entry in entries:
        group_weights[entry["group"]] += entry["weight"]
        group_entries[entry["group"]] += 1
    skipped_by_mod = Counter((item.split(":", 1)[0] if ":" in item else item) for _, item, _, _, _ in skipped)

    removal_data = [
        {
            "item": row["item"],
            "count": row["count"],
            "title": row["title"],
            "weight": row["weight"],
            "chance": pct(row["weight"], total_weight),
            "human_readable": one_in(row["weight"], total_weight),
        }
        for row in agg_rows
    ]

    group_rows = "\n".join(
        f"""<tr>
<td>{esc(group)}</td>
<td class="num">{group_entries[group]}</td>
<td class="num">{weight:.2f}</td>
<td class="num strong">{pct(weight, total_weight)}</td>
<td class="num">{one_in(weight, total_weight)}</td>
</tr>"""
        for group, weight in group_weights.most_common()
    )

    agg_html = "\n".join(
        f"""<tr data-index="{idx}">
<td class="select"><input type="checkbox" class="remove-check" data-index="{idx}" aria-label="Select {esc(row['title'])}"></td>
<td class="item"><span class="title">{esc(row['title'])}</span><code>{esc(row['item'])}</code></td>
<td class="num">{row['count']}</td>
<td class="num">{row['weight']:.2f}</td>
<td class="num strong">{pct(row['weight'], total_weight)}</td>
<td class="num">{one_in(row['weight'], total_weight)}</td>
<td class="num">{row['entries']}</td>
<td>{group_mix(row['groups'], total_weight)}</td>
</tr>"""
        for idx, row in enumerate(agg_rows)
    )

    detailed_rows = "\n".join(
        f"""<tr>
<td>{esc(entry['group'])}</td>
<td class="item"><span class="title">{esc(title_for(entry['item']))}</span><code>{esc(entry['item'])}</code></td>
<td class="num">{entry['count']}</td>
<td class="num">{entry['group_weight']:.0f}</td>
<td class="num">{entry['entry_weight']:.0f}</td>
<td class="num">{entry['weight']:.2f}</td>
<td class="num strong">{pct(entry['weight'], total_weight)}</td>
<td class="num">{one_in(entry['weight'], total_weight)}</td>
<td><code>{esc(entry['original'])}:{entry['damage']}</code> x{entry['original_count']}</td>
</tr>"""
        for entry in entry_rows
    )

    skipped_rows = "\n".join(
        f"""<tr>
<td>{esc(group)}</td>
<td><code>{esc(item)}:{damage}</code></td>
<td class="num">{count}</td>
<td>{esc(reason)}</td>
</tr>"""
        for group, item, damage, count, reason in skipped
    )

    removal_json = json.dumps(removal_data, ensure_ascii=False)
    rules_label = str(rules_path) if rules_path else "default rules"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Enigmatica 2 Ported - Random Quest Reward Pool</title>
<style>
:root {{ color-scheme: light; --bg:#f6f7f9; --panel:#fff; --text:#1f2933; --muted:#667085; --line:#d9dee7; --head:#172033; --accent:#1f6feb; --soft:#eaf2ff; --danger:#b42318; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font:14px/1.45 system-ui, -apple-system, Segoe UI, sans-serif; }}
header {{ background:var(--head); color:white; padding:28px 36px; }}
h1 {{ margin:0 0 8px; font-size:28px; letter-spacing:0; }}
header p {{ margin:0; max-width:1050px; color:#d7dce7; }}
main {{ padding:24px 36px 48px; max-width:1500px; margin:0 auto; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; margin-bottom:22px; }}
.card {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.card .label {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.04em; }}
.card .value {{ font-size:24px; font-weight:700; margin-top:4px; }}
section {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; margin:18px 0; overflow:hidden; }}
section h2 {{ margin:0; padding:16px 18px; font-size:18px; border-bottom:1px solid var(--line); background:#fbfcfe; }}
.note {{ margin:0; padding:12px 18px; color:var(--muted); border-bottom:1px solid var(--line); }}
.toolbar {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; padding:12px 18px; border-bottom:1px solid var(--line); background:#fbfcfe; }}
button {{ border:1px solid #b7c3d7; background:white; color:#1f2933; border-radius:6px; padding:7px 10px; font:inherit; cursor:pointer; }}
button.primary {{ background:var(--accent); border-color:var(--accent); color:white; }}
button.danger {{ color:var(--danger); border-color:#f2b8b5; }}
button:hover {{ filter:brightness(.97); }}
.status {{ margin-left:auto; color:var(--muted); }}
textarea {{ width:100%; min-height:170px; border:0; border-top:1px solid var(--line); padding:12px 18px; font:12px/1.4 ui-monospace, SFMono-Regular, Consolas, monospace; resize:vertical; }}
table {{ width:100%; border-collapse:collapse; }}
th, td {{ padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top; }}
th {{ position:sticky; top:0; background:#eef2f8; color:#334155; text-align:left; font-size:12px; text-transform:uppercase; letter-spacing:.035em; z-index:1; }}
tr:hover td {{ background:var(--soft); }}
.select {{ width:42px; text-align:center; }}
.num {{ text-align:right; white-space:nowrap; font-variant-numeric:tabular-nums; }}
.strong {{ font-weight:700; }}
.item .title {{ display:block; font-weight:650; }}
code {{ font-family:ui-monospace, SFMono-Regular, Consolas, monospace; font-size:12px; color:#334155; background:#f1f4f8; border:1px solid #e1e6ef; border-radius:4px; padding:1px 4px; }}
details {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; margin-top:18px; overflow:hidden; }}
summary {{ cursor:pointer; padding:16px 18px; font-weight:700; background:#fbfcfe; }}
.footer {{ color:var(--muted); margin-top:18px; }}
</style>
</head>
<body>
<header>
<h1>Random Quest Reward Pool</h1>
<p>Generated from the current FTB Quests conversion of the legacy BetterQuesting random loot table. Check rows in the aggregated table, then generate a remove-list file for either checked or unchecked rows.</p>
</header>
<main>
<div class="cards">
<div class="card"><div class="label">Actual Outcomes</div><div class="value">{len(agg_rows)}</div></div>
<div class="card"><div class="label">Weighted Entries</div><div class="value">{len(entries)}</div></div>
<div class="card"><div class="label">Total Weight</div><div class="value">{total_weight:.0f}</div></div>
<div class="card"><div class="label">Skipped Legacy Entries</div><div class="value">{len(skipped)}</div></div>
<div class="card"><div class="label">Legacy Source Entries</div><div class="value">{source_total}</div></div>
</div>

<section>
<h2>Chance By Legacy Group</h2>
<p class="note">This shows how much of the current flat FTB table is contributed by each old BetterQuesting loot group after unmapped entries are removed.</p>
<table><thead><tr><th>Group</th><th class="num">Kept Entries</th><th class="num">Total Weight</th><th class="num">Chance</th><th class="num">Human Readable</th></tr></thead><tbody>
{group_rows}
</tbody></table>
</section>

<section>
<h2>Aggregated Reward Outcomes</h2>
<p class="note">Select items here to build a remove-list. The generated file is JSON so it can be pasted back into chat or used by a script later.</p>
<div class="toolbar">
<button type="button" id="select-all">Check All</button>
<button type="button" id="select-none">Check None</button>
<button type="button" id="invert-selection">Invert</button>
<button type="button" class="primary" id="download-checked">Download Checked Remove File</button>
<button type="button" id="download-unchecked">Download Unchecked Remove File</button>
<button type="button" id="copy-checked">Copy Checked JSON</button>
<button type="button" class="danger" id="clear-output">Clear Output</button>
<span class="status" id="selection-status">0 selected</span>
</div>
<table><thead><tr><th class="select">Remove</th><th>Reward</th><th class="num">Count</th><th class="num">Weight</th><th class="num">Chance Per Claim</th><th class="num">Human Readable</th><th class="num">Entries</th><th>Group Contribution</th></tr></thead><tbody>
{agg_html}
</tbody></table>
<textarea id="remove-output" readonly placeholder="Generated remove-list JSON will appear here."></textarea>
</section>

<section>
<h2>Detailed Weighted Entries</h2>
<p class="note">This lists the exact converted weighted entries feeding the FTB random reward table.</p>
<table><thead><tr><th>Legacy Group</th><th>Reward</th><th class="num">Count</th><th class="num">Group Weight</th><th class="num">Entry Weight</th><th class="num">Final Weight</th><th class="num">Chance</th><th class="num">Human Readable</th><th>Legacy Stack</th></tr></thead><tbody>
{detailed_rows}
</tbody></table>
</section>

<details>
<summary>Skipped legacy loot entries ({len(skipped)})</summary>
<p class="note">These old rewards were not included because the mapped item is not installed or the old mod/item no longer has a confident replacement. Top skipped namespaces: {", ".join(f"{esc(k)} ({v})" for k, v in skipped_by_mod.most_common(10))}.</p>
<table><thead><tr><th>Legacy Group</th><th>Legacy Stack</th><th class="num">Count</th><th>Reason</th></tr></thead><tbody>
{skipped_rows}
</tbody></table>
</details>

<p class="footer">Generated {esc(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))} from {esc(loot_path)} using {esc(rules_label)}.</p>
</main>
<script>
const rewardRows = {removal_json};
const checks = () => Array.from(document.querySelectorAll(".remove-check"));
const output = document.getElementById("remove-output");
const statusEl = document.getElementById("selection-status");

function selectedRows(useChecked) {{
  return checks()
    .filter(cb => cb.checked === useChecked)
    .map(cb => rewardRows[Number(cb.dataset.index)]);
}}

function buildPayload(useChecked) {{
  const rows = selectedRows(useChecked);
  return {{
    type: "enigmatica2_ported_random_reward_remove_list",
    selection: useChecked ? "checked" : "unchecked",
    generated_at: new Date().toISOString(),
    item_count: rows.length,
    remove: rows.map(row => ({{
      item: row.item,
      count: row.count,
      title: row.title,
      chance: row.chance,
      human_readable: row.human_readable,
      weight: row.weight
    }}))
  }};
}}

function refreshStatus() {{
  const selected = checks().filter(cb => cb.checked).length;
  statusEl.textContent = `${{selected}} selected / ${{rewardRows.length}} total`;
}}

function showPayload(useChecked) {{
  const payload = buildPayload(useChecked);
  output.value = JSON.stringify(payload, null, 2);
  return payload;
}}

function downloadPayload(useChecked) {{
  const payload = showPayload(useChecked);
  const blob = new Blob([JSON.stringify(payload, null, 2) + "\\n"], {{ type: "application/json" }});
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = useChecked ? "remove_checked_random_rewards.json" : "remove_unchecked_random_rewards.json";
  document.body.appendChild(link);
  link.click();
  URL.revokeObjectURL(link.href);
  link.remove();
}}

document.getElementById("select-all").addEventListener("click", () => {{ checks().forEach(cb => cb.checked = true); refreshStatus(); }});
document.getElementById("select-none").addEventListener("click", () => {{ checks().forEach(cb => cb.checked = false); refreshStatus(); }});
document.getElementById("invert-selection").addEventListener("click", () => {{ checks().forEach(cb => cb.checked = !cb.checked); refreshStatus(); }});
document.getElementById("download-checked").addEventListener("click", () => downloadPayload(true));
document.getElementById("download-unchecked").addEventListener("click", () => downloadPayload(false));
document.getElementById("copy-checked").addEventListener("click", async () => {{
  const payload = showPayload(true);
  await navigator.clipboard.writeText(JSON.stringify(payload, null, 2));
  statusEl.textContent = `Copied ${{payload.item_count}} checked items`;
}});
document.getElementById("clear-output").addEventListener("click", () => output.value = "");
checks().forEach(cb => cb.addEventListener("change", refreshStatus));
refreshStatus();
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--loot-source", type=Path, required=True)
    parser.add_argument("--item-ids", type=Path)
    parser.add_argument("--rules", type=Path)
    parser.add_argument("--remove-list", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    entries, skipped, source_total = build_entries(args.loot_source, args.item_ids, args.rules, args.remove_list)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_report(entries, skipped, source_total, args.loot_source, args.rules), encoding="utf-8")
    print(args.out)
    print(f"outcomes={len(aggregate(entries))} entries={len(entries)} skipped={len(skipped)} source={source_total}")


if __name__ == "__main__":
    main()
