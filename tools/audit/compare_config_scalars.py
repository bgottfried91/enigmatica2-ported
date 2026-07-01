#!/usr/bin/env python3
"""Compare scalar config values between old E2 configs and the 1.20 Packwiz baseline."""

from __future__ import annotations

from pathlib import Path
import argparse
import re


ROOT = Path("/mnt/i/minecraft/Instances")
OLD_ROOT = ROOT / "Enigmatica 2 - E2" / "config"
PACK_ROOT = ROOT / "Enigmatica2-1.20.1"
NEW_ROOT = PACK_ROOT / "config"
AUDIT_ROOT = PACK_ROOT / "audit"


def extract_values(path: Path) -> list[tuple[str, str, str]]:
    values: list[tuple[str, str, str]] = []
    section: list[str] = []
    for raw in path.read_text(errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        if line.endswith("{"):
            section.append(line[:-1].strip())
            continue
        if line == "}":
            if section:
                section.pop()
            continue

        cfg_match = re.match(r'([BIDS]):"?([^"=]+)"?=(.*)', line)
        if cfg_match:
            typ, key, value = cfg_match.groups()
            values.append((".".join(section + [key.strip()]), typ, value.strip()))
            continue

        toml_match = re.match(r'"?([^"=]+)"?\s*=\s*(.*)', line)
        if toml_match and not line.startswith("["):
            key, value = toml_match.groups()
            values.append((".".join(section + [key.strip()]), "=", value.strip()))
            continue

        if line.startswith("[") and line.endswith("]"):
            name = line.strip("[]").strip()
            section = [name] if name else []
    return values


def summarize_pair(old_file: Path, new_file: Path) -> list[str]:
    old_values = extract_values(old_file)
    new_values = extract_values(new_file)
    old_map = {key: (typ, value) for key, typ, value in old_values}
    new_map = {key: (typ, value) for key, typ, value in new_values}
    common = sorted(set(old_map) & set(new_map))
    changed = [key for key in common if old_map[key] != new_map[key]]
    old_only = sorted(set(old_map) - set(new_map))
    new_only = sorted(set(new_map) - set(old_map))

    lines = [
        f"## {old_file.relative_to(OLD_ROOT)} -> {new_file.relative_to(NEW_ROOT)}",
        "",
        f"- Parsed old scalar values: {len(old_values)}",
        f"- Parsed new scalar values: {len(new_values)}",
        f"- Same key/value pairs: {len(common) - len(changed)}",
        f"- Same key but changed value/type: {len(changed)}",
        f"- Old-only scalar keys: {len(old_only)}",
        f"- New-only scalar keys: {len(new_only)}",
    ]
    if changed:
        lines.extend(["", "Changed same-name keys:"])
        for key in changed[:120]:
            old_typ, old_value = old_map[key]
            new_typ, new_value = new_map[key]
            lines.append(f"- `{key}`: old `{old_typ}={old_value}` -> new `{new_typ}={new_value}`")
    if old_only:
        lines.extend(["", "Old-only keys sample:"])
        for key in old_only[:50]:
            lines.append(f"- `{key}` = `{old_map[key][1]}`")
    if new_only:
        lines.extend(["", "New-only keys sample:"])
        for key in new_only[:50]:
            lines.append(f"- `{key}` = `{new_map[key][1]}`")
    lines.append("")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("pairs", nargs="+", help="old-relative:new-relative")
    args = parser.parse_args()

    lines = [f"# {args.title}", "", "Generated comparison notes for config value porting.", ""]
    for pair in args.pairs:
        old_rel, new_rel = pair.split(":", 1)
        old_file = OLD_ROOT / old_rel
        new_file = NEW_ROOT / new_rel
        if not old_file.exists() or not new_file.exists():
            lines.extend([f"## {old_rel} -> {new_rel}", "", f"- Missing old or new file: `{old_file.exists()}` / `{new_file.exists()}`", ""])
            continue
        lines.extend(summarize_pair(old_file, new_file))

    out = AUDIT_ROOT / args.out
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
