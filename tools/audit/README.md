# KubeJS Port Audit Tools

These tools are local-only helpers for checking the E2 CraftTweaker-to-KubeJS port.
`tools/**` is ignored by Packwiz and is not shipped in exported modpack zips.

## Static Check

Run from anywhere:

```bash
python3 /mnt/i/minecraft/Instances/Enigmatica2-1.20.1/tools/audit/audit_kubejs_static.py
```

Outputs:

- `audit/static_findings.md`
- `audit/static_findings.csv`

The checker validates item IDs in loaded KubeJS server scripts against the imported
instance item dump. It prefers `Enigmatica 2 Ported (1)/kubejs/config/audit_item_ids.json`
when present, then falls back to `item_ids*.txt` dumps.

Recipe removals by ID are reported as informational until a recipe dump exists.
Pass `--recipes path/to/kubejs/config/audit_recipe_ids.json` to verify those too.

Current expected result:

```text
Findings: 0 errors, 0 warnings, 0 info
```

Verified recipe removals are tracked in `verified_recipe_removals.txt`. Add a
recipe ID there only after confirming the ID exists in the source mod jar and is
absent after the KubeJS recipe pass.

## Coverage Checklist

Run from anywhere:

```bash
python3 /mnt/i/minecraft/Instances/Enigmatica2-1.20.1/tools/audit/summarize_script_coverage.py
```

Output:

- `audit/script_coverage.md`

This generates a coarse review matrix comparing original `.zs` scripts to likely
KubeJS ports. The operation counts are intentionally approximate; they identify
which files deserve manual semantic review first.

## In-Game Item Dump

The reliable item-ID dump path is KubeJS' in-game registry dump command. In game,
run:

```text
/kubejs dump_registry minecraft:item
```

KubeJS writes one chat/log line per registry entry to
`Enigmatica 2 Ported (1)/logs/stdout-logs.txt`. Rebuild the audit item list with:

```bash
awk '/\[System\] \[CHAT\] List of all entries for registry minecraft:item:/{in_dump=1; next} in_dump && /\[System\] \[CHAT\] Total: [0-9]+ entries/{in_dump=0} in_dump && match($0, /\[System\] \[CHAT\] - ([a-z0-9_.-]+:[a-z0-9_\.\/-]+)/, m){print m[1]}' \
  'Enigmatica 2 Ported (1)/logs/stdout-logs.txt' | sort -u > \
  'Enigmatica 2 Ported (1)/item_ids_verified.txt'
```

The broader regex is intentional. Some valid registry IDs use digits, dots,
hyphens, or slashes in the namespace/path.

`kubejs_debug_dumps.disabled.js` is an experimental script-based dump template.
In this instance, `JsonIO.write(...)` logged success but did not produce visible
files, so prefer the command-log workflow for item IDs.

## Inspecting Mod Jars

Use the imported CurseForge instance as the source for installed jars:

```bash
cd /mnt/i/minecraft/Instances
find 'Enigmatica 2 Ported (1)/mods' -maxdepth 1 -type f | sed 's#.*/##' | sort
```

Find a likely jar by mod name:

```bash
find 'Enigmatica 2 Ported (1)/mods' -maxdepth 1 -type f | sed 's#.*/##' | rg -i 'mekanism|immersive|thermal|actually'
```

List recipe files in a jar:

```bash
unzip -l 'Enigmatica 2 Ported (1)/mods/Mekanism-1.20.1-10.4.16.80.jar' 'data/*/recipes/*'
```

Search a jar's file list for recipe, tag, or asset names:

```bash
unzip -l 'Enigmatica 2 Ported (1)/mods/ImmersivePetroleum-1.20.1-4.3.1-36.jar' | rg 'recipes|distillation|crude|diesel'
unzip -l 'Enigmatica 2 Ported (1)/mods/thermal_foundation-1.20.1-11.0.6.70.jar' | rg 'tags/items|plates|ingots'
```

Print a recipe JSON directly:

```bash
unzip -p 'Enigmatica 2 Ported (1)/mods/ImmersivePetroleum-1.20.1-4.3.1-36.jar' \
  'data/immersivepetroleum/recipes/distillationtower/oil.json'
```

Print tag JSON directly:

```bash
unzip -p 'Enigmatica 2 Ported (1)/mods/thermal_cultivation-1.20.1-11.0.1.24.jar' \
  'data/forge/tags/items/crops/flax.json'
```

When the exact jar name is awkward, use a shell glob only after checking it
matches one file:

```bash
find 'Enigmatica 2 Ported (1)/mods' -maxdepth 1 -type f -iname '*ImmersivePetroleum*.jar'
unzip -p 'Enigmatica 2 Ported (1)'/mods/*ImmersivePetroleum*.jar \
  'data/immersivepetroleum/recipes/distillationtower/oil.json'
```

Use jar data for these decisions:

- Recipe IDs: file `data/<namespace>/recipes/path/name.json` has recipe ID `<namespace>:path/name`.
- Recipe type: read the JSON `type` field and mirror that in `event.custom`.
- Input/output item IDs: prefer the item dump first, then confirm recipe JSON `item`, `tag`, and `result` fields.
- Tags: file `data/<namespace>/tags/items/path/name.json` defines tag `<namespace>:path/name`.
- Existing native tags: if a mod already ships the Forge tag needed by a recipe, do not add a duplicate KubeJS tag unless the tag is incomplete.
- Assets without items are not enough. A jar may contain textures/models for old or generated content; only use IDs confirmed by `item_ids_verified.txt` or recipe/tag JSON.

Typical workflow for a converted recipe:

1. Find whether the target mod is installed in `Enigmatica 2 Ported (1)/mods`.
2. Check `Enigmatica 2 Ported (1)/item_ids_verified.txt` for every output and concrete input item.
3. Inspect the current jar recipe JSON to verify recipe IDs and current recipe schema.
4. If replacing a recipe, add the removed current recipe ID to `verified_recipe_removals.txt` only after confirming the file exists in the jar.
5. Patch both Packwiz source and imported instance.
6. Run `node --check`, `audit_kubejs_static.py`, `diff -qr`, and `packwiz refresh`.
