#!/usr/bin/env python3
"""Generate the OpenLoader E2 worldgen datapack.

This is intentionally table-driven. The old E2 source of truth was CoFH World
JSON in the 1.12 instance; 1.20.1 uses datapack worldgen instead.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "config/openloader/data/e2_worldgen"
DATA = PACK / "data"
AUDIT = ROOT / "audit/worldgen_porting_inventory.md"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def state(name: str) -> dict:
    return {"Name": name}


def block_target(block: str) -> dict:
    return {"predicate_type": "minecraft:block_match", "block": block}


def tag_target(tag: str) -> dict:
    return {"predicate_type": "minecraft:tag_match", "tag": tag}


def ore_config(size: int, targets: list[tuple[dict, str]], discard: float = 0.0) -> dict:
    return {
        "type": "minecraft:ore",
        "config": {
            "discard_chance_on_air_exposure": discard,
            "size": size,
            "targets": [
                {"target": target, "state": state(block)} for target, block in targets
            ],
        },
    }


def oil_sand_config() -> dict:
    return ore_config(
        24,
        [
            (block_target("minecraft:sand"), "thermal:oil_sand"),
            (block_target("minecraft:red_sand"), "thermal:oil_red_sand"),
        ],
    )


def disk_config(state_name: str, targets: list[str], radius: int, half_height: int = 2) -> dict:
    return {
        "type": "minecraft:disk",
        "config": {
            "half_height": half_height,
            "radius": {
                "type": "minecraft:uniform",
                "value": {"min_inclusive": 2, "max_inclusive": radius},
            },
            "state_provider": {
                "fallback": {
                    "type": "minecraft:simple_state_provider",
                    "state": state(state_name),
                },
                "rules": [],
            },
            "target": {
                "type": "minecraft:matching_blocks",
                "blocks": targets,
            },
        },
    }


def placement(feature: str, count: int | dict | None, min_y: int, max_y: int, *, chance: int | None = None, distribution: str = "uniform") -> dict:
    entries: list[dict] = []
    if chance:
        entries.append({"type": "minecraft:rarity_filter", "chance": chance})
    if count is not None:
        entries.append({"type": "minecraft:count", "count": count})
    entries.extend(
        [
            {"type": "minecraft:in_square"},
            {
                "type": "minecraft:height_range",
                "height": {
                    "type": f"minecraft:{distribution}",
                    "min_inclusive": {"absolute": min_y},
                    "max_inclusive": {"absolute": max_y},
                },
            },
            {"type": "minecraft:biome"},
        ]
    )
    return {"feature": feature, "placement": entries}


def add_modifier(path: str, biomes: str, features: str | list[str], step: str = "underground_ores") -> None:
    write_json(
        DATA / f"e2_worldgen/forge/biome_modifier/{path}.json",
        {"type": "forge:add_features", "biomes": biomes, "features": features, "step": step},
    )


def remove_modifier(path: str, biomes: str, features: str | list[str]) -> None:
    write_json(
        DATA / f"e2_worldgen/forge/biome_modifier/{path}.json",
        {"type": "forge:remove_features", "biomes": biomes, "features": features},
    )


def add_ore(name: str, size: int, count: int | dict | None, min_y: int, max_y: int, targets: list[tuple[dict, str]], biomes: str = "#minecraft:is_overworld", chance: int | None = None, distribution: str = "uniform") -> None:
    feature = f"e2_worldgen:{name}"
    write_json(DATA / f"e2_worldgen/worldgen/configured_feature/{name}.json", ore_config(size, targets))
    write_json(DATA / f"e2_worldgen/worldgen/placed_feature/{name}.json", placement(feature, count, min_y, max_y, chance=chance, distribution=distribution))
    add_modifier(f"e2_add_{name}", biomes, feature)


STONE_DEEPSLATE = [
    tag_target("minecraft:stone_ore_replaceables"),
    tag_target("minecraft:deepslate_ore_replaceables"),
]


def main() -> None:
    for sub in [DATA / "e2_worldgen/worldgen", DATA / "e2_worldgen/forge/biome_modifier", DATA / "forge"]:
        if sub.exists():
            shutil.rmtree(sub)

    # Vanilla replacements from old 00_minecraft.json, remapped for 1.20 terrain.
    # Ranges preserve E2's relative rarity while giving deepslate layers a real role.
    vanilla = [
        ("coal_ore", 14, 16, -32, 192, "minecraft:coal_ore", "minecraft:deepslate_coal_ore"),
        ("iron_ore", 8, 22, -48, 96, "minecraft:iron_ore", "minecraft:deepslate_iron_ore"),
        ("gold_ore", 5, 10, -64, 48, "minecraft:gold_ore", "minecraft:deepslate_gold_ore"),
        ("redstone_ore", 9, 14, -64, 16, "minecraft:redstone_ore", "minecraft:deepslate_redstone_ore"),
        ("diamond_ore", 5, 5, -64, 16, "minecraft:diamond_ore", "minecraft:deepslate_diamond_ore"),
        ("lapis_ore", 5, 5, -32, 64, "minecraft:lapis_ore", "minecraft:deepslate_lapis_ore"),
        ("emerald_ore", 5, 4, -16, 128, "minecraft:emerald_ore", "minecraft:deepslate_emerald_ore"),
    ]
    for name, size, count, min_y, max_y, stone, deep in vanilla:
        add_ore(name, size, count, min_y, max_y, [(STONE_DEEPSLATE[0], stone), (STONE_DEEPSLATE[1], deep)])

    add_ore("nether_quartz_ore", 14, 23, 10, 118, [(tag_target("minecraft:base_stone_nether"), "minecraft:nether_quartz_ore")], "#minecraft:is_nether")

    # Non-ore vanilla stone blobs from old 00_minecraft.json.
    stone_blobs = [
        ("dirt_blob", "minecraft:dirt", 33, 3, -64, 160),
        ("gravel_blob", "minecraft:gravel", 33, 4, -64, 160),
        ("diorite_blob", "minecraft:diorite", 33, 1, -32, 96),
        ("granite_blob", "minecraft:granite", 33, 1, -32, 96),
        ("andesite_blob", "minecraft:andesite", 33, 1, -32, 96),
    ]
    for name, block, size, count, min_y, max_y in stone_blobs:
        add_ore(name, size, count, min_y, max_y, [(tag_target("minecraft:base_stone_overworld"), block)])

    remove_modifier(
        "e2_remove_vanilla_overworld_ores",
        "#minecraft:is_overworld",
        [
            "minecraft:ore_coal_upper",
            "minecraft:ore_coal_lower",
            "minecraft:ore_iron_upper",
            "minecraft:ore_iron_middle",
            "minecraft:ore_iron_small",
            "minecraft:ore_gold",
            "minecraft:ore_gold_lower",
            "minecraft:ore_redstone",
            "minecraft:ore_redstone_lower",
            "minecraft:ore_diamond",
            "minecraft:ore_diamond_large",
            "minecraft:ore_diamond_buried",
            "minecraft:ore_lapis",
            "minecraft:ore_lapis_buried",
            "minecraft:ore_emerald",
            "minecraft:ore_dirt",
            "minecraft:ore_gravel",
            "minecraft:ore_granite_upper",
            "minecraft:ore_granite_lower",
            "minecraft:ore_diorite_upper",
            "minecraft:ore_diorite_lower",
            "minecraft:ore_andesite_upper",
            "minecraft:ore_andesite_lower",
        ],
    )
    remove_modifier("e2_remove_vanilla_nether_ores", "#minecraft:is_nether", "minecraft:ore_quartz_nether")

    # Thermal Foundation old 1.12 ore metadata mapping.
    thermal = [
        ("thermal_tin_ore", 6, 11, -32, 96, "thermal:tin_ore", "thermal:deepslate_tin_ore"),
        ("thermal_silver_ore", 6, 6, -48, 48, "thermal:silver_ore", "thermal:deepslate_silver_ore"),
        ("thermal_lead_ore", 6, 4, -48, 32, "thermal:lead_ore", "thermal:deepslate_lead_ore"),
        ("thermal_nickel_ore", 4, 5, -64, 32, "thermal:nickel_ore", "thermal:deepslate_nickel_ore"),
    ]
    for name, size, count, min_y, max_y, stone, deep in thermal:
        add_ore(name, size, count, min_y, max_y, [(STONE_DEEPSLATE[0], stone), (STONE_DEEPSLATE[1], deep)])
    add_ore("thermal_apatite_ore", 32, 1, 16, 160, [(STONE_DEEPSLATE[0], "thermal:apatite_ore"), (STONE_DEEPSLATE[1], "thermal:deepslate_apatite_ore")])
    remove_modifier(
        "e2_remove_thermal_ores",
        "#minecraft:is_overworld",
        [
            "thermal:tin_ore",
            "thermal:silver_ore",
            "thermal:lead_ore",
            "thermal:nickel_ore",
            "thermal:apatite_ore",
        ],
    )

    # Current 1.20 replacements for old mod ores.
    add_ore("actuallyadditions_black_quartz_ore", 3, 9, -16, 80, [(STONE_DEEPSLATE[0], "actuallyadditions:black_quartz_ore"), (STONE_DEEPSLATE[1], "actuallyadditions:black_quartz_ore")])
    remove_modifier("e2_remove_actuallyadditions_black_quartz", "#minecraft:is_overworld", "actuallyadditions:ore_black_quartz")

    add_ore("immersiveengineering_uranium_ore", 4, 10, -64, 32, [(STONE_DEEPSLATE[0], "immersiveengineering:ore_uranium"), (STONE_DEEPSLATE[1], "immersiveengineering:deepslate_ore_uranium")])
    add_ore("immersiveengineering_aluminum_ore", 5, 5, 0, 112, [(STONE_DEEPSLATE[0], "immersiveengineering:ore_aluminum"), (STONE_DEEPSLATE[1], "immersiveengineering:deepslate_ore_aluminum")])
    remove_modifier("e2_remove_immersiveengineering_ores", "#minecraft:is_overworld", ["immersiveengineering:bauxite", "immersiveengineering:uranium"])

    add_ore("mekanism_osmium_ore", 4, 10, -32, 64, [(STONE_DEEPSLATE[0], "mekanism:osmium_ore"), (STONE_DEEPSLATE[1], "mekanism:deepslate_osmium_ore")])
    remove_modifier("e2_remove_mekanism_osmium", "#mekanism:spawn_ores", ["mekanism:ore_osmium_upper", "mekanism:ore_osmium_middle", "mekanism:ore_osmium_small"])

    # Chisel stones from 07_chisel_stone.json. Basalt is now vanilla.
    add_ore("chisel_marble", 32, 2, 16, 64, [(tag_target("minecraft:base_stone_overworld"), "chisel:marble/raw")])
    add_ore("minecraft_basalt", 32, 2, -32, 32, [(tag_target("minecraft:base_stone_overworld"), "minecraft:basalt")])
    add_ore("chisel_limestone", 24, 2, 32, 80, [(tag_target("minecraft:base_stone_overworld"), "chisel:limestone/raw")])

    # Draconic Evolution keeps separate dimension-specific ore blocks.
    add_ore("draconicevolution_overworld_draconium_ore", 8, None, -64, -48, [(STONE_DEEPSLATE[0], "draconicevolution:overworld_draconium_ore"), (STONE_DEEPSLATE[1], "draconicevolution:deepslate_draconium_ore")], chance=10)
    add_ore("draconicevolution_nether_draconium_ore", 32, None, 4, 16, [(tag_target("minecraft:base_stone_nether"), "draconicevolution:nether_draconium_ore")], "#minecraft:is_nether", chance=30)
    add_ore("draconicevolution_end_draconium_ore", 8, 3, 0, 70, [(block_target("minecraft:end_stone"), "draconicevolution:end_draconium_ore"), (tag_target("minecraft:base_stone_end"), "draconicevolution:end_draconium_ore")], "#minecraft:is_end")
    remove_modifier("e2_remove_draconicevolution_ores_overworld", "#minecraft:is_overworld", "draconicevolution:overworld_draconium_ore")
    remove_modifier("e2_remove_draconicevolution_ores_nether", "#minecraft:is_nether", "draconicevolution:nether_draconium_ore")
    remove_modifier("e2_remove_draconicevolution_ores_end", "#minecraft:is_end", "draconicevolution:end_draconium_ore")

    # Thermal oil sand approximation. Old oil geodes/clathrates no longer exist,
    # so this follows Thermal's 1.20 sand/red-sand replacement style.
    write_json(DATA / "e2_worldgen/worldgen/configured_feature/thermal_oil_sand_disk.json", oil_sand_config())
    write_json(DATA / "e2_worldgen/worldgen/placed_feature/thermal_oil_sand_disk.json", placement("e2_worldgen:thermal_oil_sand_disk", 2, 40, 80))
    add_modifier("e2_add_thermal_oil_sand_disk", "#minecraft:is_overworld", "e2_worldgen:thermal_oil_sand_disk", "underground_ores")
    remove_modifier("e2_remove_thermal_oil_sand", "#minecraft:is_overworld", "thermal:oil_sand")

    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(
        """# Worldgen Porting Inventory

Generated by `tools/worldgen/generate_e2_worldgen_datapack.py`.

## Ported

- Vanilla dirt/gravel/stone blobs and coal, iron, gold, redstone, diamond, lapis, emerald, and nether quartz using E2-inspired counts remapped for 1.20 terrain height and deepslate.
- Thermal tin, silver, lead, nickel, and Forestry apatite intent mapped to current `thermal:*_ore` blocks with 1.20-style stone/deepslate bands.
- Actually Additions black quartz.
- Immersive Engineering uranium and old Thermal aluminum intent mapped to current IE aluminum/bauxite.
- Mekanism osmium.
- Chisel marble and limestone.
- Old Chisel basalt mapped to vanilla `minecraft:basalt`, with decorative stone counts reduced for 1.20 cave exposure.
- Draconic Evolution overworld/nether/end draconium.
- Thermal oil sand approximated with Thermal's current sand/red-sand replacement style.

## Native Generation Disabled In Config

- `config/actuallyadditions-common.toml`: `blackQuartzGeneration = false`
- `config/Mekanism/world.toml`: `world_generation.osmium.shouldGenerate = false`
- `config/chisel-common.toml`: `worldgen.marble.enabled = false`, `worldgen.limestone.enabled = false`

## Retired Or Deferred

- CoFH `00_minecraft.json.old.json`: duplicate backup.
- Thermal copper: vanilla copper now owns copper generation.
- Thermal platinum/mana-infused/iridium and clathrates: no current Thermal ore block equivalents in this pack.
- Thermal pyrotheum/petrotheum/cryotheum lake features: old fluids are absent.
- Applied Energistics Certus ore: AE2 1.20 uses meteorite/budding quartz mechanics rather than normal ore blocks.
- Forestry apatite block: Forestry is absent; mapped only to Thermal apatite.
- Thaumcraft amber/cinnabar: Thaumcraft is absent. Thermal cinnabar remains native for now unless we intentionally retune it.
- Advanced Rocketry/Astral Sorcery/LibVulpes/RFTools planet ores: source mods or ore blocks are absent.
- NuclearCraft old large fractal mixed veins: vanilla datapack ore features do not support CoFH's fractal/sparse generator shape directly. Use NuclearCraft's native ore generation or design a separate approximation after testing.
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
