# Mekanism Config Port Notes

Generated comparison notes for config value porting.

## mekanism.cfg -> Mekanism/general.toml

- Parsed old scalar values: 410
- Parsed new scalar values: 70
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 410
- New-only scalar keys: 70

Old-only keys sample:
- `client.AlignHUDLeft` = `true`
- `client.AmbientLightingLevel` = `15`
- `client.ConfiguratorModeScroll` = `true`
- `client.EnableAmbientLighting` = `false`
- `client.EnableMachineSounds` = `true`
- `client.EnablePlayerSounds` = `true`
- `client.Holidays` = `true`
- `client.MachineEffects` = `true`
- `client.MultiblockFormParticles` = `true`
- `client.OpaqueTransmitterRender` = `false`
- `client.ReplaceSoundsWhenResuming` = `true`
- `client.SoundVolume` = `1.0`
- `general.AestheticWorldDamage` = `true`
- `general.AllowChunkloading` = `false`
- `general.AllowProtection` = `true`
- `general.AllowSpawnerBoxPickup` = `true`
- `general.AllowTransmitterAlloyUpgrade` = `true`
- `general.ArmoredJepackDamageMax` = `115`
- `general.ArmoredJetpackDamageRatio` = `0.8`
- `general.BlacklistForgePower` = `false`
- `general.BlacklistIC2Power` = `false`
- `general.BlacklistRFPower` = `false`
- `general.BlacklistTeslaPower` = `false`
- `general.ClientUpdateDelay` = `10`
- `general.ControlCircuitOreDict` = `true`
- `general.CopperPerChunk` = `0`
- `general.CopperVeinSize` = `8`
- `general.DestroyDisabledBlocks` = `true`
- `general.DigitalMinerMaxRadius` = `32`
- `general.DisassemblerBatteryCapacity` = `1000000.0`
- `general.DisassemblerDamageMax` = `20`
- `general.DisassemblerDamageMin` = `4`
- `general.DisassemblerEnergyUsage` = `10`
- `general.DisassemblerEnergyUsageHoe` = `10`
- `general.DisassemblerEnergyUsageWeapon` = `2000`
- `general.DisassemblerExtendedMiningMode` = `true`
- `general.DisassemblerFastMode` = `true`
- `general.DisassemblerMiningCount` = `128`
- `general.DisassemblerMiningRange` = `10`
- `general.DisassemblerSlowMode` = `true`
- `general.DisassemblerVeinMiningMode` = `true`
- `general.DynamicTankEasterEgg` = `false`
- `general.EUToJoules` = `0.1`
- `general.EnableWorldRegeneration` = `false`
- `general.EnergyPerHeat` = `1000.0`
- `general.EnergyPerRedstone` = `10000.0`
- `general.EnergyType` = `RF`
- `general.EthyleneBurnTime` = `20`
- `general.EvaporationHeatDissipation` = `0.02`
- `general.EvaporationMaxTemp` = `3000.0`

New-only keys sample:
- `general.allowChunkloading` = `true`
- `general.auto_eject.chemical` = `1024`
- `general.auto_eject.dumpExcessKeepRatio` = `0.9`
- `general.auto_eject.fluid` = `1024`
- `general.blockDeactivationDelay` = `60`
- `general.boiler.cooledCoolantPerTank` = `256000`
- `general.boiler.heatedCoolantPerTank` = `256000`
- `general.boiler.steamPerTank` = `160000`
- `general.boiler.waterPerTank` = `16000`
- `general.boilerWaterConductivity` = `0.7`
- `general.cardboardModBlacklist` = `[]`
- `general.digital_miner.maxRadius` = `32`
- `general.digital_miner.silkMultiplier` = `12`
- `general.digital_miner.ticksPerMine` = `80`
- `general.dynamic_tank.chemicalPerTank` = `16000000`
- `general.dynamic_tank.fluidPerTank` = `350000`
- `general.easyMinerFilters` = `false`
- `general.energy_conversion.HydrogenEnergyDensity` = `"200"`
- `general.energy_conversion.blacklistFluxNetworks` = `false`
- `general.energy_conversion.blacklistForge` = `false`
- `general.energy_conversion.blacklistIC2` = `false`
- `general.energy_conversion.euConversionRate` = `"10"`
- `general.energy_conversion.feConversionRate` = `"2.5000"`
- `general.energy_conversion.maxEnergyPerSteam` = `"10"`
- `general.fuelwoodTickMultiplier` = `1`
- `general.heatPerFuelTick` = `400.0`
- `general.laser.aestheticWorldDamage` = `true`
- `general.laser.energyNeededPerHardness` = `"100000"`
- `general.laser.energyPerDamage` = `"2500"`
- `general.laser.range` = `64`
- `general.logPackets` = `false`
- `general.maxSolarNeutronActivatorRate` = `64`
- `general.maxUpgradeMultiplier` = `10`
- `general.nutritional_paste.mbPerFood` = `50`
- `general.nutritional_paste.saturation` = `0.8`
- `general.oredictionificator.validItemFilters` = `["forge:dusts/", "forge:ingots/", "forge:nuggets/", "forge:ores/", "forge:raw_materials/", "forge:storage_blocks/"]`
- `general.prefilled.fluidTanks` = `true`
- `general.prefilled.gasTanks` = `true`
- `general.prefilled.infusionTanks` = `true`
- `general.prefilled.pigmentTanks` = `true`
- `general.prefilled.slurryTanks` = `true`
- `general.pump.maxPlenisherNodes` = `4000`
- `general.pump.maxPumpRange` = `80`
- `general.pump.pumpHeavyWaterAmount` = `10`
- `general.pump.pumpWaterSources` = `false`
- `general.quantum_entangloporter.chemicalBuffer` = `8192000`
- `general.quantum_entangloporter.energyBuffer` = `"256000000"`
- `general.quantum_entangloporter.fluidBuffer` = `256000`
- `general.radiation.chunkCheckRadius` = `5`
- `general.radiation.negativeEffectsMinSeverity` = `0.1`

## Human Porting Guidance

The automatic scalar comparison is noisy because Mekanism changed from 1.12 `.cfg` camel-case keys to 1.20 nested TOML keys. Do not treat the old-only/new-only counts as meaning nothing maps.

Clear semantic mappings to review first:

- Old `general.AllowChunkloading=false` -> new `general.allowChunkloading=true`.
  - This is a real behavior difference. E2 1.12 disabled Mekanism anchor upgrade chunkloading. Consider setting new `allowChunkloading = false` if preserving E2 behavior is desired.
- Old `general.DigitalMinerMaxRadius=32` -> new `general.digital_miner.maxRadius=32`.
  - Already matches; no action.
- Old `general.MinerSilkMultiplier=5` -> new `general.digital_miner.silkMultiplier=12`.
  - Real tuning difference. Decide whether E2 intended cheaper silk mining or whether Mekanism 1.20 balance should stand.
- Old `general.MaxPumpRange=80` -> new `general.pump.maxPumpRange=80`.
  - Already matches; no action.
- Old `general.MaxPlenisherNodes=4000` -> new `general.pump.maxPlenisherNodes=4000`.
  - Already matches; no action.
- Old `general.AestheticWorldDamage=true` -> new `general.laser.aestheticWorldDamage=true`.
  - Already matches; no action.
- Old power conversion values mostly map to `general.energy_conversion.*`.
  - `JoulesToEU=10.0` -> `euConversionRate="10"` appears consistent.
  - `JoulesToForge=2.5` -> `feConversionRate="2.5000"` appears consistent.
  - Old RF/Tesla-specific keys are obsolete or folded into Forge energy.

Old worldgen keys should not be blindly ported:

- Old `CopperPerChunk=0` and `OsmiumPerChunk=0` likely disabled Mekanism ore generation because E2 used broader ore unification.
- New Mekanism worldgen lives in `config/Mekanism/world.toml`, not `general.toml`.
- Review `Mekanism/world.toml` against the pack's current ore strategy before changing it.

Old `mekanism/BoxBlacklist.txt` should not be copied directly:

- Most entries are removed mods: Astral Sorcery, IC2, Environmental Tech.
- The only obviously still relevant old entry is `cookingforblockheads:fridge`, but the block ID may have changed in 1.20.
- New equivalent is likely `general.cardboardModBlacklist` in `Mekanism/general.toml`, but it is mod-id based, not block-id based.
- If cardboard-box abuse is a concern, check current Mekanism 1.20 docs/tags for a block-level cardboard blacklist before porting.

Recommended first edit candidate:

- Consider changing `config/Mekanism/general.toml` `allowChunkloading = true` to `false` to preserve E2 1.12 behavior.
- Leave other obvious mappings unchanged unless gameplay testing shows a balance issue.
