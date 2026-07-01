# Agent Notes

This repository is the Packwiz source for **Enigmatica 2 Ported**, a Forge
1.20.1 port of Enigmatica 2 / E2.

## Paths

- Packwiz source: `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1`
- Live test instance: `/mnt/i/minecraft/Instances/Enigmatica 2 Ported`
- Original 1.12 reference instance: usually referenced as `../Enigmatica 2 - E2`

Do not treat the live test instance as source of truth. Copy deliberate tested
changes back into this Packwiz source and run `packwiz refresh`.

## Tooling

- Pack manager: Packwiz
- Packwiz binary used locally: `/home/bgottfried91/gopath/bin/packwiz`
- Minecraft: `1.20.1`
- Forge: `47.4.10`
- Pack metadata: `pack.toml`
- Pack index: `index.toml`

Common commands:

```bash
/home/bgottfried91/gopath/bin/packwiz refresh
/home/bgottfried91/gopath/bin/packwiz curseforge add <project>
/home/bgottfried91/gopath/bin/packwiz modrinth add <project>
/home/bgottfried91/gopath/bin/packwiz curseforge export
```

Network operations may need explicit approval in sandboxed agent sessions.

## Repository Layout

- `mods/*.pw.toml`: Packwiz mod metadata.
- `config/`: Client/common configs and OpenLoader datapacks.
- `defaultconfigs/`: Forge server default configs copied into new worlds.
- `kubejs/`: Recipe, tag, tooltip, and item property scripts.
- `resourcepacks/`: Packwiz resource pack entries.
- `shaderpacks/`: Shader pack entries and placeholders.
- `tools/`: Local audit/conversion utilities.
- `audit/`: Human-readable investigation notes and generated reports.
- `reference/original-e2-scripts/`: 1.12 CraftTweaker scripts used as porting reference.

Generated exports such as `*.zip` and `*.mrpack` should not be committed.
Python caches should not be committed.

## Current Questbook Direction

The pack uses **FTB Quests**, not Better Questing.

- Current questbook source: `config/ftbquests/quests/`
- Random reward table: `config/ftbquests/quests/reward_tables/standard_random_reward.snbt`
- Reward review report: `audit/questbook_port/random_reward_pool.html`

Obsolete Better Questing generated outputs are intentionally ignored:

```gitignore
audit/questbook_port/generated_bq*/
```

Do not reintroduce Better Questing. Some conversion tools still reference BQ
because the original 1.12 questbook and reward pool came from Better Questing.

## Important Balance Work Already Done

- Thermal dynamo recipes and fuels were adjusted to model old augment-based
  progression where possible.
- Lapidary Dynamo fuel values include cross-mod gems/materials, including
  Thermal apatite.
- Compression Dynamo fuels include tagged crude oils plus Thermal light/heavy
  oil balancing.
- Advanced Generators fuel values are aligned with Compression Dynamo values.
- Iron Furnaces generator augment rates were reduced to line up more closely
  with Thermal Stirling Dynamo upgrade tiers.
- Mini Utilities ender lily support was added and greenhouse growth behavior was
  investigated.
- Croptopia food compatibility and Cooking for Blockheads bulk-crafting support
  were expanded.

## Worldgen And Structure Notes

- Main custom worldgen datapack: `config/openloader/data/e2_worldgen/`
- Actually Additions structure override:
  `config/openloader/data/e2_actually_additions/`
- The Actually Additions engineer house override adds one
  `actuallyadditions:greenhouse_glass` block to the open space above the crop
  area at structure-relative position `[2, 4, 8]`.
- Actually Additions engineer houses are weighted village-pool additions, not
  guaranteed once per village.
- Terralith is present as an optional/default-off worldgen option. The default
  path remains Biomes O' Plenty unless intentionally testing Terralith.

## Rendering And Performance Notes

- Distant Horizons, Embeddium, Oculus, and Complementary Shaders Unbound are the
  current preferred rendering stack.
- Bliss shaders caused white flashing when combined with Distant Horizons during
  testing; keep Bliss only as an alternate until retested.
- Distant Horizons config was tuned from the live instance, with LOD distance
  lowered to 128 after shader compatibility testing.
- ModernFix and FerriteCore were added after live testing with no immediate
  crashes.
- Java 25 was tested in the live instance with compact object headers. Keep Java
  launch-flag changes documented because compatibility can depend on Forge and
  graphics stack versions.

## Editing Guidelines

- Prefer KubeJS for recipe/tag/script changes.
- Prefer OpenLoader datapacks for data-driven worldgen, loot, fuel, and
  structure overrides.
- Prefer Packwiz metadata files for adding/removing mods; do not commit actual
  mod jars.
- After changing tracked files, run `packwiz refresh`.
- If copying from the live instance, copy only intentional config/data changes,
  not logs, saves, crash reports, or local caches.
- Avoid deleting audit/reference files unless they are clearly obsolete
  generated outputs.

## Git Notes

This repo may be used from WSL on a Windows-mounted drive. If Git reports
ownership or chmod issues, the working tree may need:

```bash
git config --global --add safe.directory /mnt/i/minecraft/Instances/Enigmatica2-1.20.1
git init --separate-git-dir ~/.local/share/git/engimatica2-1.20.1.git
```

Do not run destructive Git commands unless explicitly requested.
