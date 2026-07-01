# Thermal Dynamo Fuel Parity

Source: original E2 1.12 `ThermalExpansion-1.12.2-5.5.7.1` built-in fuel JSONs under `assets/thermalexpansion/content/dynamo/`, old E2 `config/cofh/thermalexpansion/common.cfg`, and the decompiled 1.12 Thermal Expansion dynamo classes.

## 1.12 Dynamo Power Model

Old E2 did not globally rebalance Thermal dynamo fuel tables. It used Thermal Expansion's built-in fuel data and changed only the Reactant Dynamo base power from the comment/default of 40 RF/t to 60 RF/t. Numismatic was also 60 RF/t in the shipped config.

Base dynamos scale by upgrade tier: 100%, 150%, 200%, 250%, 300%. At level 0, the old E2 base rates were:

| 1.12 dynamo | Old E2 base RF/t | Current 1.20 equivalent/status |
| --- | ---: | --- |
| Steam | 40 | Closest current path is Stirling at 40 RF/t; no 1.20 Steam Dynamo fuel table port yet |
| Magmatic | 40 | Magmatic exists at 40 RF/t |
| Compression | 40 | Compression exists at 40 RF/t |
| Reactant | 60 | No direct current Thermal equivalent found |
| Enervation | 40 | Disenchantment Dynamo exists at 40 RF/t for enchanted-item behavior |
| Numismatic | 60 | Numismatic exists at 60 RF/t; Lapidary exists separately at 60 RF/t |
| Gourmand | n/a | Current 1.20 has Gourmand at 40 RF/t; old E2's TE jar has Gourmand classes but no `Dynamo.Gourmand` config section and no Gourmand fuel JSON |

Generic augments:

| Augment | Old 1.12 effect |
| --- | --- |
| Auxiliary Transmission Coil | Adds one additional base-power unit to RF/t at the current upgrade tier |
| Fuel Catalyzer | Adds +15% total fuel energy per augment |
| Excitation Field Limiter | Prevents RF loss from coil saturation; does not improve fuel density |
| Transmission Coil Ducting | Side output behavior only |

## Specialized Augments

These are important because several old 1.12 augment modes are now separate 1.20 dynamos or have no direct replacement.

| Old augment | 1.12 dynamo | Level 0 RF/t | Fuel-density change | 1.20 implication |
| --- | --- | ---: | --- | --- |
| Boiler Conversion | Steam | 160 | +15%; outputs steam instead of RF | No direct current Thermal dynamo target |
| Turbine Conversion | Steam | 160 | Consumes steam, effectively 2 RF/mB steam | No direct current Thermal dynamo target |
| Boiler Conversion | Magmatic | 80 | -40%; outputs steam instead of RF | No direct current Thermal dynamo target |
| Isentropic Reservoir | Magmatic | 160 | +15% plus coolant factor | Equivalent behavior is not currently ported |
| Boiler Conversion | Compression | 80 | -40%; outputs steam instead of RF | No direct current Thermal dynamo target |
| Ignition Plugs | Compression | 160 | +50%; restricts fuel to `refined_fuel` | Important for current Compression Dynamo refined fuel parity |
| Agitative Manifold | Compression | 120 | +25%; restricts fuel to `refined_biofuel` | Important for current biofuel parity if Grassoline/refined biofuel is present |
| Closed-Loop Cooling | Compression | 40 | No fuel consumed as coolant; coolant factor still boosts density | Equivalent behavior is not currently ported |
| Elemental Catalyzer | Reactant | 300 | +25%; restricts to elemental reactions | No direct current Thermal equivalent found |
| Disjunctive Extraction | Enervation | 200 | +25%; restricts to enchanted items | Current equivalent is Disenchantment Dynamo, but parity should include +25% if matching the old augment |
| Lapidary Calibration | Numismatic | 300 | +25%; restricts to gems | Current equivalent is Lapidary Dynamo; existing script ports raw old fuel values, not this +25% augmented value |

Coolant factors for Magmatic Isentropic Reservoir and Compression Closed-Loop Cooling were: water +0%, ice +20%, IC2 coolant +30%, cryotheum +40%. Isentropic Reservoir also has the base +15%, so lava with cryotheum would use 155% of the listed fuel energy. Compression Ignition Plugs and Agitative Manifold are separate locked-fuel modes, so their effective fuel totals are shown in the Compression table below.

## Steam / Stirling Fuels

Old Steam Dynamo consumes solid fuel plus water. Listed totals are RF per item before generic Fuel Catalyzer. Charcoal and charcoal dust omit an explicit value in Thermal's JSON, so Thermal falls back to furnace burn time x10: 1600 ticks x10 = 16000 RF.

| Fuel | Old RF/item | Duration at 40 RF/t | Boiler mode RF/item | Boiler duration at 160 RF/t |
| --- | ---: | ---: | ---: | ---: |
| Coal | 24000 | 600 ticks | 27600 | 172.5 ticks |
| Charcoal | 16000 | 400 ticks | 18400 | 115 ticks |
| Coal Dust | 24000 | 600 ticks | 27600 | 172.5 ticks |
| Charcoal Dust | 16000 | 400 ticks | 18400 | 115 ticks |
| Coal Block | 240000 | 6000 ticks | 276000 | 1725 ticks |
| Charcoal Block | 160000 | 4000 ticks | 184000 | 1150 ticks |
| Fuel Coke | 40000 | 1000 ticks | 46000 | 287.5 ticks |
| Fuel Coke Block | 400000 | 10000 ticks | 460000 | 2875 ticks |

## Magmatic Fuels

Old Magmatic fluid totals are RF per 1000 mB. Thermal's `energy_mod` entries use `DEFAULT_ENERGY = 100000`, so lava is 120000 RF/bucket and IC2 pahoehoe lava is 80000 RF/bucket.

| Fuel fluid | Old RF/bucket | Old RF/mB | Duration at 40 RF/t | Isentropic + water RF/bucket | Isentropic + cryotheum RF/bucket |
| --- | ---: | ---: | ---: | ---: | ---: |
| `lava` | 120000 | 120 | 3000 ticks | 138000 | 186000 |
| `pyrotheum` | 2000000 | 2000 | 50000 ticks | 2300000 | 3100000 |
| `ic2pahoehoe_lava` | 80000 | 80 | 2000 ticks | 92000 | 124000 |
| `ic2hot_coolant` | 40000 | 40 | 1000 ticks | 46000 | 62000 |

## Compression Fuels

Old Compression totals are RF per 1000 mB. Base duration assumes the normal 40 RF/t Compression Dynamo. Ignition Plugs and Agitative Manifold are shown only for the fuels they lock to.

| Fuel fluid | Old RF/bucket | Old RF/mB | Duration at 40 RF/t | Augmented old mode |
| --- | ---: | ---: | ---: | --- |
| `creosote` | 40000 | 40 | 1000 ticks | none |
| `coal` | 400000 | 400 | 10000 ticks | none |
| `crude_oil` | 400000 | 400 | 10000 ticks | none |
| `refined_oil` | 1000000 | 1000 | 25000 ticks | none |
| `refined_fuel` | 1500000 | 1500 | 37500 ticks | Ignition Plugs: 2250000 RF/bucket, 2250 RF/mB, 14062.5 ticks at 160 RF/t |
| `tree_oil` | 400000 | 400 | 10000 ticks | none |
| `seed_oil` | 80000 | 80 | 2000 ticks | none |
| `refined_biofuel` | 800000 | 800 | 20000 ticks | Agitative Manifold: 1000000 RF/bucket, 1000 RF/mB, 8333.3 ticks at 120 RF/t |
| `fuel_dense` | 2400000 | 2400 | 60000 ticks | none |
| `fuel_gaseous` | 200000 | 200 | 5000 ticks | none |
| `fuel_light` | 800000 | 800 | 20000 ticks | none |
| `fuel_mixed_heavy` | 640000 | 640 | 16000 ticks | none |
| `fuel_mixed_light` | 320000 | 320 | 8000 ticks | none |
| `oil_dense` | 1600000 | 1600 | 40000 ticks | none |
| `oil_distilled` | 400000 | 400 | 10000 ticks | none |
| `oil_heavy` | 1000000 | 1000 | 25000 ticks | none |
| `canolaoil` | 80000 | 80 | 2000 ticks | none |
| `refinedcanolaoil` | 200000 | 200 | 5000 ticks | none |
| `crystaloil` | 400000 | 400 | 10000 ticks | none |
| `empoweredoil` | 700000 | 700 | 17500 ticks | none |
| `fire_water` | 750000 | 750 | 18750 ticks | none |
| `hootch` | 300000 | 300 | 7500 ticks | none |
| `rocket_fuel` | 1000000 | 1000 | 25000 ticks | none |
| `bio.ethanol` | 500000 | 500 | 12500 ticks | none |
| `biodiesel` | 500000 | 500 | 12500 ticks | none |
| `oil` | 400000 | 400 | 10000 ticks | none |
| `diesel` | 800000 | 800 | 20000 ticks | none |
| `gasoline` | 1200000 | 1200 | 30000 ticks | none |
| `ic2biogas` | 50000 | 50 | 1250 ticks | none |

Current 1.20 Thermal defaults only define Compression fuels for creosote, tree oil, and refined fuel. Default creosote is 20000 FE/bucket, which is half of old 1.12 creosote's 40000 RF/bucket. Current Thermal does not ship a crude oil Compression fuel recipe; old E2 crude/plain oil was 400000 RF/bucket.

Current port overrides/adds:

| Current fluid | Ported FE/bucket | Ported FE/mB | Rationale |
| --- | ---: | ---: | --- |
| `#forge:crude_oil` | 400000 | 400 | Old E2 crude/plain oil parity |
| `thermal:heavy_oil` | 1500000 | 1500 | Between crude oil and refined fuel; higher than light oil because the Still yields less heavy oil from crude oil, making it the scarcer fraction |
| `thermal:light_oil` | 1000000 | 1000 | Between crude oil and refined fuel; lower than heavy oil because the Still yields more light oil from crude oil |
| `thermal:refined_fuel` | 2250000 | 2250 | Old Ignition Plugs density |

Advanced Generators also uses `thermal:refined_fuel = 2250 FE/mB`, matching the current Thermal Compression Dynamo refined-fuel override and old Ignition Plugs density.

## Reactant Fuels

Old Reactant consumes one item plus 100 mB fluid per reaction. Base old E2 Reactant throughput was 60 RF/t. Elemental Catalyzer mode runs at 300 RF/t and adds +25% total energy.

| Reactant | Fluid | Old RF/reaction | Duration at 60 RF/t |
| --- | --- | ---: | ---: |
| Sugar | `redstone` | 80000 | 1333.3 ticks |
| Nether Wart | `redstone` | 100000 | 1666.7 ticks |
| Gunpowder | `redstone` | 100000 | 1666.7 ticks |
| Blaze Dust | `redstone` | 150000 | 2500 ticks |
| Ghast Tear | `redstone` | 150000 | 2500 ticks |
| Sugar | `glowstone` | 100000 | 1666.7 ticks |
| Nether Wart | `glowstone` | 125000 | 2083.3 ticks |
| Gunpowder | `glowstone` | 125000 | 2083.3 ticks |
| Blaze Dust | `glowstone` | 200000 | 3333.3 ticks |
| Ghast Tear | `glowstone` | 200000 | 3333.3 ticks |

Elemental Catalyzer reactions:

| Reactant | Fluid | Raw old RF | Effective old RF with augment | Duration at 300 RF/t |
| --- | --- | ---: | ---: | ---: |
| Pyrotheum Dust | `cryotheum` | 400000 | 500000 | 1666.7 ticks |
| Cryotheum Dust | `pyrotheum` | 400000 | 500000 | 1666.7 ticks |
| Aerotheum Dust | `petrotheum` | 400000 | 500000 | 1666.7 ticks |
| Petrotheum Dust | `aerotheum` | 400000 | 500000 | 1666.7 ticks |

## Enervation / Disenchantment Fuels

Old Enervation base throughput was 40 RF/t. Its normal fuel table is redstone fuel plus RF container extraction. Disjunctive Extraction is the enchanted-item mode: it runs at 200 RF/t and adds +25% to the enchant-derived energy.

| Fuel | Old RF/item | Duration at 40 RF/t |
| --- | ---: | ---: |
| Redstone Dust | 64000 | 1600 ticks |
| Redstone Block | 640000 | 16000 ticks |
| RF container item | Stored RF extracted from item | depends on stored RF |

Disjunctive Extraction formula: enchantment energy is `(sum enchant minimum enchantability for each level + triangular enchant count bonus) * 5000`, then the augment applies +25%. This is not a fixed item table, so current Disenchantment Dynamo parity should be checked by formula rather than by static fuel entries.

## Numismatic / Lapidary Fuels

Old Numismatic base throughput was 60 RF/t. Lapidary Calibration is the old gem mode: it runs at 300 RF/t and adds +25% total energy. The current KubeJS script ports raw gem totals; strict old augmented parity would use the `Old RF with Lapidary` column instead.

| Fuel | Old raw RF/item | Old RF with Lapidary | Duration at 300 RF/t with Lapidary | Current port RF/item |
| --- | ---: | ---: | ---: | ---: |
| `gemQuartz` | 40000 | 50000 | 166.7 ticks | 40000 |
| `gemLapis` | 80000 | 100000 | 333.3 ticks | 80000 |
| `gemPrismarine` | 150000 | 187500 | 625 ticks | 150000 |
| `gemEmerald` | 200000 | 250000 | 833.3 ticks | 200000 |
| BoP/TechReborn common gems | 200000 | 250000 | 833.3 ticks | 200000 for selected modern replacements |
| `gemApatite` | 40000 | 50000 | 166.7 ticks | 50000 |
| `gemDiamond` | 1200000 | 1500000 | 5000 ticks | 1200000 |
| `gemCrystalFlux` | 1500000 | 1875000 | 6250 ticks | 1500000 |

Regular old Numismatic coin fuels:

| Fuel | Old RF/item | Duration at 60 RF/t |
| --- | ---: | ---: |
| Basic Thermal coins | 30000-150000 | 500-2500 ticks |
| Some modded coin metadata variants | 30000-150000 | 500-2500 ticks |
| Emerald in regular table | 200000 | 3333.3 ticks |

Current KubeJS Lapidary mapping:

| Old 1.12 fuel | Old raw RF | 1.20 fuel | Current port FE | Notes |
| --- | ---: | --- | ---: | --- |
| `gemQuartz` | 40000 | `#forge:gems/quartz` | 50000 | old Lapidary Calibration +25% |
| missing in old table | n/a | `#forge:gems/black_quartz` | 50000 | current pack quartz-tier gem |
| missing in old table | n/a | `#forge:gems/certus_quartz` | 50000 | current pack quartz-tier gem |
| `gemApatite` | 40000 | `#forge:gems/apatite` | 50000 | old Lapidary Calibration +25% |
| `gemLapis` | 80000 | `#forge:gems/lapis` | 100000 | old Lapidary Calibration +25% |
| `gemPrismarine` | 150000 | `#forge:gems/prismarine` | 187500 | old Lapidary Calibration +25% |
| missing in old table | n/a | `#forge:gems/fluix` | 50000 | AE2 crafted gem; valued at quartz tier because one charged certus + one quartz yields two fluix |
| `gemEmerald` | 200000 | `#forge:gems/emerald` | 250000 | old Lapidary Calibration +25% |
| `gemAmethyst` | 200000 | `#forge:gems/amethyst` | 250000 | old Lapidary Calibration +25% |
| `gemRuby` | 200000 | `#forge:gems/ruby` | 250000 | old Lapidary Calibration +25% |
| `gemSapphire` | 200000 | `#forge:gems/sapphire` | 250000 | old Lapidary Calibration +25% |
| replacement | 200000 | `#forge:gems/source` | 150000 | Ars Nouveau; below common gems because it can be made from lapis plus automatable source |
| replacement | 200000 | `#forge:gems/psigem` | 250000 | Psi |
| replacement | 200000 | `#forge:gems/carminite` | 250000 | Twilight Forest |
| replacement | 200000 | Ender IO crystal gem tags | 250000 | current crystal spread |
| high-tier replacement | 500000 | `#forge:gems/vibrant_crystal` | 625000 | current high-tier replacement, not old raw table |
| `gemDiamond` | 1200000 | `#forge:gems/diamond` | 1500000 | old Lapidary Calibration +25% |
| diamond upgrade replacement | n/a | Botania mana diamond/dragonstone | 1875000 | diamond upgrades, valued on par with Flux-Infused Gem |
| `gemCrystalFlux` | 1500000 | `redstone_arsenal:flux_gem` | 1875000 | old Lapidary Calibration +25% |

## Starting Conclusions

- Old E2's Thermal fuels mostly used upstream Thermal Expansion values, but the specialized augments are part of the old balance. For parity, current 1.20 split dynamos should usually model the old augmented mode, not the raw base fuel table.
- Compression refined fuel is much stronger in old Thermal than the current Advanced Generators compatibility value implies: 1500 RF/mB normal, 2250 RF/mB with Ignition Plugs. The current port now overrides Thermal Compression Dynamo `thermal:refined_fuel` to 2250000 RF/bucket and adds crude oil/heavy oil/light oil Compression fuel entries. No current `refined_biofuel`/Grassoline fluid was found, so the Agitative Manifold path was documented but not re-created.
- Current Lapidary fuels now model strict old Lapidary Calibration parity: fuel values are +25% over the old raw gem table and Lapidary Dynamo base power is 300 RF/t.
- Current Disenchantment Dynamo base power now models old Disjunctive Extraction throughput at 200 RF/t. In-game testing confirmed current Thermal's enchantment fuel formula is `(sum enchantment minimum cost at level + triangular enchant count bonus) * 8000`: Efficiency I produced 16000 FE, Efficiency II produced 96000 FE, and Efficiency I + Unbreaking I produced 72000 FE. This is intentionally accepted rather than forcing old 1.12's lower `* 5000` plus augment multiplier behavior.
- The old 1.12 augment recipes were recovered from decompiled `ItemAugment.initialize()`. Current split-dynamo recipes now use those old augment ingredient patterns: Lapidary Dynamo uses Signalum Gear / Electrum Plates / Emerald around a Numismatic Dynamo, and Disenchantment Dynamo uses Signalum Gear / Gold Plates / Lapis around a Magmatic Dynamo.
