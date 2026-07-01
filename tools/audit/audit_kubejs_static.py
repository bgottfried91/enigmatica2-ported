#!/usr/bin/env python3
"""
Static sanity checks for the E2 KubeJS port.

This intentionally uses conservative regex scanning instead of trying to execute
KubeJS. It catches the common conversion failures: nonexistent item IDs,
nonexistent tag targets, and recipe removals that need a recipe dump to verify.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PACK = Path("/mnt/i/minecraft/Instances/Enigmatica2-1.20.1")
DEFAULT_INSTANCE = Path("/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)")

STRING_RE = re.compile(r"""(['"`])((?:\\.|(?!\1).)*?)\1""")
ID_RE = re.compile(r"^[a-z0-9_.-]+:[a-z0-9_./-]+$")

KNOWN_NON_ITEM_NAMESPACES = {
    "enigmatica2",
    "forge",
    "kubejs",
    "minecraft",  # handled via item registry when in item contexts
}

RECIPE_TYPE_NAMESPACES = {
    "actuallyadditions",
    "immersivepetroleum",
    "immersiveengineering",
    "mekanism",
    "minecraft",
    "nuclearcraft",
    "tconstruct",
    "thermal",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    file: str
    line: int
    kind: str
    value: str
    detail: str


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def load_item_ids(instance: Path) -> set[str]:
    candidates = [
        instance / "kubejs/config/audit_item_ids.json",
        instance / "audit_item_ids.json",
        instance / "item_ids_verified.txt",
        instance / "item_ids_final.txt",
        instance / "item_ids_complete3.txt",
        instance / "item_ids_complete2.txt",
        instance / "item_ids_complete.txt",
    ]
    for candidate in candidates:
        if candidate.exists():
            if candidate.suffix == ".json":
                data = json.loads(candidate.read_text(encoding="utf-8", errors="replace"))
                return {str(item).strip() for item in data if ID_RE.match(str(item).strip())}
            return {
                line.strip()
                for line in candidate.read_text(encoding="utf-8", errors="replace").splitlines()
                if ID_RE.match(line.strip())
            }
    raise FileNotFoundError(f"No item_ids*.txt registry dump found in {instance}")


def load_recipe_ids(path: Path | None) -> set[str] | None:
    if path is None or not path.exists():
        return None
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        ids = set()
        for row in data:
            text = str(row).strip()
            if text == "id,type,output":
                continue
            recipe_id = text.split(",", 1)[0]
            if ID_RE.match(recipe_id):
                ids.add(recipe_id)
        return ids
    if path.suffix == ".csv":
        with path.open(newline="", encoding="utf-8", errors="replace") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames and "id" in reader.fieldnames:
                return {row["id"] for row in reader if row.get("id")}
    return {
        line.strip().split(",", 1)[0]
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if ID_RE.match(line.strip().split(",", 1)[0])
    }


def load_verified_removals(path: Path | None) -> set[str]:
    if path is None or not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip() and not line.strip().startswith("#")
    }


def is_tag(value: str) -> bool:
    return value.startswith("#")


def clean_id(value: str) -> str:
    return value[1:] if is_tag(value) else value


def looks_like_item_context(text: str, start: int) -> bool:
    prefix = text[max(0, start - 80) : start]
    suffix = text[start : min(len(text), start + 80)]
    context = prefix + suffix
    return any(
        marker in context
        for marker in (
            "event.add(",
            "event.shaped(",
            "event.shapeless(",
            "event.smelting(",
            "event.blasting(",
            "event.smoking(",
            "event.campfireCooking(",
            "output:",
            "input:",
            "ingredient:",
            "item:",
            "mold:",
            "result:",
        )
    )


def is_recipe_id_context(text: str, start: int) -> bool:
    prefix = text[max(0, start - 32) : start]
    return ".id(" in prefix


def is_tag_declaration_context(text: str, start: int) -> bool:
    line_start = text.rfind("\n", 0, start) + 1
    prefix = text[line_start:start]
    return ("event.add(" in prefix or "addMany(" in prefix) and prefix.count(",") == 0


def scan_file(
    path: Path,
    root: Path,
    item_ids: set[str],
    recipe_ids: set[str] | None,
    verified_removals: set[str],
) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = str(path.relative_to(root))
    findings: list[Finding] = []

    for match in STRING_RE.finditer(text):
        raw = match.group(2)
        value = raw.replace("\\'", "'").replace('\\"', '"')
        check_value = clean_id(value)
        if not ID_RE.match(check_value):
            continue

        line = line_number(text, match.start())
        prefix = text[max(0, match.start() - 64) : match.start()]
        namespace = check_value.split(":", 1)[0]

        if namespace in {"enigmatica2", "forge"}:
            continue

        if is_recipe_id_context(text, match.start()) or is_tag_declaration_context(text, match.start()):
            continue
        if "removeId:" in prefix:
            continue

        if "event.remove" in prefix and "id:" in prefix:
            if check_value in verified_removals:
                continue
            if recipe_ids is None:
                findings.append(
                    Finding(
                        "info",
                        rel,
                        line,
                        "recipe-removal-unverified",
                        check_value,
                        "Recipe ID removal cannot be verified until a recipe dump is provided.",
                    )
                )
            elif check_value not in recipe_ids:
                findings.append(
                    Finding(
                        "warning",
                        rel,
                        line,
                        "recipe-removal-missing",
                        check_value,
                        "No matching recipe ID found in the provided recipe dump.",
                    )
                )
            continue

        if is_tag(value):
            continue

        if "tag:" in prefix:
            continue

        if namespace in RECIPE_TYPE_NAMESPACES and "type:" in prefix:
            continue

        if "fluid:" in prefix:
            continue

        if check_value not in item_ids:
            findings.append(
                Finding(
                    "error",
                    rel,
                    line,
                    "missing-item",
                    check_value,
                    "Referenced item ID was not found in the imported instance item dump.",
                )
            )

    return findings


def write_reports(findings: list[Finding], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "static_findings.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["severity", "file", "line", "kind", "value", "detail"])
        for f in findings:
            writer.writerow([f.severity, f.file, f.line, f.kind, f.value, f.detail])

    md_path = out_dir / "static_findings.md"
    with md_path.open("w", encoding="utf-8") as fh:
        fh.write("# Static KubeJS Audit Findings\n\n")
        if not findings:
            fh.write("No findings.\n")
            return
        fh.write("| Severity | File | Line | Kind | Value | Detail |\n")
        fh.write("|---|---:|---:|---|---|---|\n")
        for f in findings:
            fh.write(
                f"| {f.severity} | `{f.file}` | {f.line} | {f.kind} | `{f.value}` | {f.detail} |\n"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--instance", type=Path, default=DEFAULT_INSTANCE)
    parser.add_argument("--recipes", type=Path, default=None, help="Optional recipe dump CSV or text file")
    parser.add_argument("--verified-removals", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    script_dirs = [
        args.pack / "kubejs" / "server_scripts",
        args.pack / "kubejs" / "client_scripts",
        args.pack / "kubejs" / "startup_scripts",
    ]
    out_dir = args.out or (args.pack / "audit")

    item_ids = load_item_ids(args.instance)
    recipe_ids = load_recipe_ids(args.recipes)
    verified_removals_path = args.verified_removals or (args.pack / "tools" / "audit" / "verified_recipe_removals.txt")
    verified_removals = load_verified_removals(verified_removals_path)

    findings: list[Finding] = []
    for script_dir in script_dirs:
        if not script_dir.exists():
            continue
        for path in sorted(script_dir.glob("*.js")):
            findings.extend(scan_file(path, args.pack, item_ids, recipe_ids, verified_removals))

    findings.sort(key=lambda f: ({"error": 0, "warning": 1, "info": 2}.get(f.severity, 9), f.file, f.line))
    write_reports(findings, out_dir)

    errors = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    infos = sum(1 for f in findings if f.severity == "info")
    print(f"Wrote audit reports to {out_dir}")
    print(f"Findings: {errors} errors, {warnings} warnings, {infos} info")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
