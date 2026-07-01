# Config Porting Handoff

Current date: 2026-06-25

## Current State

- Packwiz source: `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1`
- Live test instance: `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)`
- Original E2 1.12 instance: `/mnt/i/minecraft/Instances/Enigmatica 2 - E2`
- Packwiz now tracks a curated generated config baseline:
  - `config/`: 500 files
  - `defaultconfigs/`: 29 files
- `packwiz refresh` has been run after the config/defaultconfig import.
- `audit/config_porting_inventory.md` records the 1.12 -> 1.20 config family mapping.
- KubeJS static audit is clean: 0 errors, 0 warnings, 0 info.

## Important Decisions Already Made

- Do not blindly ship every generated config.
- Ship gameplay/progression/worldgen/integration configs in `config/`.
- Ship Forge per-world server configs in `defaultconfigs/`.
- Do not ship client/user preference configs unless intentionally desired.
- Do not ship generated/cache/user files:
  - `*.bak`
  - `contributors.json`
  - `contributors.json.etag`
  - `hud_settings.json`
  - `pregen_seeds.json`
  - JEI per-world lookup history
- Better Questing opens but has no authored quests. This is expected/unported, not caused by config baseline work.
  - Old 1.12 files exist:
    - `config/betterquesting/DefaultQuests.json`
    - `config/betterquesting/DefaultLoot.json`
  - New BQ 1.20 uses `.xbt` world/default databases, so quest content is a separate port/import task.

## Verification Already Completed

- Live instance launched successfully after config import.
- New world was created successfully.
- Major mods appear in JEI.
- Ore Excavation keybind is set properly.
- Quest book opens, but content is empty because quests are not ported.
- Post-launch managed config diff:
  - Packwiz `config/` vs live `config/`: 0 missing, 0 changed for tracked files.
  - Packwiz `defaultconfigs/` vs latest world `serverconfig/`: 0 missing, 0 changed.

## Generated Audit Tools

- `tools/audit/audit_config_porting.py`
  - Regenerates `audit/config_porting_inventory.md`.
  - Current summary:
    - Original E2 config files: 921
    - Active 1.20.1 instance config files: 700
    - Packwiz tracked config files: 500
    - Packwiz tracked defaultconfigs files: 29
    - Likely current counterpart families: 93
    - Installed mods with no matching generated config: 13
    - Likely removed config families: 118
    - Manual/unclear config families: 3
- `tools/audit/audit_kubejs_static.py`
  - Static KubeJS audit; currently clean.
- `tools/audit/compare_config_scalars.py`
  - Helper for generating coarse old-vs-new scalar config notes.
  - Useful for `.cfg`/`.toml` files, but noisy when config schemas were renamed or split.

## Value Porting Started

Artifacts created:

- `audit/apotheosis_config_port_notes.md`
- `audit/building_reactor_config_port_notes.md`
- `audit/core_mod_config_port_notes.md`
- `audit/incontrol_config_port_notes.md`
- `audit/lostcities_config_port_notes.md`
- `audit/mekanism_config_port_notes.md`
- `audit/nuclearcraft_config_port_notes.md`
- `audit/utility_config_port_notes.md`

Actual config edit made:

- `config/Mekanism/general.toml`
  - Changed `allowChunkloading = true` to `allowChunkloading = false`.
  - Reason: old E2 1.12 `mekanism.cfg` had `AllowChunkloading=false`, so this preserves old pack behavior for Mekanism anchor upgrades.
- `config/Mekanism/general.toml`
  - Changed `digital_miner.silkMultiplier = 12` to `5`.
  - Reason: old E2 1.12 `mekanism.cfg` had `MinerSilkMultiplier=5`.
- `config/NuclearCraft/fission.toml`
  - Changed `fission_reactor.max_size = 26` to `24`.
  - Changed `fission_reactor.reactor_explosion_radius = 4.0` to `0.0`.
  - Reason: old E2 1.12 `nuclearcraft.cfg` had `fission_max_size=24` and `fission_explosions=false`.
- `config/NuclearCraft/fusion.toml`
  - Changed `fusion_reactor.max_size = 32` to `24`.
  - Changed `fusion_reactor.reactor_explosion_radius = 2.0` to `0.0`.
  - Reason: old E2 1.12 `nuclearcraft.cfg` had `fusion_max_size=24`; old fusion meltdowns did not expose a separate explosion toggle.
- `config/NuclearCraft/ore_generation.toml`
  - Changed all current ore entries from `register = true` to `false`.
  - Reason: old E2 1.12 `nuclearcraft.cfg` disabled all NuclearCraft native ore generation and relied on centralized worldgen handling.
- `config/NuclearCraft/world.toml`
  - Changed `Dimension.wasteland = true` to `false`.
  - Reason: old E2 1.12 `nuclearcraft.cfg` had `wasteland_dimension_gen=false`.
- `config/NuclearCraft/radiation.toml`
  - Changed `radiation.enabled = true` to `false`.
  - Reason: old E2 1.12 `nuclearcraft.cfg` had `radiation_enabled=false`.
- `config/oreexcavation-common.toml`
  - Changed `Limit = 128` to `512`.
  - Changed `Range = 16` to `24`.
  - Changed `"Open Hand" = true` to `false`.
  - Changed `"Max Undos" = 3` to `1`.
  - Reason: preserve old E2 1.12 `oreexcavation.cfg` behavior.
- `config/tconstruct-common.toml`
  - Changed `shouldSpawnWithTinkersBook = true` to `false`.
  - Reason: old E2 1.12 `tconstruct.cfg` had `spawnWithBook=false`.
  - Deferred ore melting rates because TiC 1.20 uses separate melter/smeltery/foundry rates instead of old E2's single `oreToIngotRatio=2.0`.
- `config/tleveling/common.toml`
  - No edit. Current `levelupExpRequired = 200` and `modifierLevelGap = 3` preserve the old E2 default base XP and new-tool modifier cadence where the schema still maps.
  - Old per-tool XP entries do not map directly to current TiC 1.20 tool IDs/formula config.
- JAOPCA cleanup:
  - Set `materialBlacklist = ["*"]` in:
    - `config/jaopca/modules/storage_blocks.toml`
    - `config/jaopca/modules/raw_storage_blocks.toml`
    - `config/jaopca/modules/bloodmagic.toml`
    - `config/jaopca/modules/bloodmagic_compat.toml`
    - `config/jaopca/modules/mekanism.toml`
    - `config/jaopca/modules/mekanism_compat.toml`
    - `config/jaopca/modules/mekanism_non_ingot.toml`
  - Set `config/jaopca/modules/molten.toml` `materialBlacklist = ["*", "coal"]`.
  - Set `config/jaopca/modules/dusts.toml` `materialBlacklist = ["black_quartz"]`.
  - Set `config/jaopca/modules/nuggets.toml` `materialBlacklist = ["hellforged"]`.
  - Reason: current live logs show missing JAOPCA generated models concentrated in storage blocks, raw storage blocks, Blood Magic gravel/fragments, Mekanism processing forms, and molten forms. `molten.coal` is temporarily preserved because `kubejs/server_scripts/e2_recipes_tinkers_construct.js` directly references `jaopca:molten.coal`.
- `config/pneumaticcraft-common.toml`
  - Set `Worldgen.oil_world_gen_dimension_blacklist = ["minecraft:the_end", "minecraft:the_nether"]` from old E2 `oilWorldGenBlacklist = [1, -1]`.
  - Changed `elevator_base_blocks_per_base = 6` to `4`.
  - Changed `jet_boots_air_usage = 12` to `6`.
  - Changed `freezing_ammo_block_ice_chance = 10` to `20`.
  - Changed `mek_thermal_resistance_factor = 5.0` to `100.0`.
  - Changed `mek_thermal_conversion_efficiency = 0.01` to `0.2`.
  - Reason: direct semantic mappings from old E2 `pneumaticcraft.cfg`.
- `config/industrialforegoing/machine-resource-production.toml`
  - Changed `MachineResourceProductionConfig.LaserDrillConfig.powerPerOperation = 1000` to `20000`.
  - Reason: old E2 1.12 intentionally raised Industrial Foregoing `laser_drill.energyForWork` from its default `3000` to `20000`; the 1.20 config still exposes the laser drill operation energy cost.
  - No other Industrial Foregoing edits were made. Direct old values for Mob Duplicator exact-copy/essence, Wither Builder operation cost, Biofuel Generator output, and laser base work were already matched; many old machine energy buffer/input-rate keys no longer map cleanly.
- `config/enderio/base-common.toml`
  - Changed `items.travelling.blinkRange = 24` to `16`.
  - Changed `items.travelling.itemToBlockRange = 192` to `256`.
  - Reason: direct mappings from old E2 `travelStaffMaxBlinkDistance = 16` / `defaultTeleportRangeItem = 16` and `travelStaffMaxDistance = 256` / `defaultTeleportRangeItemToBlock = 256`.
  - No other Ender IO edits were made. Current Grains of Infinity, Enderios teleport food, magnet, and exposed powered-spawner values already match old E2 defaults where the 1.20 config still exposes them. Removed 1.12 modules such as conduits, Endergy, inventory panel, and most machine-specific tuning were not ported.
- `defaultconfigs/thermal-server.toml`
  - Changed tool base capacities to old E2 values where names still map:
    - Fluxbore/Drill `50000` -> `40000`
    - Fluxsaw/Saw `50000` -> `40000`
    - Flux Capacitor `500000` -> `1000000`
    - FluxoMagnet `50000` -> `40000`
    - Reservoir `20000` -> `10000`
    - Potion Infuser/Hypoinfuser `4000` -> `2000`
    - Potion Quiver fluid capacity `4000` -> `2000`
  - Changed machine base power to old E2 values where the same machine concept exists:
    - Furnace `20` -> `30`
    - Sawmill `20` -> `30`
    - Pulverizer `20` -> `30`
    - Smelter `20` -> `40`
    - Insolator `20` -> `30`
    - Crucible `80` -> `150`
  - Changed dynamo base power to old E2 values where the same dynamo role exists:
    - Numismatic `40` -> `60`
    - Lapidary `40` -> `60`
  - Reason: old E2 set Numismatic Dynamo to `60`; modern Thermal splits the old coin/gem behavior into Numismatic and Lapidary, and Lapidary is treated as the 1.20 successor to old `thermalexpansion.numismatic_gem`.
  - Left other current-only/renamed dynamos and machines at current values unless the 1.12 mapping was direct.
- `kubejs/server_scripts/e2_recipes_thermal_dynamo_fuels.js`
  - Removes current `thermal:lapidary_fuel` recipes and replaces them with an explicit E2-style Lapidary table.
  - Restores old high-value gem fuel balance where direct equivalents exist:
    - Quartz `40000`
    - Lapis `80000`
    - Prismarine `150000`
    - Emerald/Amethyst/Ruby/Sapphire `200000`
    - Diamond `1200000`
    - Redstone Arsenal Flux Gem `1500000`
  - Adds current-pack replacement gems at similar tiers for lost BoP/old mod gems, including AE2, Ars Nouveau, Psi, Twilight Forest, Ender IO, and Botania gems.
  - Details captured in `audit/thermal_dynamo_fuel_parity.md`.
- `kubejs/server_scripts/e2_recipes_thermal_bottler.js`
  - Adds Thermal Bottler replacements for old Redstone Arsenal + Thermal Expansion Fluid Transposer integration recipes:
    - `#forge:dusts/electrum` + 500 mB `thermal:redstone` -> `redstone_arsenal:flux_dust`
    - `#forge:gems/diamond` + 500 mB `thermal:redstone` -> `redstone_arsenal:flux_gem`
  - Current Thermal already has the required `thermal:redstone` production via Magma Crucible.
  - Details captured in `audit/thermal_transposer_port.md`.
- `config/ae2/common.json`
  - Reviewed; no edit made.
  - Current exposed values already match old E2 for formation plane entity limit, crafting CPU calculation time, wireless terminal/staff/matter cannon energy capacities, wireless range/cost curve, and spatial IO power constants.
  - Old certus quartz ore generation settings do not exist in the current AE2 config and were handled during the datapack/worldgen pass instead.
- `config/lostcities/profiles/*.json`
  - Ported old E2 Lost Cities profile density/damage values where profile names still map directly:
    - `default`, `wasteland`, `safe`, `atlantis`, `rarecities`, `onlycities`, `tallbuildings`, `nodamage`, `ancient`, `cavern`, `space`, and `biosphere`.
  - Left current-only profiles (`largecities`, `void_outside`, `biosphere_caves`) at generated values.
  - Left old profiles without direct current files (`chisel`, `realistic`, `waterbubbles`, `water_empty`) unported.
  - Details captured in `audit/lostcities_config_port_notes.md`.
- `config/apotheosis/enchantments.cfg`
  - Ported old E2 `Max Level` values for current matching vanilla, Apotheosis, and Ender IO enchantments.
  - Left current 1.20 fields such as `Max Loot Level`, rarity, treasure/trade flags, and new-only enchantments at generated values.
  - Details captured in `audit/apotheosis_config_port_notes.md`.
- Utility config batch:
  - `config/integrateddynamics-common.toml`
    - Set Integrated Dynamics manual `obtainOnSpawn = false`.
    - Restored old E2 energy battery scale: `capacity = 100000`, `maxCreativeCapacity = 4096000`, `maxCreativeTabCapacity = 65536000`.
  - `config/modularrouters-common.toml`
    - Restored old E2 extruder ranges and disabled placer particles.
  - `config/functionalstorage/functionalstorage-common.toml`
    - Set controller linking range `8` -> `12` to preserve old Storage Drawers controller range.
  - `config/farmingforblockheads-common.toml`
    - Set `feedingTroughMaxAnimals = 8`.
  - `config/cookingforblockheads-common.toml`
    - Set `cowJarMilkPerTick = 0.5`.
  - Details captured in `audit/utility_config_port_notes.md`.
- Building/reactor/misc config batch:
  - `config/extremereactors/common.toml`
    - Restored old E2 fuel/reactor/turbine balance where keys still map.
    - Disabled native Extreme Reactors ore generation to preserve centralized ore/worldgen handling.
  - `config/carryon-common.toml`
    - Set `maxEntityHeight = 1.5`.
  - `config/chisel-common.toml`
    - Restored old E2 chisel durability values and iron chisel left-click behavior.
  - `config/psi-common.toml`
    - Restored old E2 `cadHarvestLevel = 2` and `spellCacheSize = 100`.
  - Details captured in `audit/building_reactor_config_port_notes.md`.
- `packwiz refresh` has been run after config edits.

## Recommended Next Work

Start value porting. For each mod family:

1. Compare old 1.12 config values against the new tracked 1.20 config(s).
2. Port only values that still represent useful pack intent.
3. Avoid forcing obsolete settings into new configs.
4. After edits, run `packwiz refresh`.
5. Launch or reload if the mod requires runtime validation.

High-impact order:

1. Apotheosis
2. Mekanism
3. NuclearCraft
4. In Control
5. Biomes O Plenty / Lost Cities / worldgen
6. Ore Excavation
7. TConstruct / Tinkers Tool Leveling
8. JAOPCA / material unification
9. Thermal / CoFH
10. PneumaticCraft, Industrial Foregoing, Ender IO

## Known Log Issues To Track Separately

These appeared in the latest live-instance log and are not solved by the config baseline:

- Better Questing has no authored quest database.
- MineColonies built-in quest JSONs log parsing errors for `minecolonies:delivery`; this appears to be MineColonies internal data, not BQ content.
- JER logs biome/registry errors around NuclearCraft wasteland.
- Ender IO model loader `athena:athena` errors.
- Advanced Generators bucket model loader `forge:bucket` errors.
- Some NuclearCraft/JAOPCA fluid tag errors exist and should be triaged during material unification.

## Manual/Unclear Config Families

From `audit/config_porting_inventory.md`, only these remain unmapped:

- `acronym/base/General.cfg`
- `chiselsandbits_clipboard.cfg`
- `fw.cfg`

These are low priority unless a specific feature is missing.

## Suggested Claude Starting Point

Run:

```bash
cd /mnt/i/minecraft/Instances/Enigmatica2-1.20.1
python3 tools/audit/audit_config_porting.py
python3 tools/audit/audit_kubejs_static.py
```

Then start with Apotheosis:

- Old: `/mnt/i/minecraft/Instances/Enigmatica 2 - E2/config/apotheosis/`
- New: `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1/config/apotheosis/`

Look for values related to:

- spawner behavior
- enchantment caps/limits
- deadly/adventure boss/module tuning
- garden crop behavior
- potion behavior
- whether features were disabled in E2 1.12

Do not assume key names are stable between 1.12 and 1.20.

After Apotheosis, review the newly generated notes:

- Mekanism: only clear edit so far is already applied. Remaining candidates are Digital Miner silk multiplier and worldgen, but those need balance review.
- In Control: old `spawn.json` had numeric dimension deny rules and Quark frog/foxhound caps. Do not copy directly; map current dimension/entity IDs first.
- NuclearCraft: config was heavily split in 1.20. Start with world/ore generation and material/fluid tag errors before reactor balance.
