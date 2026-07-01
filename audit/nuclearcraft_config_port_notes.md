# NuclearCraft Config Port Notes

Generated comparison notes for config value porting.

## nuclearcraft.cfg -> NuclearCraft/common.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 46
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 46

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `"GregTech Energy Compatibility".accelerators_energy_tier` = `"ZPM"`
- `"GregTech Energy Compatibility".energy_upgrades_for_next_tier` = `16`
- `"GregTech Energy Compatibility".fission_reactor_energy_tier` = `"EV"`
- `"GregTech Energy Compatibility".fusion_reactor_energy_tier` = `"IV"`
- `"GregTech Energy Compatibility".gregtech_energy_compatibility` = `"GTCEU_AND_FE"`
- `"GregTech Energy Compatibility".gregtech_energy_overcharge_explosions` = `true`
- `"GregTech Energy Compatibility".kugelblitz_energy_tier` = `"ZPM"`
- `"GregTech Energy Compatibility".limit_fe_output` = `false`
- `"GregTech Energy Compatibility".processor_energy_tier` = `"MV"`
- `"GregTech Energy Compatibility".turbine_energy_tier` = `"EV"`
- `Energy.decay_generator_power_gen` = `128`
- `Energy.generation_multiplier` = `1.0`
- `Energy.panel_power` = `[448, 1792, 112, 28]`
- `Energy.register_panel` = `[true, true, true, true]`
- `Energy.register_rtg` = `[true, true, true, true]`
- `Energy.rtg_power` = `[112, 448, 1792, 4096]`
- `Energy.rtg_radiation` = `[560, 57800, 200000, 1900000]`
- `Energy.steam_turbine_power_gen` = `80`
- `Misc.debug_logging` = `false`
- `energy_storage.energy_block_registration` = `[true, true, true, true, true, true, true, true]`
- `energy_storage.energy_block_storage` = `[1600000, 102400000, 6400000, 32000000, 2048000000, 512000000, 25600000, 128000000]`
- `energy_storage.lightning_rod_charge` = `1048576`
- `energy_storage.lithium_ion_battery_storage` = `1048576`
- `energy_storage.qnp_energy_per_block` = `200`
- `energy_storage.qnp_energy_storage` = `2097152`
- `pu_239_bomb.chunk_resends_per_tick` = `16`
- `pu_239_bomb.fast_block_writes` = `true`
- `pu_239_bomb.fuse_ticks` = `60`
- `pu_239_bomb.ops_per_tick` = `16384`
- `pu_239_bomb.radius_horizontal` = `196`
- `pu_239_bomb.radius_vertical` = `64`
- `q36_quantite_disruptor.beam_block_break_radius` = `3`
- `q36_quantite_disruptor.beam_cooldown_ticks` = `60`
- `q36_quantite_disruptor.beam_damage` = `200.0`
- `q36_quantite_disruptor.beam_fx_ticks` = `20`
- `q36_quantite_disruptor.beam_qc_cost` = `2000`
- `q36_quantite_disruptor.beam_radiation` = `2000000`
- `q36_quantite_disruptor.beam_range` = `64.0`
- `q36_quantite_disruptor.pulse_cooldown_ticks` = `10`
- `q36_quantite_disruptor.pulse_damage` = `50.0`
- `q36_quantite_disruptor.pulse_fx_ticks` = `10`
- `q36_quantite_disruptor.pulse_qc_cost` = `200`
- `q36_quantite_disruptor.pulse_radiation` = `200000`
- `storage_blocks.barrel_block_registration` = `[true, true, true, true]`
- `storage_blocks.barrel_capacity` = `[512, 128, 8192, 2048]`
- `storage_blocks.container_block_registration` = `[true, true, true, true]`

## nuclearcraft.cfg -> NuclearCraft/fission.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 17
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 17

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `fission_reactor.active_heatsink_coolant_per_tick` = `10`
- `fission_reactor.active_heatsink_prime` = `true`
- `fission_reactor.boiling_mult` = `100.0`
- `fission_reactor.fe_generation_multiplier` = `10.0`
- `fission_reactor.heat_capacity` = `1000000.0`
- `fission_reactor.heat_multiplier` = `1.0`
- `fission_reactor.heat_multiplier_cap` = `3.0`
- `fission_reactor.max_size` = `26`
- `fission_reactor.min_size` = `3`
- `fission_reactor.moderator_fe_multiplier` = `16.666666667`
- `fission_reactor.moderator_heat_multiplier` = `33.33333333`
- `fission_reactor.reactor_explosion_radius` = `4.0`
- `fission_reactor.supports_boiling_mode` = `true`
- `msr_reactor.pebbles_per_fuel_cell` = `4`
- `reactor_fuel.depletion_multiplier` = `1.0`
- `reactor_fuel.fuel_heat_multiplier` = `1.0`
- `reactor_fuel.heat_multiplier` = `3.24444444`

## nuclearcraft.cfg -> NuclearCraft/fusion.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 13
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 13

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `electromagnets.heat` = `[1.0, 0.5, 4.0, 2.0, 0.2]`
- `electromagnets.power` = `[4000, 2000, 16000, 8000, 1000]`
- `electromagnets.registered` = `[true, true, true, true, true]`
- `fusion_reactor.max_size` = `32`
- `fusion_reactor.min_size` = `1`
- `fusion_reactor.minimal_magnetic_field` = `8.0`
- `fusion_reactor.plasma_to_energy_convertion` = `1.0`
- `fusion_reactor.reactor_explosion_radius` = `2.0`
- `fusion_reactor.rf_amplification_multiplier` = `5.0`
- `rf_amplifiers.heat` = `[300, 2260, 580, 1140, 4500]`
- `rf_amplifiers.power` = `[500, 4000, 1000, 2000, 8000]`
- `rf_amplifiers.registered` = `[true, true, true, true, true]`
- `rf_amplifiers.voltage` = `[200000, 2000000, 500000, 1000000, 4000000]`

## nuclearcraft.cfg -> NuclearCraft/world.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 4
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 4

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `Biome.wasteland` = `true`
- `Dimension.wasteland` = `true`
- `Villages.scientist_house` = `true`
- `Villages.wandering_trader_trades` = `true`

## nuclearcraft.cfg -> NuclearCraft/processors.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 93
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 93

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `"Common settings".base_power` = `128`
- `"Common settings".base_time` = `240`
- `"Common settings".gteu_amperage` = `2`
- `"Common settings".gteu_explode` = `false`
- `"Common settings".gteu_support` = `1`
- `"Common settings".skip_ticks` = `0`
- `alloy_smelter.base_power` = `50`
- `alloy_smelter.base_time` = `200`
- `alloy_smelter.register` = `true`
- `analyzer.base_power` = `50`
- `analyzer.base_time` = `200`
- `analyzer.register` = `true`
- `assembler.base_power` = `50`
- `assembler.base_time` = `200`
- `assembler.register` = `true`
- `centrifuge.base_power` = `50`
- `centrifuge.base_time` = `200`
- `centrifuge.register` = `true`
- `chemical_reactor.base_power` = `50`
- `chemical_reactor.base_time` = `200`
- `chemical_reactor.register` = `true`
- `creative_particle_source.base_power` = `50`
- `creative_particle_source.base_time` = `200`
- `creative_particle_source.register` = `true`
- `crystallizer.base_power` = `50`
- `crystallizer.base_time` = `200`
- `crystallizer.register` = `true`
- `decay_hastener.base_power` = `50`
- `decay_hastener.base_time` = `200`
- `decay_hastener.register` = `true`
- `electrolyzer.base_power` = `50`
- `electrolyzer.base_time` = `200`
- `electrolyzer.register` = `true`
- `extractor.base_power` = `50`
- `extractor.base_time` = `200`
- `extractor.register` = `true`
- `fluid_enricher.base_power` = `50`
- `fluid_enricher.base_time` = `200`
- `fluid_enricher.register` = `true`
- `fluid_infuser.base_power` = `50`
- `fluid_infuser.base_time` = `200`
- `fluid_infuser.register` = `true`
- `fuel_reprocessor.base_power` = `50`
- `fuel_reprocessor.base_time` = `200`
- `fuel_reprocessor.register` = `true`
- `gas_scrubber.base_power` = `50`
- `gas_scrubber.base_time` = `200`
- `gas_scrubber.register` = `true`
- `in_situ_leaching.add_ie_veins` = `true`
- `in_situ_leaching.allow_to_leach_ie_veins` = `true`

## nuclearcraft.cfg -> NuclearCraft/radiation.toml

- Parsed old scalar values: 160
- Parsed new scalar values: 12
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 160
- New-only scalar keys: 12

Old-only keys sample:
- `accelerator.accelerator_electromagnet_power` = `5000`
- `accelerator.accelerator_supercooler_coolant` = `1`
- `accelerator.accelerator_update_rate` = `40`
- `condenser.condenser_max_size` = `24`
- `condenser.condenser_min_size` = `1`
- `entities.entity_tracking_range` = `64`
- `fission.fission_active_cooler_max_rate` = `5`
- `fission.fission_base_capacity` = `64000`
- `fission.fission_base_max_heat` = `25000`
- `fission.fission_comparator_max_heat` = `50`
- `fission.fission_experimental_mechanics` = `false`
- `fission.fission_explosions` = `false`
- `fission.fission_force_heat_comparator` = `false`
- `fission.fission_fuel_use` = `1.0`
- `fission.fission_heat_generation` = `1.0`
- `fission.fission_max_size` = `24`
- `fission.fission_meltdown_radiation_multiplier` = `1.0`
- `fission.fission_min_size` = `1`
- `fission.fission_moderator_extra_heat` = `2.0`
- `fission.fission_moderator_extra_power` = `1.0`
- `fission.fission_neutron_reach` = `4`
- `fission.fission_overheat` = `true`
- `fission.fission_power` = `1.0`
- `fission.fission_sound_volume` = `1.0`
- `fission.fission_update_rate` = `40`
- `fission.fission_water_cooler_requirement` = `true`
- `fusion.fusion_active_cooling` = `true`
- `fusion.fusion_alternate_sound` = `false`
- `fusion.fusion_base_power` = `1.0`
- `fusion.fusion_comparator_max_efficiency` = `90`
- `fusion.fusion_electromagnet_power` = `1000`
- `fusion.fusion_enable_sound` = `true`
- `fusion.fusion_fuel_use` = `1.0`
- `fusion.fusion_heat_generation` = `1.0`
- `fusion.fusion_heating_multiplier` = `1.0`
- `fusion.fusion_max_size` = `24`
- `fusion.fusion_meltdown_radiation_multiplier` = `1.0`
- `fusion.fusion_min_size` = `1`
- `fusion.fusion_overheat` = `true`
- `fusion.fusion_plasma_craziness` = `true`
- `fusion.fusion_sound_volume` = `1.0`
- `fusion.fusion_update_rate` = `40`
- `generators.generator_rf_per_eu` = `4`
- `generators.generator_update_rate` = `20`
- `heat_exchanger.heat_exchanger_alternate_exhaust_recipe` = `false`
- `heat_exchanger.heat_exchanger_condenser_tube_spread_ratio` = `0.5`
- `heat_exchanger.heat_exchanger_coolant_mult` = `30.0`
- `heat_exchanger.heat_exchanger_max_size` = `24`
- `heat_exchanger.heat_exchanger_min_size` = `1`
- `heat_exchanger.heat_exchanger_tube_spread_ratio` = `0.5`

New-only keys sample:
- `radiation.armor_shielding` = `["mekanism:hazmat_mask|3", "mekanism:hazmat_gown|5", "mekanism:hazmat_pants|4", "mekanism:hazmat_boots|3", "mekanism:mekasuit_helmet|5", "mekanism:mekasuit_bodyarmor|5", "mekanism:mekasuit_pants|5", "mekanism:mekasuit_boots|5", "nuclearcraft:hazmat_mask|3", "nuclearcraft:hazmat_chest|5", "nuclearcraft:hazmat_pants|4", "nuclearcraft:hazmat_boots|3", "nuclearcraft:hev_helmet|5", "nuclearcraft:hev_chest|7", "nuclearcraft:hev_pants|6", "nuclearcraft:hev_boots|5"]`
- `radiation.background_radiation` = `20`
- `radiation.biome_radiation` = `["nuclearcraft:wasteland|40000", "minecraft:nether_wastes|10000"]`
- `radiation.decay_speed` = `2000`
- `radiation.decay_speed_for_player` = `50`
- `radiation.dimension_radiation` = `["nuclearcraft:wasteland|50000", "minecraft:the_nether|5000"]`
- `radiation.enabled` = `true`
- `radiation.gain_speed_for_player` = `0.1`
- `radiation.items_radiation` = `["nuclearcraft:spaxelhoe_thorium|50000", "mekanism:pellet_polonium|4000000", "mekanism:pellet_plutonium|2500000", "mekanism:reprocessed_fissile_fragment|1800000"]`
- `radiation.mekanism_radiation_integration` = `true`
- `radiation.radiation_removal_items` = `["minecraft:golden_carrot|10000000", "minecraft:golden_apple|100000000", "minecraft:enchanted_golden_apple|2500000000", "nuclearcraft:dominos|250000000", "nuclearcraft:moresmore|2500000000", "nuclearcraft:evenmoresmore|1000000000", "nuclearcraft:radaway|50000000000"]`
- `radiation.update_interval` = `40`

## Human Porting Guidance

NuclearCraft 1.12 `nuclearcraft.cfg` was a single large file. NuclearCraft Neoteric 1.20 splits config across many TOML and JSON files. Do not bulk-port old scalar keys.

High-value areas to review manually:

1. Reactor safety/balance
   - Old fission values include `fission_power`, `fission_fuel_use`, `fission_heat_generation`, `fission_overheat`, `fission_explosions=false`, reactor size limits, cooling rates, and fuel times.
   - New likely targets: `NuclearCraft/fission.toml`, `NuclearCraft/fission_fuel/*.json`, and `NuclearCraft/heat_sinks/*.json`.
   - Preserve old intent only where the same mechanic clearly exists.

2. Ore/world generation
   - Old E2 likely coordinated NuclearCraft ore generation with broader ore unification.
   - New likely targets: `NuclearCraft/world.toml` and `NuclearCraft/ore_generation.toml`.
   - Also inspect KubeJS/JAOPCA material handling before disabling or changing ores.

3. Radiation
   - New dedicated target: `NuclearCraft/radiation.toml`.
   - Do not assume old radiation options map directly.

4. Processors
   - New target: `NuclearCraft/processors.toml`.
   - Porting speed/power values could have broad progression impact; defer until recipe/progression balance is clearer.

5. Material/fluid errors from latest log
   - Latest live log includes many missing fluid/tag errors around NuclearCraft/JAOPCA materials, e.g. xenorium, molten hard carbon, chromium, niobium, silicon, titanium, osmium.
   - These may be config/material-generation issues, not just recipe issues.
   - Review alongside `config/jaopca/materials/*`, `config/jaopca/modules/*`, and KubeJS fluid compatibility scripts.

Recommended next action:

- Start with `NuclearCraft/world.toml` / `ore_generation.toml` to determine whether ore generation aligns with E2's unified-ore strategy.
- Then handle reactor balance after material/fluid tags are stable.

## Applied Ports

- `config/NuclearCraft/fission.toml`
  - Set `fission_reactor.max_size = 24` to preserve old E2 `fission_max_size=24`.
  - Set `fission_reactor.reactor_explosion_radius = 0.0` to preserve old E2 `fission_explosions=false`; the new config documents `0` as disabling explosions.
  - Left `fission_reactor.min_size = 3` because the new config range no longer allows the old `fission_min_size=1`.
- `config/NuclearCraft/fusion.toml`
  - Set `fusion_reactor.max_size = 24` to preserve old E2 `fusion_max_size=24`.
  - Set `fusion_reactor.reactor_explosion_radius = 0.0`; old E2 exposed fusion overheating and meltdown radiation but did not expose a fusion explosion toggle.
  - Left `fusion_reactor.min_size = 1`, already matching old E2 `fusion_min_size=1`.
- `config/NuclearCraft/ore_generation.toml`
  - Set every current ore entry `register = false`.
  - Reason: old E2 `ore_gen` disabled all NuclearCraft native ores: copper, tin, lead, thorium, uranium, boron, lithium, and magnesium. Old E2 used centralized CoFH/worldgen handling instead of NC native generation.
  - Current 1.20-only ore entries such as platinum, silver, cobalt, and zinc were also disabled to preserve the same "no native NC ore generation" intent.
- `config/NuclearCraft/world.toml`
  - Set `Dimension.wasteland = false` to preserve old E2 `wasteland_dimension_gen=false`.
  - Left `Biome.wasteland = true`, matching old E2 `wasteland_biome=true`.
- `config/NuclearCraft/radiation.toml`
  - Set `radiation.enabled = false` to preserve old E2 `radiation_enabled=false`.

Deferred:

- Heat exchanger, turbine, molten salt, and processor size/balance values still need a separate review because NuclearCraft Neoteric's multiblock schemas and ranges differ from 1.12 NuclearCraft.
