# Energy Generation Balance Audit

## Old E2 Findings

The old 1.12 pack did explicit energy-generation balancing through configs and a few CraftTweaker scripts. Most values were left at mod defaults, but several high-impact generators were intentionally scaled down or had concrete pack values worth preserving.

## Ported Values

| Area | Old E2 value | 1.20.1 port |
| --- | --- | --- |
| Extreme Reactors | `fuelUsageMultiplier=3.0`, `reactorPowerProductionMultiplier=0.5`, turbine size 16 | Already ported in `config/extremereactors/common.toml` |
| Thermal Dynamos | Steam/Magmatic/Compression/Enervation 40 RF/t, Reactant/Numismatic 60 RF/t | Already ported in `defaultconfigs/thermal-server.toml` |
| Actually Additions / Actually Subtractions | Leaf 300 CF/leaf, cooldown 5, area 7; coal generator 30 CF/t in old E2 config; oil generator old tier list 40/80/120/160 CF/t with 100/150/300/400 duration values | Leaf/reconstructor/miner values already ported in `config/actuallyadditions-common.toml`. Added OpenLoader recipe overrides for Actually Subtractions solid fuels and liquid canola fuels in `config/openloader/data/e2_energy_balance`: solid fuels now run at 40 CF/t, and canola oils use the old E2 oil curve. |
| Mekanism Generators | solar 50 J/t, advanced solar 200 J/t, bio 300 J/t, heat 150 J/t, lava modifier 5, wind 45-180 J/t over Y 48-255, turbine flow 16000/640/32000, fusion fuel 1500000 | Ported in `config/Mekanism/generators.toml` |
| Advanced Generators turbine modules | old material caps: iron 10, gold 40, steel 80, vibrant 150, enderium 160 MJ/t | Ported to current tier caps 10/40/80/150/160 FE/t in `config/advgenerators-common.toml` |
| Advanced Generators fuels | biodiesel 50 MJ/mB, ethene 100 MJ/mB, oil 30 MJ/mB | Added OpenLoader datapack overrides: biodiesel 50, ethene 100, Thermal refined fuel 2250 FE/mB to match the current Thermal Compression Dynamo refined-fuel value |
| Immersive Petroleum portable generator | gasoline 5, 256 | Ported gasoline numeric fuel use from 6 to 5 in `defaultconfigs/immersivepetroleum-server.toml`; retained new naphtha/benzol entries |
| NuclearCraft passive generators | solar Basic/Advanced/DU/Elite 20/60/120/240 RF/t; RTG Uranium/Plutonium/Americium/Californium 50/250/150/300 RF/t | Ported to current config order in `config/NuclearCraft/common.toml` |
| Draconic Evolution reactor | output multiplier 0.5, fuel usage 2.0, explosion scale 0.2 | Ported in `config/brandon3055/DraconicEvolution.cfg` |
| Powah | Not present in old E2 | Conservative 1.20.1-only balance pass in `config/powah.json5`: Furnator/Magmator 20/60/120/240/480/960/1920 FE/t, Reactor 250/750/1500/4000/10000/25000/75000 FE/t, Solar/Thermo 20/50/90/150/240/400/640 FE/t |
| Cyclic Fuel Generator | No old E2 value found | Reduced from 80 FE/t to 40 FE/t in `config/cyclic.toml`; recipe is early enough that it should sit with Thermal/Ender IO/Actually Additions solid-fuel generation rather than above them. |
| Iron Furnaces Generator augment | Not present in old E2 | Added `config/ironfurnaces-client.toml` rate tuning. Regular generator fuels still use the mod's hardcoded `ForgeHooks burn time * 20 FE`, but generation rates now track Thermal Stirling Dynamo upgrade tiers: copper/iron approximate one upgrade, silver/gold two upgrades, emerald/crystal/obsidian three upgrades, and netherite four upgrades. |

## Not Directly Ported

- Ender IO 1.12 exposed many generator values, but current Ender IO has different generators and much lower photovoltaic tiers. No direct E2 value was applied beyond documenting the mismatch.
- Extra Utilities 2, IC2, Forestry engines, and BuildCraft-style MJ generation are absent from the current 1.20.1 pack.
- NuclearCraft fission/fusion/turbine internals changed substantially in the current mod. Passive solar/RTG outputs were ported, but modern reactor multipliers were left for launch/playtest rather than forcing old 1.12 fuel-table assumptions onto the new system.
- Immersive Petroleum changed the portable-generator fuel field from the old tick wording to current second wording. The old configured gasoline numeric value was preserved, but this should be checked in-game.
- Powah had no old E2 equivalent, so its values are not an E2 port. They are a pack-local balance pass against the already-ported generator landscape: passive Powah generation stays above Mekanism/NuclearCraft solar at high tier without trivializing them, fuel burners no longer eclipse large/reactor generation, and Powah reactors remain strong late-game without the default 500k FE/t Nitro spike.

## Consumer-Side Follow-Up

After porting the generation values, the matching machine/recipe energy costs were checked for obvious cases where 1.20.1 generation may have been raised to compensate for higher machine drain.

| Area | Finding | Action |
| --- | --- | --- |
| Mekanism core machines | Many common machines are equal or cheaper than old E2: Metallurgic Infuser 50 J/t unchanged, Osmium Compressor 100 unchanged, Purification/Injection/Chemical machines unchanged, Crusher/Energized Smelter/Enrichment are 50 J/t now vs 75 J/t old. Some specific consumers are higher: Digital Miner 1000 J/t vs 100 old, Laser 10000 J/t vs 5000 old, Electric Pump 100 J/t vs 50 old. | No automatic revert. The generator nerfs are still reasonable for normal processing, but Digital Miner/Laser should be playtest watchpoints. |
| Mekanism energy conversion | FE/RF to Joules remains effectively the old 2.5 J per FE/RF scale. Current `maxEnergyPerSteam` is 10 vs old 100, so boiler/steam behavior is already lower than 1.12 in one key place. | Left unchanged; this is a modern Mekanism system difference and should be validated in-game before forcing old steam math. |
| Powah Energizing | Powah has no old E2 equivalent. Energizing recipes use fixed stored energy costs, e.g. Niotic Crystal 300k FE, Spirited Crystal 1M FE, Nitro Crystal 20M FE for 16. Energizing Rod transfer rates were not reduced, so the Powah generator nerf affects self-powered throughput but does not make recipes impossible. | Left Energizing costs and rod transfer rates unchanged. |
| Thermal machines | Current 1.20.1 Thermal machine base powers match the old E2 values that were already ported: Furnace/Sawmill/Pulverizer 30 RF/t, Smelter 40, Insolator 30, Centrifuge 20, Crucible 150, Refinery 20, Bottler 20, Crafter 20. Recipe energy multipliers are all 1.0. Early dynamos remain 40 RF/t, so one basic dynamo can sustain one early processing machine at base speed. | No further change. This does not appear hamstrung. |
| Ender IO machines | Current Ender IO main early consumers are equal or cheaper than old E2: Alloy Smelter 20 uI/t vs old 20 RF/t, SAG Mill 20 vs old 20, Stirling Generator 40 uI/t generation vs old base 20 RF/t. Current Soul Binder/Slicer/Powered Spawner are much cheaper than old nominal values. Photovoltaic rates are lower than old Ender IO/Endergy solar tiers, but that is passive solar only, not early Stirling-based progression. | No further change. Early Ender IO looks easier, not harder, on the energy side. |
| Actually Additions / Actually Subtractions machines | Current consumer constants match old 1.12 class constants: Powered Furnace 25 CF/t per slot, Crusher 40 CF/t, Canola Press 35 CF/t for 30 ticks, Vertical Digger 650 CF/block, Atomic Reconstructor normal shot 1000 CF and mining lens 60000 CF. Current upstream solid-fuel recipes were only 20 CF/t, below old E2's configured 30 CF/t and below current Thermal/Ender IO 40 RF/t solid-fuel generation. | Buffed Actually Subtractions solid-fuel recipes to 40 CF/t to sit with Thermal/Ender IO rather than below them. Restored the old E2 canola/refined oil curve at 40/80 CF/t, then improved upper-tier throughput without changing fuel density: crystallized oil is 36,000 CF over 225 ticks for 160 CF/t, and empowered oil is 64,000 CF over 200 ticks for 320 CF/t. This makes the canola chain a real midgame generator path while staying below the current 500 CF/t oil generator transfer cap. |
| Solid item-fuel generators | Thermal Stirling starts at 40 FE/t; its current upgrade BaseMod tiers are 2x/3x/4x, which map to roughly 80/120/160 FE/t. Current early item-burning spread after this pass: Integrated Dynamics Coal Generator 20; Powah Starter Furnator 20; Thermal/Ender IO/Actually Additions/Cyclic base solid fuel 40; Iron Furnaces copper/iron 80, silver/gold 110/120, diamond 140, emerald/crystal/obsidian 155/160/170, netherite 240. | Reduced Cyclic Fuel Generator from 80 to 40 FE/t. Added Iron Furnaces config and retuned Generator augment rates to copper 80, iron 80, silver 110, gold 120, diamond 140, emerald 155, crystal 160, obsidian 170, netherite 240. Rainbow is special-cased closer to its original behavior because it requires all eight normal furnaces to be running: generation is 1600 FE/t and `rainbow_generation` is 40000, down from defaults 2000 and 50000 but much higher than the normal furnace ladder. Allthemodium/Vibranium/Unobtainium remain at 480/960/1920. These settings affect rate only; regular Iron Furnaces fuel density remains hardcoded at `burn time * 20 FE`. Blasting generator recipes remain datapack-backed and can be adjusted separately if testing shows those item fuels are too strong. |
| NuclearCraft processors | Current processor drain is far below old E2 values. Old processors were commonly 1000-2000 RF/t; current processors are mostly 50 FE/t with longer base times. | No compensating generation increase needed for passive generator ports. |
| Immersive Petroleum machines | Pumpjack consumption/speed and distillation energy/time modifiers match the old active refining section: Pumpjack 1024 RF/t and 15 mB/t, Distillation energy/time 1.0. | No further change. |
| Draconic Evolution | Reactor output/fuel multipliers map directly. Tool and armor energy values are modern/internal-default based and are not consumers of the reactor loop in the same direct way. | No further change. |

## Verification

- JSON validation passed for the new OpenLoader datapack and Advanced Generators recipe overrides.
- Edited source files were synced to `Enigmatica 2 Ported` and byte-compared against the source pack copy.
