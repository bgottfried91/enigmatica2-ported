#!/usr/bin/env python3
"""
Create a coarse coverage matrix between original E2 ZenScripts and KubeJS ports.

This is not a semantic verifier. It is a checklist generator that makes missing
or unexpectedly broad conversions visible enough to review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_PACK = Path("/mnt/i/minecraft/Instances/Enigmatica2-1.20.1")
DEFAULT_SOURCE = Path("/mnt/i/minecraft/Instances/Enigmatica 2 - E2/scripts")


ZS_PATTERNS = {
    "crafting_add": re.compile(r"\brecipes\.add(?:Shaped|ShapedMirrored|Shapeless)\b"),
    "crafting_remove": re.compile(r"\brecipes\.remove(?:Shaped|Shapeless)?\b"),
    "furnace": re.compile(r"\bfurnace\."),
    "jei_hide": re.compile(r"\brh\("),
    "oredict_add": re.compile(r"<ore:[^>]+>\.add\("),
    "oredict_remove": re.compile(r"<ore:[^>]+>\.remove\("),
    "machine_recipe": re.compile(r"\bmods\.[A-Za-z0-9_.]+\.(?:add|addRecipe|remove|removeRecipe)\b"),
    "property_change": re.compile(r"\.(?:maxStackSize|maxDamage)\s*="),
}

JS_PATTERNS = {
    "crafting_add": re.compile(r"\bevent\.(?:shaped|shapeless)\("),
    "crafting_remove": re.compile(r"\bevent\.remove\("),
    "furnace": re.compile(r"\bevent\.(?:smelting|blasting|smoking|campfireCooking)\("),
    "tags": re.compile(r"\bServerEvents\.tags\(|\bevent\.add\("),
    "custom_machine": re.compile(r"\bevent\.custom\("),
    "modify": re.compile(r"\bevent\.replaceInput\(|\bevent\.replaceOutput\("),
    "property_change": re.compile(r"\.(?:maxStackSize|maxDamage)\s*="),
    "tooltip": re.compile(r"\bItemEvents\.tooltip\("),
}


def count_patterns(text: str, patterns: dict[str, re.Pattern[str]]) -> dict[str, int]:
    return {name: len(pattern.findall(text)) for name, pattern in patterns.items()}


def normalize_name(path: Path) -> str:
    stem = path.stem.lower()
    return re.sub(r"[^a-z0-9]+", "", stem)


def likely_js_matches(zs_path: Path, js_paths: list[Path]) -> list[Path]:
    zs_key = normalize_name(zs_path)
    aliases = {
        "actuallyadditions": ["actuallyadditions"],
        "appliedenergistics": ["appliedenergistics"],
        "oredict": ["oredict"],
        "oredictatm": ["oredictatm"],
        "recipeconflicts": ["conflicts"],
        "advancedgenerators": ["advancedgenerators", "advgen"],
        "immersiveengineering": ["immersiveengineering"],
        "industrialforegoing": ["industrialforegoing"],
        "integrateddynamics": ["integrateddynamics"],
        "thermalexpansion": ["thermal"],
        "furnace": ["furnace"],
        "fluidcompatibility": ["fluidcompatibility"],
        "plates": ["plates"],
        "miscrecipes": ["misc"],
        "nuclearcraft": ["nuclearcraft"],
        "cyclic": ["cyclic", "itemproperties"],
        "mekanism": ["mekanism", "itemproperties"],
        "tooltips": ["tooltips"],
    }
    keys = aliases.get(zs_key, [zs_key])
    matches = []
    for js_path in js_paths:
        js_name = normalize_name(js_path)
        if any(key in js_name for key in keys):
            matches.append(js_path)
    return matches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    out_path = args.out or (args.pack / "audit" / "script_coverage.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    js_paths = sorted((args.pack / "kubejs" / "server_scripts").glob("*.js"))
    js_paths.extend(sorted((args.pack / "kubejs" / "client_scripts").glob("*.js")))
    js_paths.extend(sorted((args.pack / "kubejs" / "startup_scripts").glob("*.js")))
    zs_paths = sorted(args.source.glob("*.zs"))

    with out_path.open("w", encoding="utf-8") as fh:
        fh.write("# Script Port Coverage Checklist\n\n")
        fh.write("Counts are regex-based indicators for review, not proof of correctness.\n\n")
        fh.write(
            "| Original script | ZS lines | ZS operations | Candidate KubeJS | JS lines | JS operations | Review note |\n"
        )
        fh.write("|---|---:|---|---|---:|---|---|\n")

        for zs_path in zs_paths:
            zs_text = zs_path.read_text(encoding="utf-8", errors="replace")
            zs_counts = count_patterns(zs_text, ZS_PATTERNS)
            zs_ops = ", ".join(f"{k}:{v}" for k, v in zs_counts.items() if v) or "none"

            matches = likely_js_matches(zs_path, js_paths)
            if matches:
                js_text = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in matches)
                js_counts = count_patterns(js_text, JS_PATTERNS)
                js_ops = ", ".join(f"{k}:{v}" for k, v in js_counts.items() if v) or "none"
                js_lines = sum(path.read_text(encoding="utf-8", errors="replace").count("\n") + 1 for path in matches)
                js_names = ", ".join(f"`{path.name}`" for path in matches)
                note = "review mapped port"
            else:
                js_ops = "none"
                js_lines = 0
                js_names = ""
                note = "no obvious KubeJS match"

            fh.write(
                f"| `{zs_path.name}` | {zs_text.count(chr(10)) + 1} | {zs_ops} | "
                f"{js_names} | {js_lines} | {js_ops} | {note} |\n"
            )

    print(f"Wrote coverage checklist to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
