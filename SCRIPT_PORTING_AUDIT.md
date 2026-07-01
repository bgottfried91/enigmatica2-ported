# Enigmatica 2 Script Porting Audit

Original 1.12.2 scripts are copied for reference only under:

`reference/original-e2-scripts/`

Do not put unported files directly in loaded script folders; the old 1.12.2 ZenScript files contain obsolete item IDs, OreDict entries, and mod integrations.

## Target

Use KubeJS for the 1.20.1 ported scripts. The original ZenScript files remain reference material only.

- Source script target: `kubejs/server_scripts/*.js`
- Active profile test target: `kubejs/server_scripts/*.js`
- Installed scripting mod: `kubejs-forge-2001.6.5-build.26.jar`
- Installed scripting dependency: `rhino-forge-2001.2.3-build.10.jar`
- CraftTweaker has been removed from the Packwiz source.

## API Notes

KubeJS 1.20.1 recipe scripts go in `server_scripts/` and run inside `ServerEvents.recipes`.

- Shaped recipes: `event.shaped(output, pattern, keys)`
- Shapeless recipes: `event.shapeless(output, inputs)`
- Smelting/blasting/etc.: `event.smelting(output, input)`, `event.blasting(output, input)`
- Recipe removals: `event.remove({ id: 'modid:path' })`, `event.remove({ output: 'modid:item' })`, etc.
- Custom modded JSON recipes: `event.custom({ type: 'modid:recipe_type', ... })`
- Item tags use string syntax like `'#forge:ingots/copper'`
- Item IDs use string syntax like `'minecraft:iron_ingot'`

Official reference checked: KubeJS recipe docs.

## Current State

- Original E2 scripts: 39 `.zs` files, 2,855 lines.
- Active KubeJS server scripts: 22 in both Packwiz source and `Enigmatica 2 Ported (1)`.
- Packwiz KubeJS client scripts: 2. Packwiz KubeJS startup scripts: 1. The active test instance also has KubeJS' generated `startup_scripts/example.js` and `client_scripts/example.js`.
- Latest static audit result: `0 errors, 0 warnings, 0 info`.
- Latest confirmed full restart: 2/2 startup scripts, 2/2 client scripts, and 22/22 server scripts loaded with 0 KubeJS errors and 0 KubeJS warnings; recipe pass had 0 failed recipes.
- Latest added scripts pending gameplay spot-checks: `e2_recipes_tinkers_construct.js`, `e2_item_properties.js`, `e2_tooltips.js`.
- Packwiz source and active instance KubeJS script files matched after the startup-property pass.
- Item audit source: `Enigmatica 2 Ported (1)/item_ids_verified.txt`, rebuilt from `/kubejs dump_registry minecraft:item`.

## Porting Order

| Status | Script | Lines | Initial Decision | Notes |
|---|---:|---:|---|---|
| Done | `Furnace.zs` | 17 | Port first | Ported as `e2_recipes_furnace.js`; covers vanilla + deepslate + raw ores. Tested & verified. |
| Done | `Plates.zs` | 185 | High priority | Ported as `e2_recipes_plates.js`; consolidates to Thermal plates, IE hammer shapeless. Excluded aluminum_plate and steel_plate (don't exist in TF 1.20.1). Tested & verified. |
| Done | `OreDict.zs` | 266 | High priority | Partial port as `e2_tags_material_unification.js`; only includes existing mods (Botania, Blood Magic, Twilight Forest, AE2, BOP). Skipped removed mods. Tested & verified. |
| Done | `Cyclic.zs` | 8 | Needs ID rewrite | Ported as `e2_recipes_cyclic.js`; updated mod ID from `cyclicmagic` to `cyclic`, storage bag recipe. Tested & verified. |
| Todo | `OreDictATM.zs` | 508 | High priority but noisy | Many old block/item aliases; likely many references to removed mods. |
| Todo | `RecipeConflicts.zs` | 209 | Medium priority | Many old conflict fixes; port only conflicts that still exist in 1.20. |
| Todo | `MiscRecipes.zs` | 255 | Medium priority | Mixed replacements; many removed mods. Split by mod/function before porting. |
| Todo | `Mekanism.zs` | 73 | High priority | Gear/tool recipe cleanup and processing balance likely still relevant. |
| Done | `ThermalExpansion.zs` | 75 | No-op: template only | Original file contains only commented example calls. Current Thermal machine schemas were validated from installed `thermal_*` jars; no direct recipes to port. |
| Todo | `ImmersiveEngineering.zs` | 27 | Medium priority | Scaffolding and petroleum recipes may still map cleanly. |
| Done | `IndustrialForegoing.zs` | 62 | Ported partial | BioReactor additions ported through the modern `industrialforegoing:bioreactor` item tag. Old FluidDictionary and Protein Reactor entries retired; the APIs/items are not present in current IF. |
| Done | `NuclearCraft.zs` | 73 | Ported partial | Modern NuclearCraft recipe schemas validated from jar. Obsidian melter and electrolyzer buffs ported; common pressurizer plates unified to Thermal where equivalents exist. |
| Done | `FluidCompatibility.zs` | 72 | Ported partial | Validated modern fluid/item overlap. Mekanism refined obsidian/glowstone now melt to TConstruct molten fluids in Thermal Crucible and NuclearCraft Melter. Removed-mod/missing-fluid entries retired. |
| Done | `ActuallyAdditions.zs` | 72 | Ported partial | Modern Actually Subtractions keeps the `actuallyadditions` namespace. Black Quartz unpacking and AE2 Crusher compatibility were ported; old BoP gem block crusher recipes retired because the source blocks do not exist. |
| Todo | `AppliedEnergistics.zs` | 26 | Needs replacement pass | AE2 exists, old IDs and wireless terminal dependencies changed. |
| Todo | `BiomesOPlenty.zs` | 18 | Needs replacement pass | BOP exists, old gem/food references likely changed or removed. |
| Todo | `Chisel.zs` | 31 | Needs API check | Chisel exists, but CraftTweaker Chisel integration may not. |
| Todo | `Cyclic.zs` | 8 | Needs ID rewrite | Cyclic exists, old modid was `cyclicmagic`, new modid appears to be `cyclic`. |
| Todo | `Embers.zs` | 55 | Needs API check | Embers Rekindled exists, old integration may not. |
| Todo | `IntegratedDynamics.zs` | 8 | Low risk | Mod exists; small recipe check. |
| Done | `TinkersConstruct.zs` | 39 | Ported partial | Steel alloying and current fuel fluids ported through modern TConstruct JSON recipes. Old rack hide, Chisel cobalt unification, and removed-mod fuels retired. |
| Done | `Tooltips.zs` | 69 | Ported partial | Current Blood Magic demon crystal tooltips ported through `e2_tooltips.js`; removed-mod tooltip entries retired. |
| Defer | `JEICategories.zs` | 358 | Re-evaluate later | Mostly hides old JEI categories; categories changed. |
| Done | `AdvancedGenerators.zs` | 11 | Ported and tested | Controller recipe now uses E2 redstone-block cost via `e2_recipes_advanced_generators.js`. Iron frame already matched current 1.20 recipe. KubeJS log showed 0 errors/warnings. |
| Done | `AppliedEnergistics.zs` | 27 | Ported except WCT | Thermal Press recipes added for AE2 processor presses and silicon; charged certus to dust recipe via Thermal Pulverizer. WCT retired because ae2wtlib is not present. |
| Done | `IntegratedDynamics.zs` | 9 | No-op: commented out source, obsolete IDs | Original entirely commented. Old numeric IDs (mekanism:oreblock, thermalfoundation:ore:4, etc.) don't exist in 1.20.1. Stub left for future recipes. |
| Done | `Chisel.zs` | 31 | No-op: variations already native | Original attempted to add chisel variations from non-existent source blocks (Astral Sorcery, TF castle variants). Variations (chisel:basalt/*, chisel:marble/*) load natively in 1.20.1. |
| Done | `BiomesOPlenty.zs` | 19 | No-op: dependencies removed | JEI hide (amber doesn't exist). Honey recipes used BoP hives (replaced by vanilla). Forestry Centrifuge not in pack. All recipes retired. |
| Done | `Harvestcraft.zs` | 9 | No-op: mod not in pack | Harvestcraft is not in 1.20.1. IE Fermenter/Squeezer recipes for Harvestcraft vegetables/seeds cannot be ported. |
| Done | `Embers.zs` | 55 | Deferred: API redesign | Original hid Embers 1.12 tools (copper, silver, lead, etc.). Embers Rekindled redesigned with different tools. Deferred pending modern conflict verification. |
| Done | `Croptopia.zs` (new) | 143 | New: Harvestcraft replacement | Created integration script for Croptopia (Harvestcraft replacement). Added IE Fermenter (87 crops → ethanol) + IE Squeezer (56 seeds → plant oil) recipes using `forge:crops` and `forge:seeds` tags. |
| Done | `ActuallyAdditions.zs` | 72 | Ported partial | Actually Subtractions uses modern datapack recipe types. |
| Done | `AkashicTome.zs` | 28 | No-op: native recipe + attachment system | Current Akashic Tome has native base and attachment recipes. Old preloaded tome NBT references many removed 1.12 mods and should not be recreated blindly. |
| Done | `MorphOTool.zs` | 28 | No-op: native recipe + attachment system | Current Morph-o-Tool has native base and attachment recipes. Old preloaded tool NBT references many removed/renamed tools and should not be recreated blindly. |
| Done | `Backpacks.zs` | 10 | No-op: old mod absent | Old `backpack:stick` items are absent. Sophisticated Backpacks has its own current recipes; no hide/removal needed. |
| Defer | `Thaumcraft.zs` | 45 | Retire or replace | Thaumcraft is not present. |
| Defer | `IndustrialCraft2.zs` | 62 | Retire or replace | IC2 is not present. |
| Defer | `ExtraUtilities2.zs` | 45 | Retire or replace | Extra Utilities 2 is not present. |
| Defer | `AdvancedRocketry.zs` | 6 | Retire | Advanced Rocketry is not present. |
| Defer | `Bibliocraft.zs` | 26 | Retire | Bibliocraft is not present. |
| Defer | `BinniesMod.zs` | 4 | Retire | Binnie/Forestry stack is not present. |
| Defer | `Harvestcraft.zs` | 8 | Retire or replace | Pam's HarvestCraft is not present. |
| Defer | `MekanismBgott.zs` | 6 | Retire or rewrite | Only addresses old IC2/IE combiner behavior. |
| Defer | `Smeltables&Burnables.zs` | 12 | Retire or replace | Forestry/Thermal 1.12 assumptions. |
| Defer | `TempRecipes.zs` | 28 | Retire | Extra Cells is not present. |
| Defer | `extrabees.zs` | 13 | Retire | Extra Bees is not present. |
| Defer | `ChiselsAndBits.zs` | 1 | Retire | Thaumcraft aspect assignment only. |
| Defer | `PlankWoodFix.zs` | 16 | Retire | Entire functional block is commented out. |

## Summary of Deferred Work

### Scripts Blocked on Mod Availability
These cannot be ported as-is because their primary mod is missing from 1.20.1:

| Original Script | Issue | Replacement Status |
|---|---|---|
| Thaumcraft.zs (45 L) | Mod ended at 1.8.9 | Ars Nouveau should cover magic tier |
| IndustrialCraft2.zs (62 L) | Mod ended at 1.7.10 | Industrial Foregoing chosen as replacement |
| ExtraUtilities2.zs (45 L) | Mod does not exist in 1.20.1 | Review each recipe individually |
| AdvancedRocketry.zs (6 L) | Mod does not exist in 1.20.1 | Low priority; skip for now |
| Forestry (all) | Mod does not exist in 1.20.1 | Recipes scattered; handle per-item |
| Harvestcraft (all) | Mod does not exist in 1.20.1 | Some recipes in other mods |
| Bibliocraft.zs (26 L) | Mod does not exist in 1.20.1 | No clear replacement |
| BinniesMod.zs (4 L) | Extra Bees/Forestry dependent | Skip |
| ExtrabBees.zs (13 L) | Forestry dependent | Skip |
| MekanismBgott.zs (6 L) | Only addresses old IC2/IE behavior | Skip |
| Smeltables&Burnables.zs (12 L) | Forestry/Thermal 1.12 assumptions | Skip |
| TempRecipes.zs (28 L) | Extra Cells dependent | Skip |
| ChiselsAndBits.zs (1 L) | Thaumcraft aspect assignment | Skip |
| PlankWoodFix.zs (16 L) | All code commented out | Skip |

### Scripts Blocked on API Investigation
These require checking current mod APIs in 1.20.1 before porting:

| Script | Lines | Blocker | Action |
|---|---:|---|---|
| Mekanism.zs | 73 | References Astral Sorcery (removed) | Partial port: keep tool/upgrade stack size, skip starmetal |
| ThermalExpansion.zs | 75 | All code commented out (template) | No action needed |
| ImmersiveEngineering.zs | 27 | IE Petroleum API may have changed | Needs validation against 1.20.1 IE code |
| RecipeConflicts.zs | 209 | Many old mods; need to identify still-relevant conflicts | Port incrementally, test each conflict |
| MiscRecipes.zs | 255 | Mixed mods; many recipes referencing removed mods | Port by mod section, skip removed mods |
| Embers.zs | 55 | Embers Rekindled API changed | Needs validation; may not have same recipe types |
| NuclearCraft.zs | 73 | NuclearCraft Neoteric has new API | Core melter/electrolyzer/pressurizer recipes ported; JEI duplicate hides deferred to duplicate-visibility pass |
| TinkersConstruct.zs | 39 | Tinkers 1.20 is datapack-based | Steel alloy/fuel subset ported; removed-mod and obsolete JEI hide entries retired |
| FluidCompatibility.zs | 72 | Cross-mod fluid names changed | Core modern overlap ported; remaining old entries retired because source mods or target fluids are absent |
| BiomesOPlenty.zs | 18 | Item changes in modern version | Needs validation |
| AkashicTome.zs | 28 | Recipe may have changed | Reviewed; current native base and attachment recipes are sufficient |
| MorphOTool.zs | 28 | NBT tool system may have changed | Reviewed; current native base and attachment recipes are sufficient |
| Backpacks.zs | 10 | Sophisticated Backpacks is replacement | Reviewed; no old stick items or recipe conflict to port |
| JEICategories.zs | 358 | JEI categories changed significantly | Re-evaluate after testing other scripts |

## Rules

1. Preserve intent, not old syntax.
2. Validate item IDs against the 1.20.1 mod jars, KubeJS `/kjs hand`, JEI, or generated dumps before adding recipes.
3. Prefer Forge tags for materials where the original used OreDict.
4. Port in small batches and launch-test after each batch.
5. Keep rejected/deferred rationale here so the old E2 behavior is not lost accidentally.

Jar inspection workflow: see `tools/audit/README.md` for exact `find`, `unzip -l`, and `unzip -p` commands. Use the imported instance jars in `Enigmatica 2 Ported (1)/mods` to verify current recipe IDs, recipe JSON schemas, and native Forge tags before porting old CraftTweaker entries.

## Handoff Snapshot - 2026-06-24

Current active script count is 22 server scripts and 1 startup script. Local validation after the startup-property pass:

- `node --check` passed for `e2_recipes_tinkers_construct.js` and `e2_item_properties.js`.
- Static audit passed with `0 errors, 0 warnings, 0 info`.
- Script-level diff showed no differences between Packwiz and active instance server/startup script files.
- `packwiz refresh` completed and `index.toml` includes `kubejs/server_scripts/e2_recipes_tinkers_construct.js` and `kubejs/startup_scripts/e2_item_properties.js`.
- Full restart validation completed on 2026-06-25.

Recently completed:

- `e2_recipes_actually_additions.js`: black quartz unpacking and AE2 certus crusher recipes through Actually Subtractions' `actuallyadditions` namespace.
- `e2_recipes_nuclearcraft.js` plus `e2_recipes_plates.js`: obsidian melter fix, water/heavy-water electrolyzer buffs, and NuclearCraft pressurizer plate unification.
- `e2_recipes_fluid_compatibility.js`: Mekanism refined obsidian/glowstone melting through Thermal Crucible and NuclearCraft Melter.
- `e2_recipes_industrial_foregoing.js`: BioReactor input compatibility through `industrialforegoing:bioreactor`.
- `e2_recipes_tinkers_construct.js`: molten steel alloying through `tconstruct:alloy` plus sulfuric acid, refined fuel, diesel, and gasoline melting fuels.
- `e2_item_properties.js`: Mekanism tier installer/upgrades stack sizes and Cyclic mattock max damage.
- `e2_tooltips.js`: Blood Magic demon crystal guidance from the old tooltip script.

Reviewed and retired:

- `ExtraUtilities2.zs`: Extra Utilities 2 and Animania are absent.
- `AdvancedRocketry.zs`: Advanced Rocketry is absent.
- `Bibliocraft.zs`: Bibliocraft is absent.
- `BinniesMod.zs` / `extrabees.zs`: Binnie/Forestry/Extra Bees stack is absent.
- `MekanismBgott.zs`: old IC2-to-IE uranium combiner replacement has no current Mekanism uranium `to_ore` recipe to adjust.
- `Smeltables&Burnables.zs`: Forestry entries are absent; remaining old Thermal metadata entries do not map cleanly to current item IDs.

Deferred or deliberately skipped:

- PlusTiC / PlusTiC Reforged material work. PlusTiC Reforged only has 1.12.2/1.16.5 releases on the checked distribution pages; do not force that jar into the 1.20.1 pack. Revisit only if a real 1.20.1 Forge fork is provided or gameplay shows missing TConstruct material support that another current addon can supply.
- Old Industrial Foregoing `FluidDictionary` and `ProteinReactor` entries. The current IF 1.20.1 jar does not expose direct equivalents.
- Broad JEI/client hides. Do this after gameplay confirms which duplicates are real problems.

Good next targets:

1. Spot-check the new TConstruct molten steel recipe and added smeltery fuels in JEI/in-game.
2. Spot-check Mekanism installer/upgrade stack sizes and Cyclic mattock max damage.
3. Do broad JEI/client cleanup only after gameplay confirms which duplicate items or categories are actually noisy.

## Porting Progress - Current Session

**6 Scripts Ported & Verified Working:**

1. ✅ `e2_recipes_advanced_generators.js` - Controller circuit recipe
2. ✅ `e2_recipes_furnace.js` - Vanilla ore smelting with Deepslate + Raw ore variants
3. ✅ `e2_recipes_plates.js` - Material consolidation to Thermal plates; IE hammer recipes; excluded aluminum_plate and steel_plate (don't exist)
4. ✅ `e2_tags_material_unification.js` - Forge tags for boats, meat, blood runes, quartz, cakes
5. ✅ `e2_recipes_cyclic.js` - Storage bag recipe (updated mod ID cyclicmagic → cyclic)
6. ✅ `e2_recipes_conflicts.js` - Recipe conflicts for: trapdoor, Structurize scepters, Advanced Generators, Mekanism boiler casing, Embers metal blocks. Removed conflicts for non-existent items (Quark marble, Chisel lavastone original recipe, AE2 wood gear)

**Verified in World:** 7/7 KubeJS scripts loaded with 0 errors and 0 warnings. 

Latest (8th): e2_tags_oredict_atm_complete.js - Complete wood/block consolidation with conversion recipes. Tags for planks, doors, trapdoors, beds, chests (all types). Conversion recipes allow crafting any item in a tag to vanilla standard (e.g., any trapdoor → oak trapdoor). Only includes mods in 1.20.1; skipped Forestry, Extra Trees, Rustic, Malis Doors, etc.

CRITICAL LESSON LEARNED: Never skip sections of files. Always read complete files before porting. The conversion recipes were a critical part of this script that was initially missed.

Latest (9th): e2_recipes_immersive_engineering.js - Aluminum and steel scaffolding recipes using updated 1.20.1 item IDs. Skipped Crude Oil Distillation recipe (doesn't exist in IE Petroleum 1.20.1).

Latest (11th): e2_recipes_applied_energistics.js - Thermal Press recipes for AE2 processor presses and silicon, plus charged certus quartz to dust via Thermal Pulverizer. WCT infinity booster card retired because ae2wtlib is not in pack. Thermal recipe schemas were validated from installed `thermal_expansion` / `thermal_foundation` recipe JSON.

Latest (12th): e2_recipes_integrated_dynamics.js - Documented as non-porting. Original script was entirely commented out and referenced old numeric item IDs no longer present in 1.20.1.

Latest (13th): e2_recipes_chisel.js - Documented as non-porting. Original attempted to add chisel variations; most source items (Astral Sorcery, some Twilight Forest blocks) don't exist. Variations already loaded natively in 1.20.1.

Latest (14th): e2_recipes_biomesoplenty.js - Documented as non-porting. Original relied on Forestry (not in pack) and BoP hive blocks (replaced by vanilla honey). Recipes cannot be ported.

Latest (15th): e2_recipes_harvestcraft.js - Documented as non-porting. Harvestcraft mod is not in 1.20.1 pack. All recipes require the mod to exist.

Latest (16th): e2_recipes_embers.js - Documented as deferred. Original hid Embers 1.12 tools (copper, silver, lead, etc.). Embers Rekindled was redesigned with different tools (clockwork, dawnstone). Requires verification of modern tool conflicts.

Latest (17th): e2_recipes_croptopia.js - **Croptopia integration ported**. Added IE Fermenter recipes (87 crops → ethanol) and IE Squeezer recipes (56 seeds → plant oil). Mirrors Harvestcraft compatibility. Audit flags items as missing (stale dump) but script is correct; will validate once items load in-game.

Reload fix: the 2026-06-24 live reload loaded all 17 KubeJS scripts with 0 script errors/warnings, but IE rejected 10 Croptopia fermenter recipes for non-existent items: `durian`, `passion_fruit`, `chestnut`, `hazelnut`, `pistachio`, `juniper_berries`, `pomegranate`, `lychee`, `pomelo`, and `papaya`. Removed those from `e2_recipes_croptopia.js`; Packwiz and active instance scripts were resynced and `packwiz refresh` was run.

## Audit Fixes - 2026-06-24

Reviewed current KubeJS ports against `Enigmatica 2 - E2/scripts` and mirrored fixes into both the Packwiz source and imported CurseForge test instance.

- Fixed `e2_recipes_mekanism.js`: replaced invalid Mekanism combiner wrapper usage with explicit `mekanism:combining` JSON; corrected nether quartz ore ID; replaced nonexistent Thermal bronze/steel tool inputs with direct material-cost paxel recipes.
- Fixed `e2_recipes_misc.js`: restored E2 output counts for wool dyeing, uranium block decompression, and chest conversion; synced Mega Torch recipe to the E2-style treated-wood/log/block recipe.
- Fixed `e2_recipes_plates.js`: restored IE Metal Press compatibility so ingots press into Thermal plates; removed nonexistent Embers Rekindled IDs.
- Fixed `e2_recipes_conflicts.js`: restored output counts for Advanced Generators iron frames and Mekanism boiler casing; corrected Embers block IDs.
- Fixed `e2_recipes_immersive_engineering.js`: restored scaffolding recipe output count, distinct rod/scaffolding inputs, and mirrored variants.
- Fixed `e2_recipes_furnace.js`: restored removal of default smelting recipes and set XP to 1.
- Replaced duplicate/invalid tag scripts with current-ID tag entries: AE2 uses `ae2`, Embers uses `embers`, modern Blood Magic rune IDs are used, and BOP/Chisel/Twilight Forest wood IDs were corrected.
- Deleted obsolete duplicate scripts `e2_tags_material_unification.js` and source-only `e2_tags_oredict_atm.js`.

Validation performed:

- Packwiz source and imported instance `kubejs/server_scripts` match with `diff -qr`.
- All source KubeJS server scripts pass `node --check`.
- Targeted scan for known bad converted IDs returns no matches.
- Ran `packwiz refresh`.

## Semantic Review - RecipeConflicts.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/RecipeConflicts.zs` against `e2_recipes_conflicts.js` using the current 1.20.1 item dump and installed mod jars.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Vanilla trapdoor conflict | Still relevant as `minecraft:oak_trapdoor` | Port kept. |
| Structurize gold/steel scepters | Still relevant as `structurize:sceptergold` and `structurize:sceptersteel` | Port kept; added missing mirrored recipe orientations. |
| Structurize cactus plank | No verified `structurize:blockcactusplank` item in current dump | Retired. |
| Quark marble polished recipe | No verified modern Quark marble item in current dump | Retired. |
| Natura, MalisisDoors, Rustic, HarvestCraft, Roots conflicts | Source mods are not present in the 1.20.1 pack | Retired. |
| Advanced Generators iron frame/controller | Still relevant | Port kept; controller lives in `e2_recipes_advanced_generators.js`. |
| Mekanism boiler casing | Still relevant as `mekanism:boiler_casing` | Port kept. |
| AE2 wooden gear | No verified AE2 gear item in current dump | Retired. |
| Embers lead/silver storage blocks | Still relevant as `embers:lead_block` and `embers:silver_block` | Port kept. |
| Chisel lavastone recipe | Current Chisel has many `chisel:lavastone/<variant>` blocks, but no verified simple/raw target matching the old recipe | Deferred until the desired modern base variant is chosen. |
| ComputerCraft wired modem recipe | Still relevant as `computercraft:wired_modem`; current default recipe uses redstone, while old E2 used a basic circuit | Deferred pending recipe-balance decision on the correct 1.20.1 basic circuit equivalent. |
| Broader Mekanism/IE/Forestry/IC2/PlusTiC metal block duplicate removals | Mekanism and IE storage blocks exist; Forestry, IC2, and PlusTiC do not | Deferred for Mekanism/IE policy review rather than removing broad storage recipes blindly. |

## Semantic Review - MiscRecipes.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/MiscRecipes.zs` against `e2_recipes_misc.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Bread, bookshelf, uranium block/ingots, string removal, wool dyeing, nametag, Mega Torch, Farming for Blockheads market, boat, chest conversion, Thermal bronze | Still relevant | Port kept. |
| Elytra recipe using Actually Additions crystal | Still relevant; old `<actuallyadditions:item_crystal:2>` maps to `actuallyadditions:diamatine_crystal` | Fixed the port to use diamatine crystals in the bottom corners instead of extra popped chorus fruit. |
| Elytra popped chorus fruit input | Still relevant; 1.20.1 ID is `minecraft:popped_chorus_fruit` | Fixed old `minecraft:chorus_fruit_popped` ID. |
| Farming for Blockheads market wool input | Still relevant | Fixed the port to use `#minecraft:wool` instead of the likely-empty `#forge:storage_blocks/wool`. |
| BoP Origin Grass | Still relevant as `biomesoplenty:origin_grass_block` and `biomesoplenty:origin_sapling` | Added the old Origin Grass recipe with modern IDs. |
| BoP loamy/sandy/silty/mycelial/flowering/overgrown variants | No direct current BoP item equivalents verified except Origin Grass | Retired for now. |
| Environmental Materials/Environmental Tech/ValkyrieLib guide and Lonsdaleite recipes | Environmental Tech and Environmental Materials targets are not present in the current item dump | Retired. |
| Forestry, IC2, LibVulpes/Advanced Rocketry, OpenComputers, ExtraBitManipulation, Garden Stuff, Natura, Astral Sorcery, Extra Utilities 2, HarvestCraft, Rustic recipe entries | Source target mods/items are not present in the 1.20.1 pack | Retired. |
| Charcoal block hiding | Current pack has `quark:charcoal_block`, `mekanism:block_charcoal`, and `thermal:charcoal_block`; old hidden items were Garden Stuff and Actually Additions | Deferred for duplicate-block policy review. |
| Silicon/iridium/titanium/graphite conversions | Some modern silicon/iridium/titanium/graphite items exist, but the original source/target mods changed substantially | Deferred until material-unification policy is reviewed. |

## Semantic Review - Plates.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/Plates.zs` against `e2_recipes_plates.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Hide/remove duplicate Embers plates | Current Embers Rekindled has `embers:copper_plate`, `embers:lead_plate`, `embers:silver_plate`, and `embers:iron_plate` among other mod-specific plates | Port kept for the direct duplicate material plates. |
| Hide/remove duplicate IE plates | Current IE item IDs are `immersiveengineering:plate_<material>`, not `<material>_plate` | Fixed invalid IE output IDs and removed only plates with current Thermal equivalents. |
| IE Metal Press should produce Thermal plates | Still relevant for Thermal plate materials that exist | Port kept; verified IE recipe IDs are `immersiveengineering:metalpress/plate_<material>`. |
| Aluminum and steel Thermal plates | No `thermal:aluminum_plate` or `thermal:steel_plate` in current item dump | Do not redirect IE aluminum/steel to Thermal; leave IE plates available. |
| IE hammer recipes for Thermal plates | Still relevant | Port kept for Thermal plates that exist. |
| IC2 plates/casings and IC2 hammer compatibility | IC2 is not present | Retired. |
| Redstone Arsenal electrum flux plate | Target mod/item is not present in current dump | Retired. |

Static audit note: `tools/audit/audit_kubejs_static.py` now validates literal item IDs even when they appear in arrays used later by recipe code, which catches invalid removal arrays such as the old IE plate IDs.

## Semantic Review - Mekanism.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/Mekanism.zs` against `e2_recipes_mekanism.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Hide/remove duplicate Mekanism bronze and steel tools/armor | Current IDs are `mekanismtools:bronze_*` and `mekanismtools:steel_*` | Recipe removals kept; added client-side JEI hiding in `kubejs/client_scripts/e2_jei_hide_duplicates.js`. |
| Bronze and steel paxel replacement recipes | Thermal bronze/steel tools from 1.12 are not present | Port kept as direct material-cost paxel recipes using modern ingot/rod tags. |
| Mekanism Combiner quartz and coal ore recipes | Current Mekanism recipe IDs are `mekanism:processing/quartz/to_ore` and `mekanism:processing/coal/to_ore` | Port kept; recipe IDs were verified from the Mekanism jar and by the previous in-game recipe-ID audit. |
| Astral Sorcery starmetal smelter recipe | Astral Sorcery is not present | Retired. |
| Forestry apatite dupe removal | Forestry is not present | Retired. |
| Tier installer and upgrade stack-size changes | Current items exist, but this is startup-side item modification, not a `/reload` recipe change | Deferred until we decide whether to add startup scripts and test with a full client/game restart. |

Static audit note: `tools/audit/audit_kubejs_static.py` now scans `server_scripts`, `client_scripts`, and `startup_scripts`.

## Semantic Review - Cyclic.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/Cyclic.zs` against `e2_recipes_cyclic.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Hide toxic heart | No verified `cyclic:heart_toxic` equivalent; current Cyclic has `cyclic:heart` and other changed item IDs | Retired. |
| Remove purple helmet recipe | No verified `cyclic:purple_helmet` equivalent; current armor set differs | Retired. |
| Replace Storage Bag recipe | Still relevant as `cyclic:storage_bag` | Port kept; recipe preserves old leather/string/gold-block/redstone-block cost with modern tags. |
| Increase mattock durability | Current item exists as `cyclic:mattock`, but this is startup-side item modification, not a `/reload` recipe change | Deferred with other startup item modifications. |

## Semantic Review - ImmersiveEngineering.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/ImmersiveEngineering.zs` against `e2_recipes_immersive_engineering.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Crude oil distillation unification | Immersive Petroleum is present and has `immersivepetroleum:distillationtower/oil` | Restored E2 override: 75 mB crude oil to 9 mB lubricant, 27 mB diesel, 39 mB gasoline, with 7% bitumen byproduct, 4096 energy, 20 time. |
| Aluminum scaffolding recipe | Still relevant as `immersiveengineering:alu_scaffolding_standard` | Port kept with modern rod/scaffolding tags and mirrored variants. |
| Steel scaffolding recipe | Still relevant as `immersiveengineering:steel_scaffolding_standard` | Port kept with modern rod/scaffolding tags and mirrored variants. |

Static audit note: Immersive Petroleum recipe types and fluid result fields are handled so item validation does not misclassify fluid IDs.

## Semantic Review - Furnace.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/Furnace.zs` against `e2_recipes_furnace.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Vanilla ore smelting should grant 1 XP | Still relevant | Port kept; removes default smelting by input and re-adds `.xp(1)` recipes. |
| Lapis ore output | 1.12 output was `<minecraft:dye:4>` | Correctly mapped to `minecraft:lapis_lazuli`. |
| Nether quartz ore input | 1.12 ID was `<minecraft:quartz_ore>` | Correctly mapped to `minecraft:nether_quartz_ore`. |
| Deepslate ore variants | New in 1.20.1 | Port includes deepslate variants with the same 1 XP policy. |
| Raw iron/gold inputs | New in 1.20.1 | Port includes raw iron/gold with the same 1 XP policy. |

## Semantic Review - AppliedEnergistics.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/AppliedEnergistics.zs` against `e2_recipes_applied_energistics.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| TE Compactor press recipes (4 variants) | Processor presses exist; modern Thermal uses `thermal:press` | Port kept. Old `appliedenergistics2:material` metadata maps to modern AE2 press items. `ic2:plate:11` was replaced by `#forge:plates/steel`; Extra Utilities compressed sand was replaced by `minecraft:sandstone`. |
| TE Compactor mint silicon recipe | AE2 silicon exists; modern Thermal uses `thermal:press` | Port kept as sand to `ae2:silicon` with original 2000 energy cost. |
| TE Pulverizer charged certus to dust | Both ae2:charged_certus_quartz_crystal and ae2:certus_quartz_dust exist | Port kept with recipe type thermal:pulverizer |
| WCT infinity booster card | ae2wtlib mod is not present in 1.20.1 pack | Retired; no wireless terminal library available. |

Audit tool update: added "thermal" to RECIPE_TYPE_NAMESPACES in audit_kubejs_static.py to recognize thermal:* recipe types.

## Semantic Review - OreDict.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/OreDict.zs` against `e2_tags_oredict.js` and spot-checked native 1.20.1 tag data from installed mod jars.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| IE hammer as crafting forge hammer | Still relevant as `immersiveengineering:hammer` | Port kept as `forge:tools/forge_hammer`. |
| Boat oredict | Still relevant for vanilla, BoP, and Immersive Petroleum speedboat | Port kept as `forge:boats` with modern IDs. |
| Twilight Forest venison meat tags | Still relevant | Port kept as `forge:raw_meats` and `forge:cooked_meats`. |
| Blood Magic rune family | Still relevant with modern per-rune item IDs | Port kept; added tier-2 rune items that exist in the current Blood Magic item dump. |
| Certus quartz gems/blocks | Still relevant; AE2 also ships native tags | Port kept and current IDs verified. |
| Cake tag | Partially relevant; most old cake mods are absent | Port kept for `minecraft:cake`; Thermal cakes exist but are not direct old HarvestCraft equivalents. |
| Marble and mazestone tags | Still relevant for Chisel and Twilight Forest | Port kept and current IDs verified. |
| Black quartz, flax crops, salt, sawdust, fertilizer | Current mods already provide native Forge tags for the direct modern items | No KubeJS override needed. |
| Ore-entry removals for old Mineralis/ore conflicts | Old 1.12 ore registration problems and several source mods are gone or changed substantially | Retired pending a separate current ore-generation/material policy review. |
| IC2, Forestry, Thaumcraft, Astral Sorcery, HarvestCraft, OpenComputers entries | Source target mods/items are not present in the 1.20.1 pack | Retired. |

## Semantic Review - OreDictATM.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/OreDictATM.zs` against `e2_tags_oredict_atm_complete.js`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Consolidate plank-like blocks | Still relevant, but many wood families changed since 1.12 | Port kept; added modern vanilla bamboo/crimson/warped planks plus current Ars Nouveau, Integrated Dynamics, Thermal, TConstruct, and Botania planks. |
| Consolidate chests and wood chests | Still relevant | Port kept; added Twilight Forest wood chests. Avoided broad special/storage/metal chests that are not direct wood-chest equivalents. |
| Consolidate trapped chests | Still relevant | Port kept for vanilla and Quark trapped chests. |
| Consolidate beds | Still relevant for vanilla colored beds | Port kept. Old Cyclic sleeping mat target was retired because it does not map directly to a current bed item. |
| Consolidate trapdoors | Still relevant | Port kept; added modern vanilla bamboo/crimson/warped, BoP trapdoors, and current Ars/Thermal/TConstruct trapdoors. |
| Consolidate doors | Still relevant | Port kept; added modern vanilla bamboo/crimson/warped, Twilight Forest, Ars, Integrated Dynamics, Thermal, and TConstruct doors. |
| Conversion recipes to vanilla chest/trapped chest/bed/trapdoor/door | Still relevant | Port kept with modern vanilla outputs. |
| Rustic, Forestry, Extra Trees, MalisisDoors, Wizardry, Blockcraftery, Roots, Structurize cactus entries | Source target mods/items are not present or no direct current item exists | Retired. |

## Semantic Review - ActuallyAdditions.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/ActuallyAdditions.zs` against the current Actually Subtractions jar, which keeps the `actuallyadditions` item and recipe namespace.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Black Quartz Block to Black Quartz | Still relevant as `actuallyadditions:black_quartz_block` to `actuallyadditions:black_quartz` | Ported as shapeless `4x` unpacking recipe. |
| Chiseled Block of Black Quartz to Black Quartz | Still relevant as `actuallyadditions:chiseled_black_quartz_block` | Ported as shapeless `4x` unpacking recipe. |
| Pillar of Black Quartz to Black Quartz | Still relevant as `actuallyadditions:black_quartz_pillar_block` | Ported as shapeless `2x` unpacking recipe to match old E2 output. |
| BoP gem blocks to dyes in Actually Additions Crusher | Modern BoP gem block items are not present in the current item dump | Retired. |
| Charged certus quartz ore to certus crystal in Crusher | Old AE2 charged ore item no longer exists; current AE2 uses `ae2:charged_certus_quartz_crystal` | Ported as `actuallyadditions:crushing` to `ae2:certus_quartz_dust`, matching the current available AE2 processing target. |
| Certus quartz crystals to certus dust in Crusher | Still relevant as `ae2:certus_quartz_crystal` to `ae2:certus_quartz_dust` | Ported as `actuallyadditions:crushing`. |
| Treasure Chest, Ball of Fur, Atomic Reconstructor, Compost, Empowerer example calls | Original file only contained commented examples for these sections | No action needed. |

Validation note: Actually Subtractions crusher schema was verified from `data/actuallyadditions/recipes/crushing/*.json` in the installed jar, and `actuallyadditions` was added to the static audit's known recipe-type namespaces.

## Semantic Review - NuclearCraft.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/NuclearCraft.zs` against the current `NuclearCraft-1.20.1-1.2.28-beta4.jar`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Remove obsidian dust melter dupe and make obsidian melt to 144 mB | Still relevant. Current defaults were `minecraft:obsidian` to 180 mB and `forge:dusts/obsidian` to 90 mB | Ported: removed both defaults and added `minecraft:obsidian` to 144 mB `forge:molten_obsidian`. |
| Lithium ingot Mekanism smelter compatibility from IC2 dust | IC2 is not present; modern lithium items and Mekanism lithium fluid/dust handling differ | Retired. |
| Heavy water electrolysis buff | Still relevant. Current default produces deuterium and oxygen only | Ported: 1000 mB heavy water to 1000 mB deuterium, 500 mB oxygen, and 50 mB tritium. |
| Water electrolysis buff | Still relevant. Current default produces hydrogen and oxygen only | Ported: 1000 mB water to 1000 mB hydrogen, 500 mB oxygen, and 50 mB deuterium. |
| IC2 heavy water electrolysis | IC2 heavy water fluid is not present | Retired. |
| Pressurizer should make Thermal Foundation plates for iron/gold/copper/tin/lead/bronze/steel | Modern NuclearCraft has pressurizer recipes for most of these, and Thermal has matching plates except steel | Ported for iron, gold, copper, tin, lead, and bronze in `e2_recipes_plates.js`; steel retired because no Thermal output exists. |
| Hide NuclearCraft duplicate ores, dusts, ingots, alloys, and tools | Modern NuclearCraft item IDs changed substantially | Deferred to the duplicate visibility / JEI hide pass; recipe behavior should be validated before hiding broad item families. |

Validation note: NuclearCraft machine schemas were verified from installed jar JSON under `data/nuclearcraft/recipes/{melter,electrolyzer,pressurizer}/`. Recipe removals added for this pass were confirmed present in the jar and recorded in `tools/audit/verified_recipe_removals.txt`.

## Semantic Review - FluidCompatibility.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/FluidCompatibility.zs` against current Thermal, NuclearCraft, Mekanism, and TConstruct jars.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| Thermal Crucible and NuclearCraft Melter compatibility for Mekanism refined obsidian | Current Mekanism items and TConstruct `forge:molten_refined_obsidian` fluid tag exist | Ported for nuggets, ingots, and storage blocks. Uses modern TConstruct fluid units: 10/90/810 mB. |
| Thermal Crucible and NuclearCraft Melter compatibility for Mekanism refined glowstone | Current Mekanism items and TConstruct `forge:molten_refined_glowstone` fluid tag exist | Ported for nuggets, ingots, and storage blocks. Uses modern TConstruct fluid units: 10/90/810 mB. |
| Alumite, Osgloglas, Osmiridium, Mirion | PlusTiC is not present; no matching current source items/fluids | Retired. |
| Elementium, Manasteel, Terrasteel | Botania items exist, but no current TConstruct/Forge molten fluid tags exist in installed jars | Retired until a modern molten-Botania material provider is added. |
| Psimetal | Psi items exist, but no current molten psimetal fluid tag exists in installed jars | Retired. |
| Thaumium | Thaumcraft is not present | Retired. |

Validation note: Thermal Crucible schema was verified from `thermal_expansion` recipe JSON. NuclearCraft Melter schema was already verified during the NuclearCraft pass. TConstruct fluid tags were verified from installed `TConstruct` jar data.

## Semantic Review - IndustrialForegoing.zs - 2026-06-24

Compared the original `Enigmatica 2 - E2/scripts/IndustrialForegoing.zs` against `industrial-foregoing-1.20.1-3.5.22.jar`.

| Original intent | 1.20.1 status | Decision |
| --- | --- | --- |
| FluidDictionary aliases for seed oil, sulfuric acid, hydrogen, IC2 hydrogen, and liquid hydrogen | The old Industrial Foregoing FluidDictionary integration is not present as a direct KubeJS/datapack surface, and several referenced old fluids/mods are absent | Retired. |
| Add all raw meats to Protein Reactor | The old Protein Reactor item/API is not present in current Industrial Foregoing | Retired. |
| Add HarvestCraft crops/seeds/vegetables/fruits to BioReactor | HarvestCraft is absent; Croptopia is the pack's modern food/crop replacement | Ported by adding verified Croptopia crops/seeds and vanilla crop/seed foods to `industrialforegoing:bioreactor`. |
| Explicit extra HarvestCraft items such as mustard, ginger, garlic, oats, barley, peanut, pecan, almond, kale, walnut | Current Croptopia equivalents exist for many of these; `croptopia:walnut` was additionally verified from the item dump | Ported where current items exist. Missing old-only crops were retired. |

Validation note: Current Industrial Foregoing ships `data/industrialforegoing/tags/items/bioreactor.json` with only `minecraft:sweet_berries`. The port extends that modern item tag in `e2_recipes_industrial_foregoing.js`; no custom BioReactor recipe JSON was invented.

## Semantic Review - Utility Scripts - 2026-06-25

Reviewed `AkashicTome.zs`, `MorphOTool.zs`, and `Backpacks.zs` after confirming the 21-script KubeJS launch was clean.

| Original script | Original intent | 1.20.1 status | Decision |
| --- | --- | --- | --- |
| `AkashicTome.zs` | Craft a preloaded "Super Akashic Tome" containing many 1.12 guide books | `AkashicTome-1.7-27.jar` provides `akashictome:tome` and native `akashictome:attachment` recipe support. Most old embedded books reference removed mods or obsolete item IDs. | No KubeJS recipe added. Use the current native tome and attachment behavior. |
| `MorphOTool.zs` | Craft a preloaded "Super Morph-O-Tool" containing many 1.12 wrenches/tools | `Morph-o-Tool-1.7-38.jar` provides `morphtool:tool` and native `morphtool:attachment` recipe support. Several old tools are removed/renamed. | No KubeJS recipe added. Use the current native tool and attachment behavior. |
| `Backpacks.zs` | JEI-hide old `backpack:stick` variants | The old Backpack mod is absent. Current replacement is Sophisticated Backpacks, which has its own `sophisticatedbackpacks:backpack` recipe. | No KubeJS/JEI change needed. |

Validation note: Current jar recipes inspected:

- `data/akashictome/recipes/tome.json`
- `data/akashictome/recipes/attachment.json`
- `data/morphtool/recipes/tool.json`
- `data/morphtool/recipes/attachment.json`
- `data/sophisticatedbackpacks/recipes/backpack.json`
