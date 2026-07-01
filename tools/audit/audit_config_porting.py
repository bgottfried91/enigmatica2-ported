#!/usr/bin/env python3
"""Build a coarse config-porting inventory for the E2 1.12 -> 1.20.1 port."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re


ROOT = Path("/mnt/i/minecraft/Instances")
OLD_CONFIG = ROOT / "Enigmatica 2 - E2" / "config"
PACK = ROOT / "Enigmatica2-1.20.1"
PACK_CONFIG = PACK / "config"
PACK_DEFAULTCONFIGS = PACK / "defaultconfigs"
ACTIVE_CONFIG = ROOT / "Enigmatica 2 Ported (1)" / "config"
OUT = PACK / "audit" / "config_porting_inventory.md"


ALIASES = {
    "actuallyadditions": ["actuallyadditions", "actuallysubtractions"],
    "advgenerators": ["advgenerators", "advancedgenerators"],
    "aiimprovements": ["aiimprovements"],
    "appliedenergistics2": ["ae2", "appliedenergistics2", "appliedenergistics"],
    "apotheosis": ["apotheosis"],
    "appleskin": ["appleskin"],
    "attributefix": ["attributeslib", "attributefix"],
    "badwithernocookiereloaded": ["bwncr", "badwithernocookiereloaded"],
    "baubles": ["curios"],
    "betteradvancements": ["betteradvancements"],
    "betterquesting": ["betterquesting"],
    "biomesoplenty": ["biomesoplenty"],
    "bloodmagic": ["bloodmagic"],
    "botania": ["botania"],
    "bookshelf": ["bookshelf"],
    "brandon3055": ["brandon3055", "brandonscore", "draconicevolution"],
    "buildinggadgets": ["buildinggadgets", "buildinggadgets2"],
    "carryon": ["carryon"],
    "chisel": ["chisel"],
    "chiselsandbits": ["chiselsandbits"],
    "codechickenlib": ["ccl", "codechickenlib"],
    "cofh": ["cofhcore"],
    "commoncapabilities": ["commoncapabilities"],
    "compactmachines3": ["compactmachines", "compactmachines3"],
    "computercraft": ["computercraft", "cctweaked"],
    "cookingforblockheads": ["cookingforblockheads"],
    "cosmeticarmorreworked": ["cosmeticarmorreworked"],
    "ctm": ["ctm"],
    "cyclicores": ["cyclic"],
    "cyclicmagic": ["cyclic", "cyclicmagic"],
    "cyclopscore": ["cyclopscore"],
    "darkutils": ["darkutilities", "darkutils"],
    "defaultoptions": ["defaultoptions"],
    "ding": ["ding"],
    "elevatormod": ["openblockselevator"],
    "embers": ["embers"],
    "enderio": ["enderio"],
    "enderstorage": ["enderstorage"],
    "environmentalmaterials": ["environmentalmaterials"],
    "extremereactors": ["extremereactors", "extremereactors2"],
    "farmingforblockheads": ["farmingforblockheads"],
    "fastbench": ["fastbench", "fastworkbench"],
    "fastfurnace": ["fastfurnace"],
    "fpsreducer": ["fpsreducer"],
    "bbm": ["aiimprovements"],
    "immersiveengineering": ["immersiveengineering"],
    "immersivepetroleum": ["immersivepetroleum"],
    "immersivetech": ["immersivetechnology", "mctimmersivetechnology"],
    "incontrol": ["incontrol"],
    "industrialforegoing": ["industrialforegoing"],
    "integrateddynamics": ["integrateddynamics"],
    "integratedtunnels": ["integratedtunnels"],
    "integratedtunnelscompat": ["integratedtunnels"],
    "ironchest": ["ironchest", "ironchests"],
    "jaopca": ["jaopca"],
    "jei": ["jei"],
    "jeresources": ["jeresources"],
    "journeymap": ["journeymap"],
    "journeymapmodinfo": ["journeymap"],
    "kleeslabs": ["kleeslabs"],
    "lostcities": ["lostcities", "thelostcities"],
    "mcjtylib": ["mcjtylib"],
    "mctimmersivetechnology": ["immersivetechnology"],
    "mekanism": ["mekanism"],
    "minecolonies": ["minecolonies"],
    "minecoloniesnames": ["minecolonies"],
    "modularrouters": ["modularrouters"],
    "morphtool": ["morphtool"],
    "naturescompass": ["naturescompass"],
    "neat": ["neat"],
    "notenoughwands": ["notenoughwands"],
    "nuclearcraft": ["nuclearcraft"],
    "oreexcavation": ["oreexcavation"],
    "oreexcavationgroups": ["oreexcavation"],
    "oreexcavationoverrides": ["oreexcavation"],
    "oreexcavationshapes": ["oreexcavation"],
    "overpoweredarmorbar": ["overloadedarmorbar", "overpoweredarmorbar"],
    "patchouli": ["patchouli"],
    "placebo": ["placebo"],
    "pneumaticcraft": ["pneumaticcraft"],
    "pregenerator": ["pregen", "chunkpregenerator"],
    "psi": ["psi"],
    "quark": ["quark"],
    "refinedstorage": ["refinedstorage"],
    "refinedstorageaddons": ["refinedstorageaddons"],
    "rftools": ["rftools", "rftoolsbase", "rftoolscontrol", "rftoolsdim"],
    "scannable": ["scannable"],
    "solcarrot": ["solcarrot"],
    "structurize": ["structurize"],
    "storagedrawers": ["functionalstorage"],
    "tconstruct": ["tconstruct"],
    "tinkertoolleveling": ["tleveling", "tinkertoolleveling"],
    "toastcontrol": ["toastcontrol"],
    "torchmaster": ["torchmaster"],
    "twilightforest": ["twilightforest"],
    "valkyrielib": ["valkyrielib"],
    "xnet": ["xnet"],
    "zeta": ["zeta"],
}

KNOWN_REMOVED = {
    "additionalstructures",
    "ae2stuff",
    "ae2wirelessterminals",
    "additionalstructuresgeneral",
    "additionalstructuresstructures",
    "advancedrocketry",
    "advrocketry",
    "ancientwarfare",
    "animania",
    "animaniafarm",
    "armoryexpansion",
    "astralsorcery",
    "backpack",
    "betterbuilderswands",
    "bettercaves1122",
    "betterfps",
    "bettermineshafts",
    "bettermineshafts1122",
    "bibliocraft",
    "binniesmod",
    "blockcraftery",
    "bqstandard",
    "comforts",
    "conarm",
    "craftingtweaks",
    "custombackgrounds",
    "custommainmenu",
    "danknull",
    "demagnetize",
    "dirt2path",
    "discordsuite",
    "engineersdoors",
    "endercore",
    "environmentaltech",
    "exchangers",
    "extrabitmanipulation",
    "extrautils2",
    "fasterladderclimbing",
    "flatcoloredblocks",
    "foamfix",
    "forestry",
    "forgechunkloading",
    "ftbbackups",
    "ftblib",
    "ftbutilities",
    "funkylocomotion",
    "gendustry",
    "gendustryjei",
    "geographicraft",
    "guideapi",
    "harvestcraft",
    "harvestcraftfruittree",
    "horsetweaks",
    "ic2",
    "integrationforegoing",
    "invtweaks",
    "ironbackpacks",
    "jepb",
    "jeibees",
    "jeivillagers",
    "laserdrillores",
    "librarianlib",
    "libvulpes",
    "lootcapacitortooltips",
    "lunatriuscore",
    "magicbees",
    "malisiscore",
    "malisisdoors",
    "memorytester",
    "meecreeps",
    "moreoverlays",
    "movingworld",
    "multimob",
    "mysticalworld",
    "natura",
    "naturamodules",
    "nomobspawningontrees",
    "nutrition",
    "oldjavawarning",
    "openblocks",
    "opencomputers",
    "openmods",
    "openmodslibcore",
    "oredictinit",
    "p455w0rdslib",
    "phosphor",
    "playersdropheads",
    "plustic",
    "primitivemobs",
    "quickleafdecay",
    "randompatches",
    "reccomplex",
    "refinedstoragerequestify",
    "roots",
    "rustic",
    "schematica",
    "shadowfacts",
    "spiceoflife",
    "splash",
    "stg",
    "supersoundmuffler",
    "teamreborn",
    "teslacorelib",
    "thaumcraft",
    "thaumcraftgraphics",
    "thaumcraftmisc",
    "thaumcraftworld",
    "thaumicjei",
    "thaumicjeiitemstackaspects",
    "thaumictinkerer",
    "tinkermodules",
    "tombmanygraves",
    "torohealthmod",
    "toughnessbar",
    "unidict",
    "unlimitedchiselworks",
    "unloader",
    "waila",
    "wawla",
    "wizardry",
    "ynot",
}


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def config_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def rels(root: Path) -> list[str]:
    if not root.exists():
        return []
    return [str(path.relative_to(root)) for path in config_files(root)]


def installed_mod_keys() -> set[str]:
    keys: set[str] = set()
    for path in sorted((PACK / "mods").glob("*.pw.toml")):
        name = path.name.removesuffix(".pw.toml")
        keys.add(norm(name))
    return keys


def config_key(rel: str) -> str:
    path = Path(rel)
    if len(path.parts) > 1:
        return norm(path.parts[0])
    stem = path.name.rsplit(".", 1)[0]
    key = norm(stem)
    for suffix in ("common", "client", "server"):
        if key.endswith(suffix) and len(key) > len(suffix):
            return key[: -len(suffix)]
    return key


def bucket_by_key(paths: list[str]) -> dict[str, list[str]]:
    buckets: dict[str, list[str]] = defaultdict(list)
    for rel in paths:
        buckets[config_key(rel)].append(rel)
    return dict(buckets)


def alias_keys(key: str) -> list[str]:
    return ALIASES.get(key, [key])


def has_installed_alias(old_key: str, installed_keys: set[str]) -> bool:
    for alias in alias_keys(old_key):
        if any(alias == mod_key or mod_key.startswith(alias) for mod_key in installed_keys):
            return True
    return False


def is_known_removed(old_key: str) -> bool:
    return old_key in KNOWN_REMOVED or any(old_key.startswith(key) for key in KNOWN_REMOVED if len(key) >= 5)


def find_matches(old_key: str, current_buckets: dict[str, list[str]]) -> list[str]:
    matches: list[str] = []
    aliases = set(alias_keys(old_key))
    for current_key, current_paths in current_buckets.items():
        if current_key in aliases:
            matches.extend(current_paths)
    return sorted(set(matches))


def table(rows: list[tuple[str, str, str]]) -> str:
    lines = [
        "| Original config family | Current config candidates | Notes |",
        "|---|---|---|",
    ]
    for left, middle, right in rows:
        lines.append(f"| `{left}` | {middle} | {right} |")
    return "\n".join(lines)


def main() -> int:
    old_paths = rels(OLD_CONFIG)
    current_paths = rels(ACTIVE_CONFIG)
    pack_paths = rels(PACK_CONFIG)
    pack_default_paths = rels(PACK_DEFAULTCONFIGS)

    old_buckets = bucket_by_key(old_paths)
    current_buckets = bucket_by_key(current_paths)
    pack_set = set(pack_paths)
    installed_keys = installed_mod_keys()

    likely_current = []
    installed_without_config = []
    removed = []
    unknown = []

    for old_key, old_group in sorted(old_buckets.items()):
        matches = find_matches(old_key, current_buckets)
        if matches:
            tracked = [path for path in matches if path in pack_set]
            note = "tracked in Packwiz" if tracked else "current instance has defaults; not tracked in Packwiz source"
            likely_current.append((
                old_group[0] if len(old_group) == 1 else f"{old_group[0]} (+{len(old_group) - 1})",
                "<br>".join(f"`{m}`" for m in matches[:8]) + ("<br>..." if len(matches) > 8 else ""),
                note,
            ))
        elif is_known_removed(old_key):
            removed.append((
                old_group[0] if len(old_group) == 1 else f"{old_group[0]} (+{len(old_group) - 1})",
                "",
                "source mod is not installed in the 1.20.1 pack",
            ))
        elif has_installed_alias(old_key, installed_keys):
            installed_without_config.append((
                old_group[0] if len(old_group) == 1 else f"{old_group[0]} (+{len(old_group) - 1})",
                "",
                "mod appears installed, but the active instance did not generate a matching config family",
            ))
        else:
            unknown.append((
                old_group[0] if len(old_group) == 1 else f"{old_group[0]} (+{len(old_group) - 1})",
                "",
                "no obvious current config by name; needs manual mod mapping",
            ))

    current_only_by_key = {
        key: paths
        for key, paths in sorted(current_buckets.items())
        if not any(find_matches(old_key, {key: paths}) for old_key in old_buckets)
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("# Config Porting Inventory\n\n")
        fh.write("Generated from original E2 1.12 configs, Packwiz source configs, and the active 1.20.1 instance configs.\n\n")
        fh.write("## Summary\n\n")
        fh.write(f"- Original E2 config files: {len(old_paths)}\n")
        fh.write(f"- Active 1.20.1 instance config files: {len(current_paths)}\n")
        fh.write(f"- Packwiz source config files currently tracked: {len(pack_paths)}\n")
        fh.write(f"- Packwiz source defaultconfigs files currently tracked: {len(pack_default_paths)}\n")
        fh.write(f"- Original config families with likely current counterparts: {len(likely_current)}\n")
        fh.write(f"- Original config families for installed mods with no matching generated config: {len(installed_without_config)}\n")
        fh.write(f"- Original config families likely removed with missing mods: {len(removed)}\n")
        fh.write(f"- Original config families needing manual mapping: {len(unknown)}\n\n")

        fh.write("## Immediate Finding\n\n")
        if len(pack_paths) <= 3:
            fh.write(
                "The Packwiz source currently tracks only a few config files. Most 1.20.1 configs exist only in the imported CurseForge test instance, "
                "so porting should first decide which generated current configs need to be copied into Packwiz before values are edited.\n\n"
            )
        else:
            fh.write(
                "The Packwiz source now tracks a curated baseline of generated 1.20.1 configs. Remaining untracked counterparts are mostly client-only "
                "or user-preference configs that should be included only if the pack intentionally wants to manage those defaults. Forge server configs "
                "that apply to newly created worlds are tracked separately in defaultconfigs/.\n\n"
            )

        fh.write("## Likely Current Counterparts\n\n")
        fh.write(table(likely_current[:120]))
        fh.write("\n\n")

        fh.write("## Installed Mods With No Matching Generated Config\n\n")
        fh.write(table(installed_without_config[:120]))
        fh.write("\n\n")

        fh.write("## Likely Removed Mods\n\n")
        fh.write(table(removed[:120]))
        fh.write("\n\n")

        fh.write("## Needs Manual Mapping\n\n")
        fh.write(table(unknown[:160]))
        fh.write("\n\n")

        fh.write("## Current-Only Config Families\n\n")
        fh.write("These are generated by mods in the 1.20.1 pack without an obvious 1.12 config family match.\n\n")
        for key, paths in list(current_only_by_key.items())[:120]:
            fh.write(f"- `{key}`: " + ", ".join(f"`{p}`" for p in paths[:5]) + (" ..." if len(paths) > 5 else "") + "\n")

    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    "betterbuilderswands",
    "bettercaves1122",
    "betterfps",
    "bettermineshafts",
    "bettermineshafts1122",
    "blockcraftery",
    "endercore",
    "guideapi",
    "memorytester",
    "nutrition",
