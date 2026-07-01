# Building Reactor Config Port Notes

Generated comparison notes for config value porting.

## Extreme Reactors/Extreme Reactors.cfg -> extremereactors/common.toml

- Parsed old scalar values: 44
- Parsed new scalar values: 31
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 44
- New-only scalar keys: 31

Old-only keys sample:
- `client.disableReactorFuelRodRender` = `false`
- `client.disableReactorParticles` = `false`
- `client.disableTurbineParticles` = `false`
- `client.disableTurbineRotorRender` = `false`
- `compatibility.autoAddUranium` = `true`
- `compatibility.enableMetallurgyFantasyMetalsInTurbines` = `true`
- `general.enableComedy` = `true`
- `general.fuelUsageMultiplier` = `3.0`
- `general.powerProductionMultiplier` = `1.0`
- `general.ticksPerRedstoneUpdate` = `20`
- `reactor.maxReactorHeight` = `48`
- `reactor.maxReactorSize` = `32`
- `reactor.reactorPowerProductionMultiplier` = `0.5`
- `recipes.enableCyaniteFromYelloriumRecipe` = `true`
- `recipes.enableReactorPowerTapRecipe` = `true`
- `recipes.registerCharcoalForSmelting` = `true`
- `recipes.registerCoalForSmelting` = `true`
- `recipes.registerCreativeMultiblockParts` = `true`
- `recipes.registerGraphiteCharcoalCraftingRecipes` = `false`
- `recipes.registerGraphiteCoalCraftingRecipes` = `false`
- `recipes.registerYelloriteSmeltToUranium` = `true`
- `recipes.registerYelloriumAsUranium` = `true`
- `recipes.requireObsidianGlass` = `false`
- `turbine.maxTurbineHeight` = `32`
- `turbine.maxTurbineSize` = `16`
- `turbine.turbineAeroDragMultiplier` = `1.0`
- `turbine.turbineCoilDragMultiplier` = `1.0`
- `turbine.turbineFluidPerBladeMultiplier` = `1.0`
- `turbine.turbineMassDragMultiplier` = `1.0`
- `turbine.turbinePowerProductionMultiplier` = `1.0`
- `worldgen.anglesiteOreEnableWorldGen` = `false`
- `worldgen.anglesiteOreMaxClustersPerChunk` = `1`
- `worldgen.anglesiteOrePerCluster` = `4`
- `worldgen.benitoiteOreEnableWorldGen` = `false`
- `worldgen.benitoiteOreMaxClustersPerChunk` = `2`
- `worldgen.benitoiteOrePerCluster` = `5`
- `worldgen.enableWorldGen` = `false`
- `worldgen.enableWorldRegeneration` = `false`
- `worldgen.useBlacklist` = `false`
- `worldgen.userWorldGenVersion` = `0`
- `worldgen.yelloriteOreEnableWorldGen` = `false`
- `worldgen.yelloriteOreMaxClustersPerChunk` = `2`
- `worldgen.yelloriteOreMaxY` = `32`
- `worldgen.yelloriteOrePerCluster` = `5`

New-only keys sample:
- `common.energizer.maxEnergizerHeight` = `32`
- `common.energizer.maxEnergizerSize` = `32`
- `common.fluidizer.energyPerRecipeTick` = `25`
- `common.fluidizer.maxFluidizerHeight` = `16`
- `common.fluidizer.maxFluidizerSize` = `16`
- `common.general.fuelUsageMultiplier` = `1.0`
- `common.general.powerProductionMultiplier` = `1.0`
- `common.general.ticksPerRedstoneUpdate` = `20`
- `common.reactor.maxReactorHeight` = `48`
- `common.reactor.maxReactorSize` = `32`
- `common.reactor.reactorPowerProductionMultiplier` = `1.0`
- `common.turbine.maxTurbineHeight` = `32`
- `common.turbine.maxTurbineSize` = `32`
- `common.turbine.turbineAeroDragMultiplier` = `1.0`
- `common.turbine.turbineCoilDragMultiplier` = `1.0`
- `common.turbine.turbineFluidPerBladeMultiplier` = `1.0`
- `common.turbine.turbineMassDragMultiplier` = `1.0`
- `common.turbine.turbinePowerProductionMultiplier` = `1.0`
- `common.worldgen.anglesiteOreEnableWorldGen` = `true`
- `common.worldgen.anglesiteOreMaxClustersPerChunk` = `2`
- `common.worldgen.anglesiteOrePerCluster` = `5`
- `common.worldgen.benitoiteOreEnableWorldGen` = `true`
- `common.worldgen.benitoiteOreMaxClustersPerChunk` = `2`
- `common.worldgen.benitoiteOrePerCluster` = `5`
- `common.worldgen.enableWorldGen` = `true`
- `common.worldgen.enableWorldRegeneration` = `false`
- `common.worldgen.userWorldGenVersion` = `1`
- `common.worldgen.yelloriteOreEnableWorldGen` = `true`
- `common.worldgen.yelloriteOreMaxClustersPerChunk` = `3`
- `common.worldgen.yelloriteOreMaxY` = `32`
- `common.worldgen.yelloriteOrePerCluster` = `5`

### Ported Values

- `common.general.fuelUsageMultiplier`: `1.0` -> `3.0`
- `common.reactor.reactorPowerProductionMultiplier`: `1.0` -> `0.5`
- `common.turbine.maxTurbineSize`: `32` -> `16`
- Disabled native Extreme Reactors ore generation:
  - `enableWorldGen`: `true` -> `false`
  - `yelloriteOreEnableWorldGen`: `true` -> `false`
  - `anglesiteOreEnableWorldGen`: `true` -> `false`
  - `benitoiteOreEnableWorldGen`: `true` -> `false`
- Ported old exposed ore-generation scalar values that still exist:
  - `userWorldGenVersion`: `1` -> `0`
  - `yelloriteOreMaxClustersPerChunk`: `3` -> `2`
  - `anglesiteOreMaxClustersPerChunk`: `2` -> `1`
  - `anglesiteOrePerCluster`: `5` -> `4`

Reason: old E2 disabled Extreme Reactors native ore generation and used centralized ore/worldgen handling. Reactor/turbine values preserve old E2 balance where the same config concepts still exist.

## carryon.cfg -> carryon-common.toml

- Parsed old scalar values: 23
- Parsed new scalar values: 31
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 23
- New-only scalar keys: 31

Old-only keys sample:
- `general.settings.allowBabies` = `false`
- `general.settings.blockSlownessMultiplier` = `1.0`
- `general.settings.dropCarriedWhenHit` = `false`
- `general.settings.entitySizeMattersStacking` = `true`
- `general.settings.entitySlownessMultiplier` = `1.0`
- `general.settings.facePlayer` = `false`
- `general.settings.heavyEntities` = `true`
- `general.settings.heavyTiles` = `true`
- `general.settings.hitWhileCarrying` = `false`
- `general.settings.maxDistance` = `2.5`
- `general.settings.maxEntityHeight` = `1.5`
- `general.settings.maxEntityStackLimit` = `10`
- `general.settings.maxEntityWidth` = `1.5`
- `general.settings.pickupAllBlocks` = `false`
- `general.settings.pickupHostileMobs` = `false`
- `general.settings.renderArms` = `true`
- `general.settings.slownessInCreative` = `true`
- `general.settings.stackableEntities` = `true`
- `general.settings.tamedHostileMobExemption` = `true`
- `general.settings.useScripts` = `false`
- `general.settings.useWhitelistBlocks` = `false`
- `general.settings.useWhitelistEntities` = `false`
- `general.settings.useWhitelistStacking` = `false`

New-only keys sample:
- `blacklist.forbiddenEntities` = `["minecraft:end_crystal", "minecraft:ender_dragon", "minecraft:ghast", "minecraft:shulker", "minecraft:leash_knot", "minecraft:armor_stand", "minecraft:item_frame", "minecraft:painting", "minecraft:shulker_bullet", "animania:hamster", "animania:ferret*", "animania:hedgehog*", "animania:cart", "animania:wagon", "mynko:*", "pixelmon:*", "mocreatures:*", "quark:totem", "vehicle:*", "securitycraft:*", "taterzens:npc", "easy_npc:*", "bodiesbodies:dead_body"]`
- `blacklist.forbiddenStacking` = `["minecraft:horse"]`
- `blacklist.forbiddenTiles` = `["#forge:immovable", "#forge:relocation_not_supported", "minecraft:end_portal", "minecraft:piston_head", "minecraft:end_gateway", "minecraft:tall_grass", "minecraft:large_fern", "minecraft:peony", "minecraft:rose_bush", "minecraft:lilac", "minecraft:sunflower", "minecraft:*_bed", "minecraft:*_door", "minecraft:big_dripleaf_stem", "minecraft:waterlily", "minecraft:cake", "minecraft:nether_portal", "minecraft:tall_seagrass", "animania:block_trough", "animania:block_invisiblock", "colossalchests:*", "ic2:*", "bigreactors:*", "forestry:*", "tconstruct:*", "rustic:*", "botania:*", "astralsorcery:*", "quark:colored_bed_*", "immersiveengineering:*", "embers:block_furnace", "embers:ember_bore", "embers:ember_activator", "embers:mixer", "embers:heat_coil", "embers:large_tank", "embers:crystal_cell", "embers:alchemy_pedestal", "embers:boiler", "embers:combustor", "embers:catalzyer", "embers:field_chart", "embers:inferno_forge", "storagedrawers:framingtable", "skyresources:*", "lootbags:*", "exsartagine:*", "aquamunda:tank", "opencomputers:*", "malisisdoors:*", "industrialforegoing:*", "minecolonies:*", "thaumcraft:pillar*", "thaumcraft:infernal_furnace", "thaumcraft:placeholder*", "thaumcraft:infusion_matrix", "thaumcraft:golem_builder", "thaumcraft:thaumatorium*", "magneticraft:oil_heater", "magneticraft:solar_panel", "magneticraft:steam_engine", "magneticraft:shelving_unit", "magneticraft:grinder", "magneticraft:sieve", "magneticraft:solar_tower", "magneticraft:solar_mirror", "magneticraft:container", "magneticraft:pumpjack", "magneticraft:solar_panel", "magneticraft:refinery", "magneticraft:oil_heater", "magneticraft:hydraulic_press", "magneticraft:multiblock_gap", "refinedstorage:*", "mcmultipart:*", "enderstorage:*", "betterstorage:*", "practicallogistics2:*", "wearablebackpacks:*", "rftools:screen", "rftools:creative_screen", "create:*", "magic_doorknob:*", "iceandfire:*", "ftbquests:*", "waystones:*", "contact:*", "framedblocks:*", "securitycraft:*", "forgemultipartcbe:*", "integrateddynamics:cable", "mekanismgenerators:wind_generator", "cookingforblockheads:cabinet", "cookingforblockheads:corner", "cookingforblockheads:counter", "cookingforblockheads:oven", "cookingforblockheads:toaster", "cookingforblockheads:milk_jar", "cookingforblockheads:cow_jar", "cookingforblockheads:fruit_basket", "cookingforblockheads:cooking_table", "cookingforblockheads:fridge", "cookingforblockheads:sink", "powah:*", "advancementtrophies:trophy", "mekanismgenerators:heat_generator", "mna:filler_block"]`
- `customPickupConditions.customPickupConditionsBlocks` = `[]`
- `customPickupConditions.customPickupConditionsEntities` = `[]`
- `settings.allowBabies` = `false`
- `settings.blockSlownessMultiplier` = `1.0`
- `settings.dropCarriedWhenHit` = `false`
- `settings.entitySizeMattersStacking` = `true`
- `settings.entitySlownessMultiplier` = `1.0`
- `settings.heavyEntities` = `true`
- `settings.heavyTiles` = `true`
- `settings.hitWhileCarrying` = `false`
- `settings.maxDistance` = `2.5`
- `settings.maxEntityHeight` = `2.5`
- `settings.maxEntityStackLimit` = `10`
- `settings.maxEntityWidth` = `1.5`
- `settings.pickupAllBlocks` = `false`
- `settings.pickupHostileMobs` = `false`
- `settings.pickupPlayers` = `true`
- `settings.pickupUnbreakableBlocks` = `false`
- `settings.placementStateExceptions` = `["minecraft:chest[type]", "minecraft:stone_button[face]", "minecraft:vine[north,east,south,west,up]", "minecraft:creeper_head[rotation]", "minecraft:glow_lichen[north,east,south,west,up,down]", "minecraft:oak_sign[rotation]", "minecraft:oak_trapdoor[half]"]`
- `settings.slownessInCreative` = `true`
- `settings.stackableEntities` = `true`
- `settings.useScripts` = `false`
- `settings.useWhitelistBlocks` = `false`
- `settings.useWhitelistEntities` = `false`
- `settings.useWhitelistStacking` = `false`
- `whitelist.allowedBlocks` = `[]`
- `whitelist.allowedEntities` = `[]`
- `whitelist.allowedStacking` = `[]`

### Ported Values

- `settings.maxEntityHeight`: `2.5` -> `1.5`
  - Direct mapping from old E2 `maxEntityHeight = 1.5`.
  - Other old Carry On settings already matched current values or were current-only safety lists.

## chisel.cfg -> chisel-common.toml

- Parsed old scalar values: 122
- Parsed new scalar values: 35
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 122
- New-only scalar keys: 35

Old-only keys sample:
- `autochisel.autoChiselNeedsPower` = `false`
- `autochisel.autoChiselTakesPower` = `true`
- `block.getRoadLineTool` = `pickaxe`
- `block.roadLineToolLevel` = `0`
- `block.useRoadLineTool` = `false`
- `chisel.allowChiselCrossColors` = `true`
- `chisel.allowChiselDamage` = `true`
- `chisel.diamondChiselAttackDamage` = `3`
- `chisel.diamondChiselMaxDamage` = `5000`
- `chisel.hitechChiselAttackDamage` = `3`
- `chisel.hitechChiselMaxDamage` = `10000`
- `chisel.ironChiselAttackDamage` = `2`
- `chisel.ironChiselCanLeftClick` = `true`
- `chisel.ironChiselHasModes` = `false`
- `chisel.ironChiselMaxDamage` = `500`
- `client.imTooGoodForBlockDescriptions` = `false`
- `client.pillarOldGraphics` = `false`
- `client.tooltipsUseBlockDescriptions` = `true`
- `features.aluminum` = `true`
- `features.andesite` = `true`
- `features.antiblock` = `true`
- `features.arcaneStone` = `true`
- `features.autochisel` = `true`
- `features.basalt` = `true`
- `features.bloodMagic` = `true`
- `features.bookshelf` = `true`
- `features.bricks` = `true`
- `features.bronze` = `true`
- `features.brownstone` = `true`
- `features.carpet` = `true`
- `features.certus` = `true`
- `features.charcoal` = `true`
- `features.chisel` = `true`
- `features.cloud` = `true`
- `features.coal` = `true`
- `features.coalCoke` = `true`
- `features.cobalt` = `true`
- `features.cobblestone` = `true`
- `features.cobblestonemossy` = `true`
- `features.concrete` = `true`
- `features.copper` = `true`
- `features.diamond` = `true`
- `features.diorite` = `true`
- `features.dirt` = `true`
- `features.electrum` = `true`
- `features.emerald` = `true`
- `features.endPurpur` = `true`
- `features.endstone` = `true`
- `features.factory` = `true`
- `features.futura` = `true`

New-only keys sample:
- `allowChiselDamage` = `true`
- `autoChiselNeedsPower` = `false`
- `autoChiselPowered` = `true`
- `carvingCooldownTicks` = `4`
- `concreteVelocityMult` = `1.35`
- `diamondChiselAttackDamage` = `3`
- `diamondChiselMaxDamage` = `5056`
- `enableUltimineCompat` = `true`
- `hitechChiselAttackDamage` = `3`
- `hitechChiselMaxDamage` = `10048`
- `ironChiselAttackDamage` = `2`
- `ironChiselCanLeftClick` = `false`
- `ironChiselHasModes` = `false`
- `ironChiselMaxDamage` = `512`
- `ultimineGroupVariants` = `true`
- `worldgen.basalt.enabled` = `false`
- `worldgen.basalt.maxY` = `0`
- `worldgen.basalt.minY` = `-64`
- `worldgen.basalt.veinCount` = `1`
- `worldgen.basalt.veinSize` = `48`
- `worldgen.diabase.enabled` = `true`
- `worldgen.diabase.maxY` = `0`
- `worldgen.diabase.minY` = `-64`
- `worldgen.diabase.veinCount` = `1`
- `worldgen.diabase.veinSize` = `48`
- `worldgen.limestone.enabled` = `false`
- `worldgen.limestone.maxY` = `60`
- `worldgen.limestone.minY` = `0`
- `worldgen.limestone.veinCount` = `1`
- `worldgen.limestone.veinSize` = `48`
- `worldgen.marble.enabled` = `false`
- `worldgen.marble.maxY` = `60`
- `worldgen.marble.minY` = `0`
- `worldgen.marble.veinCount` = `1`
- `worldgen.marble.veinSize` = `48`

### Ported Values

- `ironChiselMaxDamage`: `512` -> `500`
- `diamondChiselMaxDamage`: `5056` -> `5000`
- `hitechChiselMaxDamage`: `10048` -> `10000`
- `ironChiselCanLeftClick`: `false` -> `true`

Chisel marble/limestone/basalt generation was already disabled in the current config and handled by the existing worldgen/datapack pass.

## chiselsandbits.cfg -> chiselsandbits-common.toml

- Parsed old scalar values: 530
- Parsed new scalar values: 4
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 530
- New-only scalar keys: 4

Old-only keys sample:
- `"balance settings".bagStackSize` = `4096`
- `"balance settings".bitLightPercentage` = `6.25`
- `"balance settings".blacklistTickingBlocks` = `true`
- `"balance settings".compatabilityMode` = `true`
- `"balance settings".damageTools` = `true`
- `"balance settings".diamondChiselUses` = `796480`
- `"balance settings".diamondSawUses` = `7980`
- `"balance settings".enableBitLightSource` = `true`
- `"balance settings".enableChiselToolHarvestCheck` = `true`
- `"balance settings".enableChiselToolHarvestCheckTools` = `pickaxe,axe,shovel`
- `"balance settings".enableSetBitCommand` = `false`
- `"balance settings".enableToolHarvestLevels` = `true`
- `"balance settings".fullBlockCrafting` = `true`
- `"balance settings".goldChiselUses` = `1024`
- `"balance settings".ironChiselUses` = `293440`
- `"balance settings".maxDrawnRegionSize` = `4.0`
- `"balance settings".requireBagSpace` = `false`
- `"balance settings".stoneChiselUses` = `8384`
- `"balance settings".voidExcessBits` = `false`
- `"balance settings".wrenchUses` = `1888`
- `"client performance settings".defaultToDynamicRenderer` = `false`
- `"client performance settings".dynamicMaxConcurrentTessalators` = `32`
- `"client performance settings".dynamicModelFaceCount` = `40`
- `"client performance settings".dynamicModelMinimizeLatancy` = `true`
- `"client performance settings".dynamicModelRange` = `128`
- `"client performance settings".dynamicRenderFullChunksOnly` = `true`
- `"client performance settings".forceDynamicRenderer` = `false`
- `"client performance settings".maxMillisecondsPerBlock` = `10`
- `"client performance settings".maxMillisecondsUploadingPerFrame` = `15`
- `"client performance settings".minimizeLatancyMaxTime` = `100`
- `"client performance settings".useVBO` = `AUTOMATIC`
- `"client settings".addBrokenBlocksToCreativeClipboard` = `true`
- `"client settings".chatModeNotification` = `false`
- `"client settings".creativeClipboardSize` = `32`
- `"client settings".displayMeasuringTapeInChat` = `false`
- `"client settings".enableChiselMode_ConnectedMaterial` = `true`
- `"client settings".enableChiselMode_ConnectedPlane` = `true`
- `"client settings".enableChiselMode_DrawnRegion` = `true`
- `"client settings".enableChiselMode_LargeCube` = `true`
- `"client settings".enableChiselMode_Line` = `true`
- `"client settings".enableChiselMode_MediumCube` = `true`
- `"client settings".enableChiselMode_Plane` = `true`
- `"client settings".enableChiselMode_SameMaterial` = `true`
- `"client settings".enableChiselMode_SmallCube` = `true`
- `"client settings".enableChiselMode_Snap2` = `true`
- `"client settings".enableChiselMode_Snap4` = `true`
- `"client settings".enableChiselMode_Snap8` = `true`
- `"client settings".enablePositivePatternMode_Additive` = `true`
- `"client settings".enablePositivePatternMode_Impose` = `true`
- `"client settings".enablePositivePatternMode_Placement` = `true`

New-only keys sample:
- `help.enabled-in-tooltips` = `true`
- `performance.caches.sizes.class-metadata` = `10000`
- `performance.caches.sizes.collision-boxes` = `10000`
- `performance.saving.thread-count` = `6`

## psi.cfg -> psi-common.toml

- Parsed old scalar values: 10
- Parsed new scalar values: 3
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 10
- New-only scalar keys: 3

Old-only keys sample:
- `general.CAD Harvest Level` = `2`
- `general.Client Side Magical Psi` = `false`
- `general.Context Sensitive Bar` = `true`
- `general.Maximum Psi Bar Scale` = `3`
- `general.Psi Bar on the Right` = `true`
- `general.Spell Cache Size` = `100`
- `general.Use Persistent Data` = `true`
- `general.Use Shaders` = `true`
- `general.Use Vanilla Particle Limiter` = `true`
- `general.Version Checking` = `false`

New-only keys sample:
- `common.cadHarvestLevel` = `3`
- `common.magiPsiClientSide` = `false`
- `common.spellCacheSize` = `200`

### Ported Values

- `common.cadHarvestLevel`: `3` -> `2`
- `common.spellCacheSize`: `200` -> `100`

Both are direct mappings from old E2 `CAD Harvest Level` and `Spell Cache Size`. `magiPsiClientSide` already matched old E2's server-side behavior.
