# Enigmatica 2 Ported

Enigmatica 2 Ported is a work-in-progress Forge 1.20.1 port of the original
Enigmatica 2 experience. The goal is to preserve the broad kitchen-sink,
cross-mod progression feel of E2 while rebuilding recipes, quests, worldgen, and
balance around the modern 1.20.1 mod ecosystem.

This repository is the Packwiz source for the pack.

## Pack Details

- Minecraft: `1.20.1`
- Forge: `47.4.10`
- Packwiz format: `packwiz:1.1.0`
- Pack metadata: `pack.toml`
- Pack index: `index.toml`

## What Is In This Repo

- `mods/`: Packwiz mod metadata files.
- `config/`: Pack configs, FTB Quests data, and OpenLoader datapacks.
- `defaultconfigs/`: Default server configs for new worlds.
- `kubejs/`: Recipe, tag, tooltip, and item-property scripts.
- `resourcepacks/` and `shaderpacks/`: Packwiz-managed visual resources.
- `tools/`: Local audit and conversion scripts.
- `audit/`: Notes and reports from the porting/balancing process.
- `reference/`: Original E2 CraftTweaker scripts used as reference material.

Generated export archives are intentionally ignored by Git.

## Questbook

The pack uses FTB Quests. The active questbook lives in:

```text
config/ftbquests/quests/
```

The standard random reward table is:

```text
config/ftbquests/quests/reward_tables/standard_random_reward.snbt
```

Better Questing was used by the original 1.12 pack, but it is not the active
quest system for this port.

## Worldgen

Custom worldgen lives mostly in OpenLoader datapacks:

```text
config/openloader/data/
```

Biomes O' Plenty is the default overworld path. Terralith is included as an
optional/default-off worldgen option for testing or alternate world creation.

## Rendering Stack

The current preferred client rendering stack is:

- Embeddium
- Oculus
- Distant Horizons
- Complementary Shaders Unbound

Bliss shaders are present as an alternate, but earlier testing showed visual
flashing when Bliss was combined with Distant Horizons.

## Common Maintenance Commands

Run these from the repository root.

Refresh the Packwiz index after changing files:

```bash
/home/bgottfried91/gopath/bin/packwiz refresh
```

Add a CurseForge mod:

```bash
/home/bgottfried91/gopath/bin/packwiz curseforge add <project>
```

Add a Modrinth mod or shader/resource pack:

```bash
/home/bgottfried91/gopath/bin/packwiz modrinth add <project>
```

Export a CurseForge-compatible pack archive:

```bash
/home/bgottfried91/gopath/bin/packwiz curseforge export
```

## Development Notes

Prefer data-driven changes where practical:

- Recipes and tags: KubeJS.
- Datapack data, loot, fuels, structures, worldgen: OpenLoader.
- Mods/resource packs/shader packs: Packwiz metadata.

Do not commit generated exports, logs, saves, crash reports, mod jars, or Python
cache files.
