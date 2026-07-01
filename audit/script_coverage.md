# Script Port Coverage Checklist

Counts are regex-based indicators for review, not proof of correctness.

| Original script | ZS lines | ZS operations | Candidate KubeJS | JS lines | JS operations | Review note |
|---|---:|---|---|---:|---|---|
| `ActuallyAdditions.zs` | 73 | crafting_add:3, machine_recipe:19 | `e2_recipes_actually_additions.js` | 62 | crafting_add:3, custom_machine:2 | review mapped port |
| `AdvancedGenerators.zs` | 12 | crafting_add:1 | `e2_recipes_advanced_generators.js` | 14 | crafting_add:1, crafting_remove:1 | review mapped port |
| `AdvancedRocketry.zs` | 7 | crafting_add:1 |  | 0 | none | no obvious KubeJS match |
| `AkashicTome.zs` | 29 | crafting_add:1 |  | 0 | none | no obvious KubeJS match |
| `AppliedEnergistics.zs` | 27 | crafting_add:1, crafting_remove:1, machine_recipe:1 | `e2_recipes_applied_energistics.js` | 58 | custom_machine:6 | review mapped port |
| `Backpacks.zs` | 11 | jei_hide:2 |  | 0 | none | no obvious KubeJS match |
| `Bibliocraft.zs` | 27 | crafting_add:8, crafting_remove:1 |  | 0 | none | no obvious KubeJS match |
| `BinniesMod.zs` | 5 | crafting_add:1, machine_recipe:1 |  | 0 | none | no obvious KubeJS match |
| `BiomesOPlenty.zs` | 19 | crafting_add:3, jei_hide:1, machine_recipe:3 | `e2_recipes_biomesoplenty.js` | 18 | none | review mapped port |
| `Chisel.zs` | 32 | none | `e2_recipes_chisel.js` | 17 | none | review mapped port |
| `ChiselsAndBits.zs` | 2 | none |  | 0 | none | no obvious KubeJS match |
| `Cyclic.zs` | 9 | crafting_add:1, crafting_remove:2, jei_hide:1, property_change:1 | `e2_recipes_cyclic.js`, `e2_item_properties.js` | 56 | crafting_add:1, crafting_remove:1, property_change:3 | review mapped port |
| `Embers.zs` | 56 | jei_hide:40 | `e2_recipes_embers.js` | 12 | none | review mapped port |
| `ExtraUtilities2.zs` | 46 | crafting_add:2, crafting_remove:3 |  | 0 | none | no obvious KubeJS match |
| `FluidCompatibility.zs` | 73 | none | `e2_recipes_fluid_compatibility.js` | 71 | custom_machine:2 | review mapped port |
| `Furnace.zs` | 18 | furnace:2 | `e2_recipes_furnace.js` | 27 | crafting_remove:1, furnace:1 | review mapped port |
| `Harvestcraft.zs` | 9 | machine_recipe:2 | `e2_recipes_harvestcraft.js` | 9 | none | review mapped port |
| `ImmersiveEngineering.zs` | 28 | crafting_add:2, crafting_remove:2, machine_recipe:1 | `e2_recipes_immersive_engineering.js` | 75 | crafting_add:4, crafting_remove:3, custom_machine:1 | review mapped port |
| `IndustrialCraft2.zs` | 63 | crafting_add:2 |  | 0 | none | no obvious KubeJS match |
| `IndustrialForegoing.zs` | 63 | none | `e2_recipes_industrial_foregoing.js` | 53 | tags:2 | review mapped port |
| `IntegratedDynamics.zs` | 9 | machine_recipe:4 | `e2_recipes_integrated_dynamics.js` | 14 | none | review mapped port |
| `JEICategories.zs` | 359 | none |  | 0 | none | no obvious KubeJS match |
| `Mekanism.zs` | 74 | crafting_add:2, crafting_remove:2, jei_hide:18, machine_recipe:6, property_change:8 | `e2_recipes_mekanism.js`, `e2_item_properties.js` | 123 | crafting_add:2, crafting_remove:22, custom_machine:2, property_change:3 | review mapped port |
| `MekanismBgott.zs` | 7 | machine_recipe:2 |  | 0 | none | no obvious KubeJS match |
| `MiscRecipes.zs` | 256 | crafting_add:63, crafting_remove:9, jei_hide:27, oredict_add:2, machine_recipe:6 | `e2_recipes_misc.js` | 276 | crafting_add:28, crafting_remove:7 | review mapped port |
| `MorphOTool.zs` | 29 | crafting_add:1 |  | 0 | none | no obvious KubeJS match |
| `NuclearCraft.zs` | 74 | jei_hide:38, machine_recipe:12 | `e2_recipes_nuclearcraft.js` | 83 | crafting_remove:4, custom_machine:3 | review mapped port |
| `OreDict.zs` | 267 | jei_hide:2, oredict_add:44, oredict_remove:25 | `e2_tags_oredict.js`, `e2_tags_oredict_atm_complete.js` | 356 | crafting_add:5, tags:188 | review mapped port |
| `OreDictATM.zs` | 509 | crafting_add:5 | `e2_tags_oredict_atm_complete.js` | 284 | crafting_add:5, tags:172 | review mapped port |
| `PlankWoodFix.zs` | 17 | crafting_add:1, oredict_remove:1 |  | 0 | none | no obvious KubeJS match |
| `Plates.zs` | 186 | crafting_add:47, jei_hide:18, machine_recipe:35 | `e2_recipes_plates.js` | 122 | crafting_add:1, crafting_remove:5, custom_machine:2 | review mapped port |
| `RecipeConflicts.zs` | 210 | crafting_add:21, crafting_remove:52 | `e2_recipes_conflicts.js` | 81 | crafting_add:7, crafting_remove:7 | review mapped port |
| `Smeltables&Burnables.zs` | 13 | furnace:5 |  | 0 | none | no obvious KubeJS match |
| `TempRecipes.zs` | 29 | none |  | 0 | none | no obvious KubeJS match |
| `Thaumcraft.zs` | 46 | none |  | 0 | none | no obvious KubeJS match |
| `ThermalExpansion.zs` | 76 | machine_recipe:24 | `e2_recipes_thermal_bottler.js`, `e2_recipes_thermal_dynamo_fuels.js` | 76 | crafting_remove:1, custom_machine:4 | review mapped port |
| `TinkersConstruct.zs` | 40 | jei_hide:1, machine_recipe:2 | `e2_recipes_tinkers_construct.js` | 66 | custom_machine:2 | review mapped port |
| `Tooltips.zs` | 70 | none | `e2_tooltips.js` | 17 | tags:2, tooltip:1 | review mapped port |
| `extrabees.zs` | 14 | crafting_add:6 |  | 0 | none | no obvious KubeJS match |
