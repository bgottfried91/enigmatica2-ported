# Config Porting Inventory

Generated from original E2 1.12 configs, Packwiz source configs, and the active 1.20.1 instance configs.

## Summary

- Original E2 config files: 921
- Active 1.20.1 instance config files: 700
- Packwiz source config files currently tracked: 602
- Packwiz source defaultconfigs files currently tracked: 29
- Original config families with likely current counterparts: 93
- Original config families for installed mods with no matching generated config: 13
- Original config families likely removed with missing mods: 118
- Original config families needing manual mapping: 3

## Immediate Finding

The Packwiz source now tracks a curated baseline of generated 1.20.1 configs. Remaining untracked counterparts are mostly client-only or user-preference configs that should be included only if the pack intentionally wants to manage those defaults. Forge server configs that apply to newly created worlds are tracked separately in defaultconfigs/.

## Likely Current Counterparts

| Original config family | Current config candidates | Notes |
|---|---|---|
| `actuallyadditions.cfg` | `actuallyadditions-common.toml` | tracked in Packwiz |
| `AdvGenerators/client.config (+4)` | `advgenerators-common.toml` | tracked in Packwiz |
| `akashictome.cfg` | `akashictome-common.toml` | tracked in Packwiz |
| `apotheosis/apotheosis.cfg (+8)` | `apotheosis/adventure.cfg`<br>`apotheosis/apotheosis.cfg`<br>`apotheosis/ench.cfg`<br>`apotheosis/enchantments.cfg`<br>`apotheosis/garden.cfg`<br>`apotheosis/names.cfg`<br>`apotheosis/potion.cfg`<br>`apotheosis/spawner.cfg`<br>... | tracked in Packwiz |
| `appleskin.cfg` | `appleskin-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `AppliedEnergistics2/AppliedEnergistics2.cfg (+5)` | `ae2/client.json`<br>`ae2/common.json` | tracked in Packwiz |
| `attributefix.cfg` | `attributeslib.cfg` | tracked in Packwiz |
| `badwithernocookiereloaded.cfg` | `bwncr-common.toml` | tracked in Packwiz |
| `baubles.cfg` | `curios-client.toml`<br>`curios-common.toml` | current instance has defaults; not tracked in Packwiz source |
| `bbm/AI_Improvements.cfg` | `aiimprovements-common.toml` | current instance has defaults; not tracked in Packwiz source |
| `betteradvancements/betteradvancements.cfg` | `betteradvancements-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `betterquesting/DefaultLoot.json (+3)` | `betterquesting/BetterQuesting_Client.json`<br>`betterquesting/BetterQuesting_Main.json`<br>`betterquesting/betterquesting_libs.init`<br>`betterquesting/data/loot_chests.xbt`<br>`betterquesting/data/settings.xbt` | tracked in Packwiz |
| `biomesoplenty/biome_ids.json (+107)` | `biomesoplenty/biome_toggles.json`<br>`biomesoplenty/gameplay.toml`<br>`biomesoplenty/generation.toml` | tracked in Packwiz |
| `bloodmagic/bloodmagic.cfg (+4)` | `bloodmagic-client.toml`<br>`bloodmagic-common.toml` | tracked in Packwiz |
| `botania.cfg` | `botania-client.toml`<br>`botania-common.toml` | tracked in Packwiz |
| `brandon3055/BrandonsCore.cfg (+173)` | `brandon3055/BrandonsCore.cfg`<br>`brandon3055/DraconicEvolution.cfg`<br>`brandon3055/ModuleStats.cfg`<br>`brandon3055/contributors.json`<br>`brandon3055/contributors.json.etag`<br>`brandon3055/hud_settings.json` | tracked in Packwiz |
| `Building Gadgets.cfg` | `buildinggadgets2-common.toml` | tracked in Packwiz |
| `carbonconfig.cfg` | `carbonconfig.cfg` | tracked in Packwiz |
| `carryon.cfg` | `carryon-client.toml`<br>`carryon-common.toml` | tracked in Packwiz |
| `chisel.cfg` | `chisel-common.toml` | tracked in Packwiz |
| `chiselsandbits.cfg` | `chiselsandbits-client.toml`<br>`chiselsandbits-common.toml` | tracked in Packwiz |
| `codechickenlib.cfg` | `ccl.cfg` | tracked in Packwiz |
| `cofh/core/client.cfg (+36)` | `cofh_core-client.toml`<br>`cofh_core-common.toml` | tracked in Packwiz |
| `colytra.cfg` | `colytra-server.toml` | tracked in Packwiz |
| `commoncapabilities.cfg` | `commoncapabilities-common.toml` | tracked in Packwiz |
| `compactmachines3/settings.cfg` | `compactmachines-common.toml` | tracked in Packwiz |
| `computercraft.cfg` | `computercraft-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `cookingforblockheads.cfg` | `cookingforblockheads-common.toml` | tracked in Packwiz |
| `cosmeticarmorreworked.cfg` | `cosmeticarmorreworked-client.toml`<br>`cosmeticarmorreworked-common.toml` | current instance has defaults; not tracked in Packwiz source |
| `ctm.cfg` | `ctm.toml` | current instance has defaults; not tracked in Packwiz source |
| `cyclicmagic.cfg` | `cyclic-client.toml`<br>`cyclic.toml` | tracked in Packwiz |
| `cyclic_ores.cfg` | `cyclic-client.toml`<br>`cyclic.toml` | tracked in Packwiz |
| `cyclopscore.cfg` | `cyclopscore-common.toml` | tracked in Packwiz |
| `defaultoptions/keybindings.txt (+3)` | `defaultoptions-common.toml`<br>`defaultoptions/keybindings.txt`<br>`defaultoptions/options.txt` | tracked in Packwiz |
| `ding.cfg` | `ding.toml` | current instance has defaults; not tracked in Packwiz source |
| `embers.cfg` | `embers-client.toml`<br>`embers-common.toml` | tracked in Packwiz |
| `enderio/enderio.cfg (+74)` | `enderio/armory-common.toml`<br>`enderio/base-client.toml`<br>`enderio/base-common.toml`<br>`enderio/machines-client.toml`<br>`enderio/machines-common.toml` | tracked in Packwiz |
| `enderstorage.cfg` | `EnderStorage.cfg` | tracked in Packwiz |
| `Extreme Reactors/Extreme Reactors.cfg` | `extremereactors/client.toml`<br>`extremereactors/common.toml` | tracked in Packwiz |
| `FarmingForBlockheads/Market.json (+1)` | `farmingforblockheads-common.toml`<br>`farmingforblockheads/MarketRegistry.json` | tracked in Packwiz |
| `fastbench.cfg` | `fastbench.cfg` | tracked in Packwiz |
| `forge.cfg` | `forge-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `fpsreducer/fpsreducer.cfg` | `fpsreducer/fpsreducer-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `immersiveengineering.cfg` | `immersiveengineering-client.toml`<br>`immersiveengineering-common.toml` | tracked in Packwiz |
| `immersivepetroleum.cfg` | `immersivepetroleum-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `immersivetech.cfg` | `immersivetechnology-client.toml`<br>`immersivetechnology-common.toml` | tracked in Packwiz |
| `incontrol/experience.json (+5)` | `incontrol/areas.json`<br>`incontrol/breakevents.json`<br>`incontrol/effects.json`<br>`incontrol/events.json`<br>`incontrol/experience.json`<br>`incontrol/leftclicks.json`<br>`incontrol/loot.json`<br>`incontrol/phases.json`<br>... | tracked in Packwiz |
| `industrialforegoing.cfg` | `industrialforegoing/machine-agriculture-husbandry.toml`<br>`industrialforegoing/machine-core.toml`<br>`industrialforegoing/machine-generator.toml`<br>`industrialforegoing/machine-misc.toml`<br>`industrialforegoing/machine-resource-production.toml` | tracked in Packwiz |
| `integrateddynamics.cfg` | `integrateddynamics-common.toml` | tracked in Packwiz |
| `integrateddynamicscompat.cfg` | `integrateddynamicscompat-common.toml` | tracked in Packwiz |
| `integratedtunnels.cfg` | `integratedtunnels-common.toml` | tracked in Packwiz |
| `integratedtunnelscompat.cfg` | `integratedtunnels-common.toml` | tracked in Packwiz |
| `JAOPCA.cfg` | `jaopca/custom_forms.json`<br>`jaopca/lang/en_us.json`<br>`jaopca/main.toml`<br>`jaopca/materials/alugentum.toml`<br>`jaopca/materials/aluminium.toml`<br>`jaopca/materials/aluminum.toml`<br>`jaopca/materials/amethyst.toml`<br>`jaopca/materials/amethyst_bronze.toml`<br>... | tracked in Packwiz |
| `jei/itemBlacklist.cfg (+3)` | `jei/blacklist.cfg`<br>`jei/ingredient-list-mod-sort-order.ini`<br>`jei/ingredient-list-type-sort-order.ini`<br>`jei/jei-client.ini`<br>`jei/jei-colors.ini`<br>`jei/jei-debug.ini`<br>`jei/jei-mod-id-format.ini`<br>`jei/recipe-category-sort-order.ini`<br>... | current instance has defaults; not tracked in Packwiz source |
| `jeresources/jeresources.cfg (+1)` | `jeresources-common.toml`<br>`jeresources.toml` | tracked in Packwiz |
| `kleeslabs.cfg` | `kleeslabs-common.toml` | tracked in Packwiz |
| `lostcities/general.cfg (+18)` | `lostcities/common.toml`<br>`lostcities/profiles/ancient.json`<br>`lostcities/profiles/atlantis.json`<br>`lostcities/profiles/bio_wasteland.json`<br>`lostcities/profiles/biosphere.json`<br>`lostcities/profiles/biosphere_caves.json`<br>`lostcities/profiles/cavern.json`<br>`lostcities/profiles/default.json`<br>... | tracked in Packwiz |
| `mcjtylib.cfg` | `mcjtylib-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `mctimmersivetechnology.cfg` | `immersivetechnology-client.toml`<br>`immersivetechnology-common.toml` | tracked in Packwiz |
| `mekanism/BoxBlacklist.txt (+1)` | `Mekanism/client.toml`<br>`Mekanism/common.toml`<br>`Mekanism/gear.toml`<br>`Mekanism/general.toml`<br>`Mekanism/generator-storage.toml`<br>`Mekanism/generators-gear.toml`<br>`Mekanism/generators.toml`<br>`Mekanism/machine-storage.toml`<br>... | tracked in Packwiz |
| `minecolonies.cfg` | `minecolonies-client.toml`<br>`minecolonies-common.toml` | tracked in Packwiz |
| `minecolonies_names.cfg` | `minecolonies-client.toml`<br>`minecolonies-common.toml` | tracked in Packwiz |
| `modularrouters.cfg` | `modularrouters-client.toml`<br>`modularrouters-common.toml` | tracked in Packwiz |
| `morphtool.cfg` | `morphtool-common.toml` | tracked in Packwiz |
| `naturescompass.cfg` | `naturescompass-client.toml`<br>`naturescompass-common.toml` | tracked in Packwiz |
| `neat.cfg` | `neat-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `nuclearcraft.cfg` | `NuclearCraft/accelerator.toml`<br>`NuclearCraft/accelerator_coolers/! README.TXT`<br>`NuclearCraft/accelerator_coolers/aluminum.json`<br>`NuclearCraft/accelerator_coolers/arsenic.json`<br>`NuclearCraft/accelerator_coolers/boron.json`<br>`NuclearCraft/accelerator_coolers/carobbiite.json`<br>`NuclearCraft/accelerator_coolers/copper.json`<br>`NuclearCraft/accelerator_coolers/cryotheum.json`<br>... | tracked in Packwiz |
| `oreexcavation.cfg` | `oreexcavation-client.toml`<br>`oreexcavation-common.toml`<br>`oreexcavation/block_groups.json`<br>`oreexcavation/shapes.json`<br>`oreexcavation/tool_overrides.json` | tracked in Packwiz |
| `oreexcavation_groups.json` | `oreexcavation-client.toml`<br>`oreexcavation-common.toml`<br>`oreexcavation/block_groups.json`<br>`oreexcavation/shapes.json`<br>`oreexcavation/tool_overrides.json` | tracked in Packwiz |
| `oreexcavation_overrides.json` | `oreexcavation-client.toml`<br>`oreexcavation-common.toml`<br>`oreexcavation/block_groups.json`<br>`oreexcavation/shapes.json`<br>`oreexcavation/tool_overrides.json` | tracked in Packwiz |
| `oreexcavation_shapes.json` | `oreexcavation-client.toml`<br>`oreexcavation-common.toml`<br>`oreexcavation/block_groups.json`<br>`oreexcavation/shapes.json`<br>`oreexcavation/tool_overrides.json` | tracked in Packwiz |
| `overpoweredarmorbar.cfg` | `overloadedarmorbar-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `patchouli.cfg` | `patchouli-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `pneumaticcraft/AmadronOffersPeriodic.cfg (+9)` | `pneumaticcraft-client.toml`<br>`pneumaticcraft-common.toml`<br>`pneumaticcraft/ArmorFeatureStatus.cfg`<br>`pneumaticcraft/MicromissileDefaults.cfg`<br>`pneumaticcraft/PneumaticArmorHUDLayout.cfg`<br>`pneumaticcraft/ProgrammingPuzzleBlacklist.cfg`<br>`pneumaticcraft/thirdparty.cfg` | tracked in Packwiz |
| `pregen/base.cfg (+1)` | `pregen/base.cfg`<br>`pregen/map-client.cfg`<br>`pregen/map-common.cfg`<br>`pregen/minimap.cfg` | current instance has defaults; not tracked in Packwiz source |
| `pregenerator/ClientConfig.cfg (+2)` | `pregen/base.cfg`<br>`pregen/map-client.cfg`<br>`pregen/map-common.cfg`<br>`pregen/minimap.cfg` | current instance has defaults; not tracked in Packwiz source |
| `prettybeaches.cfg` | `prettybeaches-common.toml` | tracked in Packwiz |
| `psi.cfg` | `psi-client.toml`<br>`psi-common.toml` | tracked in Packwiz |
| `quark.cfg` | `quark-common.toml` | tracked in Packwiz |
| `refinedstorage.cfg` | `refinedstorage-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `rftools/control.cfg (+4)` | `rftoolsdim-common.toml` | tracked in Packwiz |
| `scannable.cfg` | `scannable-client.toml`<br>`scannable-common.toml` | tracked in Packwiz |
| `solcarrot.cfg` | `solcarrot-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `storagedrawers.cfg` | `functionalstorage/functionalstorage-client.toml`<br>`functionalstorage/functionalstorage-common.toml` | tracked in Packwiz |
| `structurize.cfg` | `structurize-client.toml` | current instance has defaults; not tracked in Packwiz source |
| `tconstruct.cfg` | `tconstruct-client.toml`<br>`tconstruct-common.toml` | tracked in Packwiz |
| `TinkerToolLeveling.cfg` | `tleveling/common.toml`<br>`tleveling/modifiers.json` | tracked in Packwiz |
| `tips.cfg` | `tips.json` | current instance has defaults; not tracked in Packwiz source |
| `toastcontrol.cfg` | `toastcontrol-common.toml` | current instance has defaults; not tracked in Packwiz source |
| `torchmaster.cfg` | `torchmaster.toml` | tracked in Packwiz |
| `twilightforest.cfg` | `twilightforest-client.toml`<br>`twilightforest-common.toml` | tracked in Packwiz |
| `valkyrielib/main.cfg` | `valkyrielib/valkyrielib-client.json`<br>`valkyrielib/valkyrielib.json` | tracked in Packwiz |
| `xnet/xnet.cfg` | `xnet-client.toml` | current instance has defaults; not tracked in Packwiz source |

## Installed Mods With No Matching Generated Config

| Original config family | Current config candidates | Notes |
|---|---|---|
| `architect/blacklist.json (+2)` |  | mod appears installed, but the active instance did not generate a matching config family |
| `bookshelf.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `codechicken/supporters.json (+1)` |  | mod appears installed, but the active instance did not generate a matching config family |
| `darkutils.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `ElevatorMod/ElevatorMod.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `environmentalmaterials/main.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `fastfurnace.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `ironchest.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `journeymap_server.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `journeymap_ModInfo.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `notenoughwands.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `placebo.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |
| `refinedstorageaddons.cfg` |  | mod appears installed, but the active instance did not generate a matching config family |

## Likely Removed Mods

| Original config family | Current config candidates | Notes |
|---|---|---|
| `Additional Structures - General.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `Additional Structures - Structures.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `advRocketry/Centrifuge.xml (+14)` |  | source mod is not installed in the 1.20.1 pack |
| `AE2Stuff/readme.txt` |  | source mod is not installed in the 1.20.1 pack |
| `AE2WirelessTerminals.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `ancientwarfare/AncientWarfare.cfg (+10)` |  | source mod is not installed in the 1.20.1 pack |
| `animania.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `animania_farm.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `armoryexpansion/conarm/conarm-config.json (+9)` |  | source mod is not installed in the 1.20.1 pack |
| `astralsorcery/aevitas_ore_perk.cfg (+7)` |  | source mod is not installed in the 1.20.1 pack |
| `backpack.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `betterbuilderswands.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `bettercaves-1_12_2.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `betterfps.json` |  | source mod is not installed in the 1.20.1 pack |
| `bettermineshafts/1_12_2/README.txt (+3)` |  | source mod is not installed in the 1.20.1 pack |
| `bettermineshafts-1_12_2.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `bibliocraft.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `blockcraftery.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `bq_standard.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `comforts.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `conarm.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `craftingtweaks.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `custombackgrounds.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `CustomMainMenu/mainmenu.json` |  | source mod is not installed in the 1.20.1 pack |
| `DankNull.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `demagnetize.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `dirt2path.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `DiscordSuite.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `endercore/cropconfig.json (+1)` |  | source mod is not installed in the 1.20.1 pack |
| `engineersdoors.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `environmentaltech/main.cfg (+18)` |  | source mod is not installed in the 1.20.1 pack |
| `Exchangers.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `ExtraBitManipulation/armor_data.cfg (+5)` |  | source mod is not installed in the 1.20.1 pack |
| `extrautils2.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `fasterladderclimbing.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `flatcoloredblocks.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `foamfix.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `forestry/apiculture.cfg (+21)` |  | source mod is not installed in the 1.20.1 pack |
| `forgeChunkLoading.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `ftbbackups.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `ftblib.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `ftbutilities.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `funkylocomotion.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `gendustry/client.config (+1)` |  | source mod is not installed in the 1.20.1 pack |
| `gendustryjei.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `GeographiCraft/CCDimensions.cfg (+3)` |  | source mod is not installed in the 1.20.1 pack |
| `Guide-API/Guide-API.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `harvestcraft.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `harvestcraft_fruittree.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `horsetweaks.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `IC2.ini (+5)` |  | source mod is not installed in the 1.20.1 pack |
| `IntegrationForegoing.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `InvTweaks/InvTweaks.cfg (+3)` |  | source mod is not installed in the 1.20.1 pack |
| `InvTweaksRules.txt` |  | source mod is not installed in the 1.20.1 pack |
| `ironbackpacks/blacklist.json (+1)` |  | source mod is not installed in the 1.20.1 pack |
| `jeibees.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `jeivillagers.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `jepb.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `laser_drill_ores/actuallyadditions_ores.json (+10)` |  | source mod is not installed in the 1.20.1 pack |
| `librarianlib.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `libvulpes.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `lootcapacitortooltips.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `lunatriuscore.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `magicbees.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `malisiscore.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `malisisdoors.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `meecreeps.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `MemoryTester/Crash.txt (+5)` |  | source mod is not installed in the 1.20.1 pack |
| `MoreOverlays.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `MovingWorld/AssemblePriority.cfg (+1)` |  | source mod is not installed in the 1.20.1 pack |
| `multimob/modInformation/allBiomeTypes.txt (+10)` |  | source mod is not installed in the 1.20.1 pack |
| `mysticalworld.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `natura.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `NaturaModules.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `NoMobSpawningOnTrees.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `nutrition/effects/example.json (+17)` |  | source mod is not installed in the 1.20.1 pack |
| `oldjavawarning.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `openblocks.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `opencomputers/default.recipes (+5)` |  | source mod is not installed in the 1.20.1 pack |
| `openmods.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `OpenModsLibCore.json` |  | source mod is not installed in the 1.20.1 pack |
| `OreDictInit.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `p455w0rdsLib.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `phosphor.json` |  | source mod is not installed in the 1.20.1 pack |
| `playersdropheads.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `plustic.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `primitivemobs/primitivemobs.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `quickleafdecay.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `randompatches.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `reccomplex.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `refinedstoragerequestify.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `roots/crops.cfg (+9)` |  | source mod is not installed in the 1.20.1 pack |
| `rustic.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `schematica.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `shadowfacts/ExtraRails.cfg (+1)` |  | source mod is not installed in the 1.20.1 pack |
| `spiceoflife/example-food-group.json` |  | source mod is not installed in the 1.20.1 pack |
| `splash.properties` |  | source mod is not installed in the 1.20.1 pack |
| `stg.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `supersoundmuffler.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `teamreborn/configData.nbt (+6)` |  | source mod is not installed in the 1.20.1 pack |
| `teslacorelib.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `thaumcraft_graphics.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `thaumcraft_misc.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `thaumcraft_world.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `thaumicjei.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `thaumicjei_itemstack_aspects.json` |  | source mod is not installed in the 1.20.1 pack |
| `thaumictinkerer.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `TinkerModules.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `tombmanygraves.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `torohealthmod.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `toughnessbar.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `unidict/IntegrationModule.cfg (+2)` |  | source mod is not installed in the 1.20.1 pack |
| `unlimitedchiselworks.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `unloader.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `waila/theme/dark.json (+2)` |  | source mod is not installed in the 1.20.1 pack |
| `wawla.cfg` |  | source mod is not installed in the 1.20.1 pack |
| `wizardry/fire_recipes/devil_dust.json (+60)` |  | source mod is not installed in the 1.20.1 pack |
| `ynot.cfg` |  | source mod is not installed in the 1.20.1 pack |

## Needs Manual Mapping

| Original config family | Current config candidates | Notes |
|---|---|---|
| `acronym/base/General.cfg` |  | no obvious current config by name; needs manual mod mapping |
| `chiselsandbits_clipboard.cfg` |  | no obvious current config by name; needs manual mod mapping |
| `fw.cfg` |  | no obvious current config by name; needs manual mod mapping |

## Current-Only Config Families

These are generated by mods in the 1.20.1 pack without an obvious 1.12 config family match.

- `arsnouveau`: `ars_nouveau/burst.toml`, `ars_nouveau/glyph_accelerate.toml`, `ars_nouveau/glyph_amplify.toml`, `ars_nouveau/glyph_animate_block.toml`, `ars_nouveau/glyph_aoe.toml` ...
- `croptopia`: `croptopia/croptopia_v3.conf`
- `endercrop`: `endercrop-common.toml`
- `flib`: `flib.toml`
- `flywheel`: `flywheel-client.toml`
- `fml`: `fml.toml`
- `guideme`: `guideme.toml`
- `ichunutil`: `ichunutil/ichunutil-client.toml`, `ichunutil/themes/aztec.json`, `ichunutil/themes/blue&black.json`, `ichunutil/themes/blue&orange.json`, `ichunutil/themes/default.json` ...
- `immersiveconvergence`: `immersiveconvergence-common.toml`
- `ironfurnaces`: `ironfurnaces-client.toml`, `ironfurnaces.toml`
- `jade`: `jade/hide-blocks.json`, `jade/hide-entities.json`, `jade/jade.json`, `jade/plugins.json`, `jade/sort-order.json`
- `leavesbegone`: `leavesbegone-server.toml`
- `mantle`: `mantle-client.toml`
- `mousetweaks`: `MouseTweaks.cfg`
- `nonvflash`: `no_nv_flash-client.toml`
- `ponder`: `ponder-client.toml`
- `powah`: `powah.json5`
- `sophisticatedbackpacks`: `sophisticatedbackpacks-common.toml`
- `sophisticatedcore`: `sophisticatedcore-client.toml`, `sophisticatedcore-common.toml`
- `terrablender`: `terrablender.toml`
- `thermal`: `thermal-client.toml`, `thermal-common.toml`
- `titanium`: `titanium/titanium-tags.toml`, `titanium/titanium.toml`
- `tombstone`: `tombstone/loottables/tombstone-pool-abandoned_grave.json`, `tombstone/loottables/tombstone-pool-archaeology.json`, `tombstone/loottables/tombstone-pool-cat_morning.json`, `tombstone/loottables/tombstone-pool-chest_treasure.json`, `tombstone/loottables/tombstone-pool-lost_treasure.json` ...
- `zeta`: `zeta-common.toml`
