# Utility Config Port Notes

Generated comparison notes for config value porting.

## integrateddynamics.cfg -> integrateddynamics-common.toml

- Parsed old scalar values: 106
- Parsed new scalar values: 79
- Same key/value pairs: 0
- Same key but changed value/type: 57
- Old-only scalar keys: 49
- New-only scalar keys: 22

Changed same-name keys:
- `core.general.analytics`: old `B=true` -> new `==true`
- `core.general.cacheCableModels`: old `B=true` -> new `==true`
- `core.general.energyRateLimit`: old `I=2147483647` -> new `==2147483647`
- `core.general.ingredientNetworkObserverEnableMultithreading`: old `B=true` -> new `==true`
- `core.general.ingredientNetworkObserverFrequencyDecreaseFactor`: old `I=5` -> new `==5`
- `core.general.ingredientNetworkObserverFrequencyForced`: old `I=1` -> new `==0`
- `core.general.ingredientNetworkObserverFrequencyIncreaseFactor`: old `I=1` -> new `==1`
- `core.general.ingredientNetworkObserverFrequencyMax`: old `I=40` -> new `==40`
- `core.general.ingredientNetworkObserverFrequencyMin`: old `I=5` -> new `==5`
- `core.general.ingredientNetworkObserverThreads`: old `I=4` -> new `==4`
- `core.general.logChangeEvents`: old `B=false` -> new `==false`
- `core.general.operatorRecursionLimit`: old `I=256` -> new `==256`
- `core.general.safeMode`: old `B=false` -> new `==false`
- `core.general.versionChecker`: old `B=true` -> new `==true`
- `general.general.audioReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.audioWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.blockReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.connectorMonoDirectionalBaseConsumption`: old `I=32` -> new `==32`
- `general.general.connectorOmniDirectionalBaseConsumption`: old `I=128` -> new `==128`
- `general.general.effectWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.energyConsumptionMultiplier`: old `I=0` -> new `==0`
- `general.general.entityReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.entityWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.extraDimensionalReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.fluidReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.inventoryReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.inventoryWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.machineReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.machineWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.materializerBaseConsumption`: old `I=1` -> new `==1`
- `general.general.networkReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.panelDisplayBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.panelDisplayBaseConsumptionEnabled`: old `I=2` -> new `==2`
- `general.general.panelLightDynamicBaseConsumption`: old `I=0` -> new `==0`
- `general.general.panelLightStaticBaseConsumption`: old `I=0` -> new `==0`
- `general.general.partOverlayRenderdistance`: old `I=15` -> new `==15`
- `general.general.proxyBaseConsumption`: old `I=2` -> new `==2`
- `general.general.redstoneReaderBaseConsumption`: old `I=1` -> new `==1`
- `general.general.redstoneWriterBaseConsumption`: old `I=1` -> new `==1`
- `general.general.variablestoreBaseConsumption`: old `I=4` -> new `==4`
- `general.general.worldReaderBaseConsumption`: old `I=1` -> new `==1`
- `item.menril_berries.nightVision`: old `B=true` -> new `==true`
- `item.on_the_dynamics_of_integration.bookRewards`: old `B=true` -> new `==true`
- `item.on_the_dynamics_of_integration.obtainOnSpawn`: old `B=false` -> new `==true`
- `machine.delay.maxHistoryCapacity`: old `I=1024` -> new `==1024`
- `machine.energy_battery.capacity`: old `I=100000` -> new `==1000000`
- `machine.energy_battery.energyRateCapacityFraction`: old `I=2000` -> new `==2000`
- `machine.energy_battery.maxCreativeCapacity`: old `I=4096000` -> new `==40960000`
- `machine.energy_battery.minEnergyRate`: old `I=2000` -> new `==2000`
- `machine.general.defaultPartUpdateFreq`: old `I=1` -> new `==1`
- `machine.general.maxDirectionalConnectorOffset`: old `I=512` -> new `==512`
- `machine.mechanical_drying_basin.capacity`: old `I=100000` -> new `==100000`
- `machine.mechanical_drying_basin.consumptionRate`: old `I=80` -> new `==80`
- `machine.mechanical_squeezer.autoEjectFluidRate`: old `I=500` -> new `==500`
- `machine.mechanical_squeezer.capacity`: old `I=100000` -> new `==100000`
- `machine.mechanical_squeezer.consumptionRate`: old `I=80` -> new `==80`
- `worldgeneration.menril_log_filled.filledMenrilLogChance`: old `I=10` -> new `==10`

Old-only keys sample:
- `"mod compat".jei` = `true`
- `biome.biome_meneglin` = `true`
- `biome.biome_meneglin.spawnWeight` = `5`
- `block.coal_generator` = `true`
- `block.creative_energy_battery` = `true`
- `block.crystalized_chorus_block` = `true`
- `block.crystalized_chorus_block_stairs` = `true`
- `block.crystalized_chorus_brick` = `true`
- `block.crystalized_chorus_brick_stairs` = `true`
- `block.crystalized_menril_block` = `true`
- `block.crystalized_menril_block_stairs` = `true`
- `block.crystalized_menril_brick` = `true`
- `block.crystalized_menril_brick_stairs` = `true`
- `block.delay` = `true`
- `block.drying_basin` = `true`
- `block.energy_battery` = `true`
- `block.invisible_light` = `true`
- `block.logic_programmer` = `true`
- `block.materializer` = `true`
- `block.mechanical_drying_basin` = `true`
- `block.mechanical_squeezer` = `true`
- `block.menril_door` = `true`
- `block.menril_leaves` = `true`
- `block.menril_leaves.berriesDropChance` = `4`
- `block.menril_log` = `true`
- `block.menril_log_filled` = `true`
- `block.menril_planks` = `true`
- `block.menril_planks_stairs` = `true`
- `block.menril_sapling` = `true`
- `block.menril_torch` = `true`
- `block.menril_torch_stone` = `true`
- `block.proxy` = `true`
- `block.squeezer` = `true`
- `block.variablestore` = `true`
- `core.general.maxValueByteSize` = `20000`
- `core.general.version` = `0.9.6`
- `item.crystalized_chorus_chunk` = `true`
- `item.crystalized_menril_chunk` = `true`
- `item.facade` = `true`
- `item.labeller` = `true`
- `item.logic_director` = `true`
- `item.menril_berries` = `true`
- `item.on_the_dynamics_of_integration` = `true`
- `item.portable_logic_programmer` = `true`
- `item.variable_transformer` = `true`
- `item.wrench` = `true`
- `machine.energy_battery.energyPerTick` = `2000`
- `machine.energy_battery.maxCapacity` = `65536000`
- `worldgeneration.general.wildMenrilTreeChance` = `350`

New-only keys sample:
- `core.general.logCardEvaluation` = `false`
- `core.general.numberCompactMaximumFractionDigits` = `2`
- `core.general.numberCompactMaximumIntegerDigits` = `3`
- `core.general.numberCompactMinimumFractionDigits` = `0`
- `core.general.numberCompactMinimumIntegerDigits` = `1`
- `core.general.numberCompactUseLongStyle` = `false`
- `core.general.recreateCorruptedNetworks` = `true`
- `core.general.speachMaxFrequency` = `1000`
- `general.general.delayerBaseConsumption` = `2`
- `general.general.diagnosticsWebServerPort` = `3030`
- `general.general.partMinimumUpdateIntervals` = `[]`
- `general.general.partsMinimumUpdateInterval` = `1`
- `machine.cable.dynamicShape` = `true`
- `machine.coal_generator.energyPerTick` = `20`
- `machine.energy_battery.maxCreativeTabCapacity` = `655360000`
- `machine.general.disableCableCollision` = `false`
- `machine.general.enchancementOffsetPartDropValue` = `4`
- `machine.general.maxPartOffset` = `32`
- `machine.general.nbtTagBlacklist` = `[]`
- `machine.general.partOffsetRenderDistance` = `16`
- `machine.general.recipeTagOutputModPriorities` = `[]`
- `machine.invisible_light.invisibleLightBlock` = `true`

### Ported Values

- `item.on_the_dynamics_of_integration.obtainOnSpawn`: `true` -> `false`
  - Old E2 did not auto-grant the Integrated Dynamics manual on first spawn.
- `machine.energy_battery.capacity`: `1000000` -> `100000`
- `machine.energy_battery.maxCreativeCapacity`: `40960000` -> `4096000`
- `machine.energy_battery.maxCreativeTabCapacity`: `655360000` -> `65536000`
  - Preserves old E2 battery capacity scale where current names still map.

## integrateddynamicscompat.cfg -> integrateddynamicscompat-common.toml

- Parsed old scalar values: 14
- Parsed new scalar values: 4
- Same key/value pairs: 0
- Same key but changed value/type: 1
- Old-only scalar keys: 13
- New-only scalar keys: 3

Changed same-name keys:
- `core.general.crashOnModCompatCrash`: old `B=false` -> new `==false`

Old-only keys sample:
- `"mod compat".crafttweaker` = `true`
- `"mod compat".forestry` = `true`
- `"mod compat".ic2` = `true`
- `"mod compat".immersiveengineering` = `true`
- `"mod compat".jei` = `true`
- `"mod compat".refinedstorage` = `true`
- `"mod compat".signals` = `true`
- `"mod compat".tconstruct` = `true`
- `"mod compat".tesla` = `true`
- `"mod compat".thaumcraft` = `true`
- `core.general.crashOnInvalidRecipe` = `false`
- `core.general.debug` = `false`
- `core.general.version` = `1.0.0`

New-only keys sample:
- `biome.general.meneglinBiomeSpawnWeight` = `5`
- `core.general.jeiHeuristicTags` = `true`
- `core.general.reiHeuristicTags` = `true`

## integratedtunnels.cfg -> integratedtunnels-common.toml

- Parsed old scalar values: 39
- Parsed new scalar values: 35
- Same key/value pairs: 0
- Same key but changed value/type: 34
- Old-only scalar keys: 5
- New-only scalar keys: 1

Changed same-name keys:
- `core.general.analytics`: old `B=true` -> new `==true`
- `core.general.ejectItemsOnBlockDropOverflow`: old `B=true` -> new `==true`
- `core.general.ejectItemsOnInconsistentSimulationMovement`: old `B=true` -> new `==true`
- `core.general.fluidRateLimit`: old `I=2147483647` -> new `==2147483647`
- `core.general.inventoryUnchangedTickTimeout`: old `I=10` -> new `==10`
- `core.general.versionChecker`: old `B=true` -> new `==true`
- `core.general.worldInteractionEvents`: old `B=true` -> new `==true`
- `general.general.exporterEnergyBaseConsumption`: old `I=1` -> new `==1`
- `general.general.exporterFluidBaseConsumption`: old `I=1` -> new `==1`
- `general.general.exporterItemBaseConsumption`: old `I=1` -> new `==1`
- `general.general.exporterWorldBlockBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.exporterWorldBlockBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.exporterWorldEnergyBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.exporterWorldEnergyBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.exporterWorldFluidBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.exporterWorldFluidBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.exporterWorldItemBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.exporterWorldItemBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.importerEnergyBaseConsumption`: old `I=1` -> new `==1`
- `general.general.importerFluidBaseConsumption`: old `I=1` -> new `==1`
- `general.general.importerItemBaseConsumption`: old `I=1` -> new `==1`
- `general.general.importerWorldBlockBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.importerWorldBlockBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.importerWorldEnergyBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.importerWorldEnergyBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.importerWorldFluidBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.importerWorldFluidBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.importerWorldItemBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.importerWorldItemBaseConsumptionEnabled`: old `I=32` -> new `==32`
- `general.general.interfaceEnergyBaseConsumption`: old `I=0` -> new `==0`
- `general.general.interfaceFluidBaseConsumption`: old `I=0` -> new `==0`
- `general.general.interfaceItemBaseConsumption`: old `I=0` -> new `==0`
- `general.general.playerSimulatorBaseConsumptionDisabled`: old `I=1` -> new `==1`
- `general.general.playerSimulatorBaseConsumptionEnabled`: old `I=64` -> new `==64`

Old-only keys sample:
- `"mod compat".tesla` = `true`
- `core.general.crashOnInvalidRecipe` = `false`
- `core.general.crashOnModCompatCrash` = `false`
- `core.general.debug` = `false`
- `core.general.version` = `1.3.5`

New-only keys sample:
- `core.general.inventoryUnchangedTickCount` = `3`

## modularrouters.cfg -> modularrouters-common.toml

- Parsed old scalar values: 33
- Parsed new scalar values: 57
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 33
- New-only scalar keys: 57

Old-only keys sample:
- `general.misc.alwaysShowSettings` = `true`
- `general.misc.startWithGuide` = `false`
- `general.module.backgroundTint` = `true`
- `general.module.breakerHarvestLimit` = `true`
- `general.module.breakerParticles` = `true`
- `general.module.extruder2BaseRange` = `24`
- `general.module.extruder2MaxRange` = `48`
- `general.module.extruderBaseRange` = `12`
- `general.module.extruderMaxRange` = `24`
- `general.module.extruderPushEntities` = `true`
- `general.module.extruderSound` = `true`
- `general.module.flingerEffects` = `true`
- `general.module.placerParticles` = `false`
- `general.module.puller2BaseRange` = `12`
- `general.module.puller2MaxRange` = `24`
- `general.module.pullerParticles` = `true`
- `general.module.sender1BaseRange` = `8`
- `general.module.sender1MaxRange` = `16`
- `general.module.sender2BaseRange` = `24`
- `general.module.sender2MaxRange` = `48`
- `general.module.senderParticles` = `true`
- `general.module.vacuumBaseRange` = `6`
- `general.module.vacuumMaxRange` = `12`
- `general.module.vacuumParticles` = `true`
- `general.router.baseTickRate` = `20`
- `general.router.configKey` = `c`
- `general.router.ecoTimeout` = `100`
- `general.router.fluidBaseTransferRate` = `50`
- `general.router.fluidMaxTransferRate` = `400`
- `general.router.hardMinTickRate` = `2`
- `general.router.lowPowerTickRate` = `100`
- `general.router.mBperFluidUpgrade` = `10`
- `general.router.ticksPerUpgrade` = `2`

New-only keys sample:
- `"Energy Costs".activatorModuleEnergyCost` = `0`
- `"Energy Costs".activatorModuleEnergyCostAttack` = `150`
- `"Energy Costs".breakerModuleEnergyCost` = `0`
- `"Energy Costs".detectorModuleEnergyCost` = `0`
- `"Energy Costs".distributorModuleEnergyCost` = `0`
- `"Energy Costs".dropperModuleEnergyCost` = `0`
- `"Energy Costs".energydistributorModuleEnergyCost` = `0`
- `"Energy Costs".energyoutputModuleEnergyCost` = `0`
- `"Energy Costs".extruderModule1EnergyCost` = `0`
- `"Energy Costs".extruderModule2EnergyCost` = `0`
- `"Energy Costs".flingerModuleEnergyCost` = `0`
- `"Energy Costs".fluidModule2EnergyCost` = `0`
- `"Energy Costs".fluidModuleEnergyCost` = `0`
- `"Energy Costs".placerModuleEnergyCost` = `0`
- `"Energy Costs".playerModuleEnergyCost` = `0`
- `"Energy Costs".pullerModule1EnergyCost` = `0`
- `"Energy Costs".pullerModule2EnergyCost` = `0`
- `"Energy Costs".senderModule1EnergyCost` = `0`
- `"Energy Costs".senderModule2EnergyCost` = `0`
- `"Energy Costs".senderModule3EnergyCost` = `0`
- `"Energy Costs".vacuumModuleEnergyCost` = `0`
- `"Energy Costs".voidModuleEnergyCost` = `0`
- `Module.breakerHarvestLevelLimit` = `true`
- `Module.breakerParticles` = `true`
- `Module.dimensionBlacklist` = `[]`
- `Module.extruder1BaseRange` = `16`
- `Module.extruder1MaxRange` = `32`
- `Module.extruder2BaseRange` = `32`
- `Module.extruder2MaxRange` = `64`
- `Module.extruderPushEntities` = `true`
- `Module.extruderSound` = `true`
- `Module.flingerEffects` = `true`
- `Module.fluid2BaseRange` = `12`
- `Module.fluid2MaxRange` = `24`
- `Module.placerParticles` = `true`
- `Module.puller2BaseRange` = `12`
- `Module.puller2MaxRange` = `24`
- `Module.pullerParticles` = `true`
- `Module.sender1BaseRange` = `8`
- `Module.sender1MaxRange` = `16`
- `Module.sender2BaseRange` = `24`
- `Module.sender2MaxRange` = `48`
- `Module.senderParticles` = `true`
- `Module.vacuumBaseRange` = `6`
- `Module.vacuumMaxRange` = `12`
- `Module.vacuumParticles` = `true`
- `Router.baseTickRate` = `20`
- `Router.blockBreakXPDrops` = `true`
- `Router.ecoTimeout` = `100`
- `Router.fePerEnergyUpgrade` = `50000`

### Ported Values

- `Module.extruder1BaseRange`: `16` -> `12`
- `Module.extruder1MaxRange`: `32` -> `24`
- `Module.extruder2BaseRange`: `32` -> `24`
- `Module.extruder2MaxRange`: `64` -> `48`
- `Module.placerParticles`: `true` -> `false`

These preserve old E2 Modular Routers range and particle behavior. Sender, puller, vacuum, router tick, and fluid-transfer values already matched old E2 where the modern config still exposes them.

## rftools/rftools.cfg -> rftoolsdim-common.toml

- Parsed old scalar values: 586
- Parsed new scalar values: 3
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 586
- New-only scalar keys: 3

Old-only keys sample:
- `blockprotector.blockProtectorMaxRF` = `500000`
- `blockprotector.blockProtectorRFPerTick` = `20000`
- `blockprotector.enabled` = `true`
- `blockprotector.maxProtectDistance` = `10`
- `blockprotector.rfForExplosionProtection` = `10000`
- `blockprotector.rfForHarvestAttempt` = `2000`
- `blockprotector.rfPerProtectedBlock` = `5`
- `booster.boosterMaxRF` = `200000`
- `booster.boosterRFPerTick` = `1000`
- `booster.energyMultiplier` = `500000.0`
- `builder.builderMaxRF` = `10000000`
- `builder.builderRFPerTick` = `50000`
- `builder.builderRfPerEntity` = `5000`
- `builder.builderRfPerLiquid` = `300`
- `builder.builderRfPerOperation` = `500`
- `builder.builderRfPerPlayer` = `40000`
- `builder.builderRfPerQuarry` = `300`
- `builder.builderRfPerSkipped` = `50`
- `builder.clearingQuarryAllowed` = `true`
- `builder.collectRFPerItem` = `20`
- `builder.collectRFPerTickPerArea` = `0.5`
- `builder.collectRFPerXP` = `2.0`
- `builder.collectTimer` = `10`
- `builder.dimensionCostFactor` = `5.0`
- `builder.fortunequarryShapeCardFactor` = `2.0`
- `builder.maxBuilderDimension` = `512`
- `builder.maxBuilderOffset` = `260`
- `builder.maxSpaceChamberDimension` = `128`
- `builder.oldSphereCylinderShape` = `false`
- `builder.quarryAllowed` = `true`
- `builder.quarryBaseSpeed` = `8`
- `builder.quarryChunkloads` = `true`
- `builder.quarryInfusionSpeedFactor` = `20`
- `builder.quarryReplacE` = `minecraft:dirt`
- `builder.quarryTileEntities` = `true`
- `builder.shapeCardAllowed` = `true`
- `builder.showProgressHud` = `true`
- `builder.silkquarryShapeCardFactor` = `3.0`
- `builder.spaceProjectorMaxRF` = `100000`
- `builder.spaceProjectorRFPerTick` = `1000`
- `builder.tileEntityMode` = `MOVE_WHITELIST`
- `builder.voidShapeCardFactor` = `0.5`
- `coalgen.enabled` = `true`
- `coalgen.generatePerTick` = `60`
- `coalgen.generatorChargePerTick` = `1000`
- `coalgen.generatorMaxRF` = `500000`
- `coalgen.generatorRFPerTick` = `2000`
- `coalgen.ticksPerCoal` = `600`
- `crafter.crafterMaxRF` = `50000`
- `crafter.crafterRFPerTick` = `500`

New-only keys sample:
- `commonBlobMaxHealth` = `30`
- `legendaryBlobMaxHealth` = `5000`
- `rareBlobMaxHealth` = `250`

## scannable.cfg -> scannable-common.toml

- Parsed old scalar values: 46
- Parsed new scalar values: 28
- Same key/value pairs: 0
- Same key but changed value/type: 1
- Old-only scalar keys: 45
- New-only scalar keys: 27

Changed same-name keys:
- `general.baseScanRadius`: old `I=64` -> new `==64`

Old-only keys sample:
- `general.energyCapacityScanner` = `5000`
- `general.energyCostModuleAnimal` = `25`
- `general.energyCostModuleBlock` = `100`
- `general.energyCostModuleEntity` = `75`
- `general.energyCostModuleFluid` = `50`
- `general.energyCostModuleMonster` = `50`
- `general.energyCostModuleOreCommon` = `75`
- `general.energyCostModuleOreRare` = `100`
- `general.energyCostModuleRange` = `100`
- `general.energyCostModuleStructure` = `150`
- `general.glowstone` = `0xE9E68E`
- `general.injectDepthTexture` = `true`
- `general.lava` = `0xE26723`
- `general.logBlockDropLookupFailures` = `false`
- `general.oreAluminium` = `0xCBE4E2`
- `general.oreAluminum` = `0xCBE4E2`
- `general.oreArdite` = `0xB77E11`
- `general.oreCinnabar` = `0xF5DA25`
- `general.oreCoal` = `0x433E3B`
- `general.oreCobalt` = `0x413BB8`
- `general.oreCopper` = `0xE4A020`
- `general.oreCrystalAir` = `0xF7E677`
- `general.oreCrystalEarth` = `0x49B45A`
- `general.oreCrystalEntropy` = `0x545476`
- `general.oreCrystalFire` = `0xDC7248`
- `general.oreCrystalOrder` = `0x9FF2DE`
- `general.oreCrystalWater` = `0x9595D5`
- `general.oreDiamond` = `0x48E2F0`
- `general.oreEmerald` = `0x12BA16`
- `general.oreGold` = `0xF4F71F`
- `general.oreIron` = `0xA17951`
- `general.oreLapis` = `0x4863F0`
- `general.oreLead` = `0x8187C3`
- `general.oreMithril` = `0x97D5FE`
- `general.oreNickel` = `0xD0D3AC`
- `general.orePlatinum` = `0x7AC0FD`
- `general.orePlutonium` = `0x9DE054`
- `general.oreQuartz` = `0xB3D9D2`
- `general.oreRedstone` = `0xE61E1E`
- `general.oreSilver` = `0xE8F2FB`
- `general.oreTin` = `0xCCE4FE`
- `general.oreUranium` = `0x9DE054`
- `general.oreYellorium` = `0xD8E054`
- `general.useEnergy` = `true`
- `general.water` = `0x4275DC`

New-only keys sample:
- `blocks.ignoredBlockTags` = `[]`
- `blocks.ignoredBlocks` = `["minecraft:command_block"]`
- `chests.commonChestBlocks` = `[]`
- `chests.commonChestTags` = `["forge:barrels", "forge:chests", "minecraft:shulker_boxes"]`
- `energy.energyCapacityScanner` = `5000`
- `energy.energyCostModuleAnimal` = `25`
- `energy.energyCostModuleBlock` = `100`
- `energy.energyCostModuleChest` = `100`
- `energy.energyCostModuleEntity` = `75`
- `energy.energyCostModuleFluid` = `50`
- `energy.energyCostModuleMonster` = `50`
- `energy.energyCostModuleOreCommon` = `75`
- `energy.energyCostModuleOreRare` = `100`
- `energy.energyCostModuleRange` = `100`
- `energy.useEnergy` = `true`
- `fluids.ignoredFluidTags` = `[]`
- `general.scanStayDuration` = `10000`
- `ores.commonOreBlockTags` = `["forge:ores/iron", "forge:ores/redstone", "forge:ores/coal", "forge:ores/quartz", "forge:ores/tin", "forge:ores/copper"]`
- `ores.commonOreBlocks` = `["minecraft:clay"]`
- `ores.rareOreBlockTags` = `[]`
- `ores.rareOreBlocks` = `["minecraft:glowstone"]`
- `range.rangeModifierModuleBlock` = `0.5`
- `range.rangeModifierModuleChest` = `0.25`
- `range.rangeModifierModuleFluid` = `0.5`
- `range.rangeModifierModuleOreCommon` = `0.25`
- `range.rangeModifierModuleOreRare` = `0.25`
- `range.rangeModifierModuleRange` = `0.5`

## storagedrawers.cfg -> functionalstorage/functionalstorage-common.toml

- Parsed old scalar values: 60
- Parsed new scalar values: 14
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 60
- New-only scalar keys: 14

Old-only keys sample:
- `blocks.compdrawers.baseStorage` = `16`
- `blocks.compdrawers.enabled` = `true`
- `blocks.compdrawers.recipeOutput` = `1`
- `blocks.controller.enabled` = `true`
- `blocks.controller.range` = `12`
- `blocks.controllerslave.enabled` = `true`
- `blocks.framedblocks.consumeDecorationItems` = `true`
- `blocks.framedblocks.enableFramedDrawers` = `true`
- `blocks.framedblocks.enableFramedTrims` = `true`
- `blocks.framedblocks.enableFramingTable` = `true`
- `blocks.fulldrawers1.baseStorage` = `32`
- `blocks.fulldrawers1.enabled` = `true`
- `blocks.fulldrawers1.recipeOutput` = `1`
- `blocks.fulldrawers2.baseStorage` = `16`
- `blocks.fulldrawers2.enabled` = `true`
- `blocks.fulldrawers2.recipeOutput` = `2`
- `blocks.fulldrawers4.baseStorage` = `8`
- `blocks.fulldrawers4.enabled` = `true`
- `blocks.fulldrawers4.recipeOutput` = `4`
- `blocks.halfdrawers2.baseStorage` = `8`
- `blocks.halfdrawers2.enabled` = `true`
- `blocks.halfdrawers2.recipeOutput` = `2`
- `blocks.halfdrawers4.baseStorage` = `4`
- `blocks.halfdrawers4.enabled` = `true`
- `blocks.halfdrawers4.recipeOutput` = `4`
- `blocks.trim.enabled` = `true`
- `blocks.trim.recipeOutput` = `4`
- `general.creativeTabVanillaWoods` = `true`
- `general.defaultQuantify` = `false`
- `general.enableCreativeUpgrades` = `true`
- `general.enableDebugLogging` = `false`
- `general.enableDrawerUI` = `true`
- `general.enableFallbackRecipes` = `true`
- `general.enableFramedDrawers` = `true`
- `general.enableIndicatorUpgrades` = `true`
- `general.enableItemConversion` = `true`
- `general.enableLockUpgrades` = `true`
- `general.enablePersonalUpgrades` = `true`
- `general.enableQuantifiableUpgrades` = `true`
- `general.enableRedstoneUpgrades` = `true`
- `general.enableShroudUpgrades` = `true`
- `general.enableSidedInput` = `true`
- `general.enableSidedOutput` = `true`
- `general.enableStorageUpgrades` = `true`
- `general.enableTape` = `true`
- `general.enableVoidUpgrades` = `true`
- `general.invertClick` = `false`
- `general.invertShift` = `false`
- `general.keepContentsOnBreak` = `true`
- `general.wailaStackRemainder` = `stack + remainder`

New-only keys sample:
- `FunctionalStorageConfig.ARMORY_CABINET_SIZE` = `4096`
- `FunctionalStorageConfig.COPPER_MULTIPLIER` = `8`
- `FunctionalStorageConfig.DIAMOND_MULTIPLIER` = `24`
- `FunctionalStorageConfig.DRAWER_CONTROLLER_LINKING_RANGE` = `8`
- `FunctionalStorageConfig.FLUID_DIVISOR` = `2`
- `FunctionalStorageConfig.GOLD_MULTIPLIER` = `16`
- `FunctionalStorageConfig.NETHERITE_MULTIPLIER` = `32`
- `FunctionalStorageConfig.RANGE_DIVISOR` = `4`
- `FunctionalStorageConfig.UPGRADE_COLLECTOR_ITEMS` = `4`
- `FunctionalStorageConfig.UPGRADE_PULL_FLUID` = `500`
- `FunctionalStorageConfig.UPGRADE_PULL_ITEMS` = `4`
- `FunctionalStorageConfig.UPGRADE_PUSH_FLUID` = `500`
- `FunctionalStorageConfig.UPGRADE_PUSH_ITEMS` = `4`
- `FunctionalStorageConfig.UPGRADE_TICK` = `4`

### Ported Values

- `FunctionalStorageConfig.DRAWER_CONTROLLER_LINKING_RANGE`: `8` -> `12`
  - Functional Storage is the current Storage Drawers successor in the pack; old E2 Storage Drawers used controller range `12`.

## torchmaster.cfg -> torchmaster.toml

- Parsed old scalar values: 22
- Parsed new scalar values: 15
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 22
- New-only scalar keys: 15

Old-only keys sample:
- `compat.LycanitesMobsBlockAll` = `true`
- `compat.MoCreaturesBlockAll` = `true`
- `general.BeginnerTooltips` = `true`
- `general.DreadLampRange` = `64`
- `general.FeralFlareLanternLightCountHardcap` = `255`
- `general.LycanitesMobsBlockAll` = `true`
- `general.MegaTorchAllowSilkTouch` = `false`
- `general.MegaTorchAllowVanillaSpawners` = `true`
- `general.MegaTorchBurnoutRate` = `0`
- `general.MegaTorchBurnoutValue` = `2147483647`
- `general.MegaTorchExtinguishOnHarvest` = `false`
- `general.MegaTorchRange` = `64`
- `general.MoCreaturesBlockAll` = `true`
- `general.TerrainLighterSpacing` = `5`
- `general.TerrainLighterTorchCount` = `7`
- `general.TorchVisualizerSegmentationFactor` = `2.0`
- `general.feralFlareLightDecayInstantly` = `false`
- `general.feralFlareMinLightLevel` = `10`
- `general.feralFlareRadius` = `16`
- `general.feralFlareTickRate` = `5`
- `general.frozenPearlDurability` = `1024`
- `general.slighlyMoreAggressiveBlocking` = `false`

New-only keys sample:
- `General.aggressiveSpawnChecks` = `false`
- `General.beginnerTooltips` = `true`
- `General.blockOnlyNaturalSpawns` = `true`
- `General.blockVillageSieges` = `true`
- `General.dreadLampEntityBlockListOverrides` = `[]`
- `General.dreadLampRadius` = `64`
- `General.feralFlareLanternLightCountHardcap` = `255`
- `General.feralFlareMinLightLevel` = `10`
- `General.feralFlareRadius` = `16`
- `General.feralFlareTickRate` = `5`
- `General.frozenPearlDurability` = `1024`
- `General.logSpawnChecks` = `false`
- `General.lycanitesMobsBlockAll` = `true`
- `General.megaTorchEntityBlockListOverrides` = `[]`
- `General.megaTorchRadius` = `64`

## cookingforblockheads.cfg -> cookingforblockheads-common.toml

- Parsed old scalar values: 15
- Parsed new scalar values: 11
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 15
- New-only scalar keys: 11

Old-only keys sample:
- `client.Show Ingredient Icon` = `true`
- `compat.Oven Requires Cooking Oil` = `false`
- `general.Cow in a Jar` = `true`
- `general.Cow in a Jar Milk per Tick` = `0.5`
- `general.Disallow Oven Automation` = `false`
- `general.Large Counters` = `false`
- `general.Oven Cook Time Multiplier` = `1.0`
- `general.Oven Fuel Time Multiplier` = `0.33000001311302185`
- `general.Sink Requires Water` = `false`
- `modules.Extra Food` = `true`
- `modules.Food Expansion` = `true`
- `modules.More Foods` = `true`
- `modules.Pam's Harvestcraft` = `true`
- `modules.Vanilla Food Pantry` = `true`
- `modules.Vanilla Minecraft` = `true`

New-only keys sample:
- `allowVeryToastedBread` = `true`
- `compressedCowJarMilkMultiplier` = `9.0`
- `cowJarEnabled` = `true`
- `cowJarMilkPerTick` = `1`
- `disallowOvenAutomation` = `false`
- `largeCounters` = `false`
- `ovenCookTimeMultiplier` = `1.0`
- `ovenFuelTimeMultiplier` = `0.33000001311302185`
- `ovenRequiresCookingOil` = `false`
- `showIngredientIcon` = `true`
- `sinkRequiresWater` = `false`

### Ported Values

- `cowJarMilkPerTick`: `1` -> `0.5`
  - Direct mapping from old E2 `Cow in a Jar Milk per Tick = 0.5`.

## enderstorage.cfg -> EnderStorage.cfg

- Parsed old scalar values: 5
- Parsed new scalar values: 5
- Same key/value pairs: 0
- Same key but changed value/type: 3
- Old-only scalar keys: 2
- New-only scalar keys: 2

Changed same-name keys:
- `anarchyMode`: old `==false` -> new `B=false`
- `disableCreatorVisuals`: old `==false` -> new `B=false`
- `personalItem`: old `==minecraft:diamond|0` -> new `S="minecraft:diamond"`

Old-only keys sample:
- `item.storage-size` = `1`
- `useVanillaEnderChestSounds` = `false`

New-only keys sample:
- `item_storage_size` = `1`
- `useVanillaEnderChestsSounds` = `false`

## farmingforblockheads.cfg -> farmingforblockheads-common.toml

- Parsed old scalar values: 7
- Parsed new scalar values: 8
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 7
- New-only scalar keys: 8

Old-only keys sample:
- `client.Show Registry Warnings` = `false`
- `general.Chicken Nest Range` = `8`
- `general.Feeding Trough Max Animals` = `8`
- `general.Feeding Trough Range` = `8`
- `general.Fertilizer Bonus Crop Chance` = `1.0`
- `general.Fertilizer Bonus Growth Chance` = `1.0`
- `general.Fertilizer Regression Chance` = `0.0`

New-only keys sample:
- `chickenNestRange` = `8`
- `feedingTroughMaxAnimals` = `24`
- `feedingTroughRange` = `8`
- `fertilizerBonusCropChance` = `1.0`
- `fertilizerBonusGrowthChance` = `1.0`
- `fertilizerRegressionChance` = `0.0`
- `merchantNames` = `["Swap-O-Matic", "Emerald Muncher", "Weathered Salesperson"]`
- `treatMerchantsLikeBabies` = `true`

### Ported Values

- `feedingTroughMaxAnimals`: `24` -> `8`
  - Direct mapping from old E2 `Feeding Trough Max Animals = 8`.
  - Chicken nest range, feeding trough range, and fertilizer chances already matched old E2.

## tconstruct.cfg -> tconstruct-common.toml

- Parsed old scalar values: 33
- Parsed new scalar values: 38
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 33
- New-only scalar keys: 38

Old-only keys sample:
- `clientside.dumpTextureMap` = `false`
- `clientside.enableForgeBucketModel` = `false`
- `clientside.extraTooltips` = `true`
- `clientside.listAllPartMaterials` = `true`
- `clientside.listAllTables` = `false`
- `clientside.listAllToolMaterials` = `true`
- `clientside.renderInventoryInWorld` = `true`
- `clientside.renderInventoryNullLayer` = `true`
- `clientside.temperatureCelsius` = `true`
- `gameplay.AutosmeltFortuneInteraction` = `true`
- `gameplay.addFlintRecipe` = `true`
- `gameplay.addLeatherDryingRecipe` = `true`
- `gameplay.allowBrickCasting` = `true`
- `gameplay.chestsKeepInventory` = `true`
- `gameplay.craftCastableMaterials` = `false`
- `gameplay.enableClayCasts` = `true`
- `gameplay.limitPiggybackpack` = `false`
- `gameplay.matchVanillaSlimeblock` = `false`
- `gameplay.obsidianAlloy` = `true`
- `gameplay.oreToIngotRatio` = `2.0`
- `gameplay.registerAllItems` = `false`
- `gameplay.reuseStencils` = `true`
- `gameplay.spawnWithBook` = `false`
- `gameplay.testIMC` = `false`
- `worldgen.arditeRate` = `18`
- `worldgen.cobaltRate` = `18`
- `worldgen.genArdite` = `true`
- `worldgen.genCobalt` = `true`
- `worldgen.generateIslandsInSuperflat` = `false`
- `worldgen.generateSlimeIslands` = `true`
- `worldgen.magmaIslandRate` = `150`
- `worldgen.slimeIslandRate` = `1000`
- `worldgen.slimeIslandsOnlyGenerateInSurfaceWorlds` = `true`

New-only keys sample:
- `compatability.allowIngotlessAlloys` = `true`
- `compatability.allowMonsterMeleeModifiers` = `true`
- `compatability.immersive_engineering_chemthrower_shot_value` = `1.25`
- `debug.disableSideInventoryWhitelist` = `false`
- `debug.forceIntegrationMaterials` = `false`
- `debug.logInvalidToolStack` = `"WARNING"`
- `debug.quickApplyToolModifiersSurvival` = `false`
- `gameplay.extendBlastProtectionSlots` = `true`
- `gameplay.extendFireProtectionSlots` = `true`
- `gameplay.repairKitAmount` = `2.0`
- `gameplay.shouldSpawnWithTinkersBook` = `false`
- `gameplay.syncKnockbackResistance` = `true`
- `gameplay.toolInventorySync` = `"MINIMAL"`
- `loot.drop_dragon_Scales` = `true`
- `loot.slimy_loot` = `true`
- `loot.wanderer_ancient_tool_weight` = `6`
- `recipes.addGravelToFlintRecipe` = `true`
- `recipes.cheaperNetheriteAlloy` = `true`
- `recipes.glassRecipeFix` = `true`
- `recipes.heads.blaze` = `true`
- `recipes.heads.cave_spider` = `true`
- `recipes.heads.drowned` = `true`
- `recipes.heads.enderman` = `true`
- `recipes.heads.husk` = `true`
- `recipes.heads.piglin_brute` = `true`
- `recipes.heads.spider` = `true`
- `recipes.heads.stray` = `true`
- `recipes.heads.zombified_piglin` = `true`
- `recipes.ore_rates.foundry.nuggetsPerMetal` = `9`
- `recipes.ore_rates.foundry.shardsPerGem` = `4`
- `recipes.ore_rates.foundry_byproduct.nuggetsPerMetal` = `3`
- `recipes.ore_rates.foundry_byproduct.shardsPerGem` = `4`
- `recipes.ore_rates.melter.nuggetsPerMetal` = `12`
- `recipes.ore_rates.melter.shardsPerGem` = `8`
- `recipes.ore_rates.smeltery.nuggetsPerMetal` = `12`
- `recipes.ore_rates.smeltery.shardsPerGem` = `8`
- `recipes.slimeRecipeFix` = `true`
- `recipes.witherBoneDrop` = `true`
