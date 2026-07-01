# Apotheosis Config Port Notes

Generated as a continuation artifact for config value porting.

## File Mapping

- `adventure.cfg`: new
- `apotheosis.cfg`: old, new
- `deadly.cfg`: old
- `ench.cfg`: new
- `enchantability.cfg`: old
- `enchantment_module.cfg`: old
- `enchantments.cfg`: old, new
- `garden.cfg`: old, new
- `names.cfg`: old, new
- `potion.cfg`: old, new
- `spawner.cfg`: old, new
- `village.cfg`: new

Notable rename: old `deadly.cfg` appears to be represented by new `adventure.cfg`; old `enchantment_module.cfg` appears to be represented by new `ench.cfg`. New `village.cfg` has no 1.12 counterpart.

## spawner.cfg -> spawner.cfg

- Parsed old scalar values: 42
- Parsed new scalar values: 3
- Same key/value pairs: 1
- Same key but changed value/type: 0
- Old-only scalar keys: 41
- New-only scalar keys: 2

Initial finding: old E2 spawner scalar values largely match the new defaults for fields that still exist. Do not blindly port old modifier sections; Apotheosis 1.20 uses a different spawner modifier model and most old modifier item/value sections are gone from the generated new file.

Old-only keys sample:
- `general.Inverse Item` = `minecraft:quartz`
- `ignore_spawn_cap.item` = `minecraft:chorus_fruit`
- `ignore_spawn_cap.max_value` = `2147483647`
- `ignore_spawn_cap.min_value` = `0`
- `ignore_spawn_cap.value` = `0`
- `ignore_spawn_conditions.item` = `minecraft:dragon_egg`
- `ignore_spawn_conditions.max_value` = `2147483647`
- `ignore_spawn_conditions.min_value` = `0`
- `ignore_spawn_conditions.value` = `0`
- `max_delay.item` = `minecraft:clock`
- `max_delay.max_value` = `2147483647`
- `max_delay.min_value` = `0`
- `max_delay.value` = `-10`
- `max_nearby_entities.item` = `minecraft:ghast_tear`
- `max_nearby_entities.max_value` = `2147483647`
- `max_nearby_entities.min_value` = `0`
- `max_nearby_entities.value` = `2`
- `min_delay.item` = `minecraft:sugar`
- `min_delay.max_value` = `2147483647`
- `min_delay.min_value` = `0`
- `min_delay.value` = `-5`
- `player_activation_range.item` = `minecraft:prismarine_crystals`
- `player_activation_range.max_value` = `2147483647`
- `player_activation_range.min_value` = `0`
- `player_activation_range.value` = `2`
- `redstone_control.item` = `minecraft:comparator`
- `redstone_control.max_value` = `2147483647`
- `redstone_control.min_value` = `0`
- `redstone_control.value` = `0`
- `require_players.item` = `minecraft:nether_star`

New-only keys sample:
- `general.Enable Capturing Enchantment JEI Info` = `true`
- `general.Spawner Silk Damage` = `100`

## garden.cfg -> garden.cfg

- Parsed old scalar values: 2
- Parsed new scalar values: 3
- Same key/value pairs: 2
- Same key but changed value/type: 0
- Old-only scalar keys: 0
- New-only scalar keys: 1

New-only keys sample:
- `general.Bamboo Height` = `32`

## potion.cfg -> potion.cfg

- Parsed old scalar values: 1
- Parsed new scalar values: 1
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 1
- New-only scalar keys: 1

Old-only keys sample:
- `general.Knowledge XP Multiplier` = `10`

New-only keys sample:
- `general.Restrict Charms to Curios` = `false`

## enchantments.cfg -> enchantments.cfg

- Parsed old scalar values: 356
- Parsed new scalar values: 999
- Same key/value pairs: 101
- Same key but changed value/type: 34
- Old-only scalar keys: 221
- New-only scalar keys: 864

Changed same-name keys:
- `"apotheosis:capturing".Max Level`: old `I=14` -> new `I=7`
- `"apotheosis:icy_thorns".Max Level`: old `I=7` -> new `I=5`
- `"apotheosis:knowledge".Max Level`: old `I=9` -> new `I=3`
- `"apotheosis:life_mending".Max Level`: old `I=4` -> new `I=3`
- `"apotheosis:natures_blessing".Max Level`: old `I=13` -> new `I=7`
- `"apotheosis:rebounding".Max Level`: old `I=18` -> new `I=5`
- `"apotheosis:reflective".Max Level`: old `I=10` -> new `I=7`
- `"apotheosis:shield_bash".Max Level`: old `I=15` -> new `I=7`
- `"apotheosis:splitting".Max Level`: old `I=16` -> new `I=1`
- `"enderio:repellent".Max Level`: old `I=18` -> new `I=11`
- `"minecraft:bane_of_arthropods".Max Level`: old `I=21` -> new `I=10`
- `"minecraft:blast_protection".Max Level`: old `I=23` -> new `I=9`
- `"minecraft:depth_strider".Max Level`: old `I=17` -> new `I=7`
- `"minecraft:efficiency".Max Level`: old `I=14` -> new `I=9`
- `"minecraft:feather_falling".Max Level`: old `I=30` -> new `I=11`
- `"minecraft:fire_aspect".Max Level`: old `I=14` -> new `I=5`
- `"minecraft:fire_protection".Max Level`: old `I=22` -> new `I=9`
- `"minecraft:fortune".Max Level`: old `I=14` -> new `I=8`
- `"minecraft:frost_walker".Max Level`: old `I=17` -> new `I=7`
- `"minecraft:knockback".Max Level`: old `I=14` -> new `I=5`
- `"minecraft:looting".Max Level`: old `I=14` -> new `I=8`
- `"minecraft:luck_of_the_sea".Max Level`: old `I=14` -> new `I=8`
- `"minecraft:lure".Max Level`: old `I=14` -> new `I=8`
- `"minecraft:mending".Max Level`: old `I=6` -> new `I=1`
- `"minecraft:power".Max Level`: old `I=18` -> new `I=9`
- `"minecraft:projectile_protection".Max Level`: old `I=31` -> new `I=11`
- `"minecraft:protection".Max Level`: old `I=17` -> new `I=8`
- `"minecraft:punch".Max Level`: old `I=9` -> new `I=5`
- `"minecraft:respiration".Max Level`: old `I=16` -> new `I=7`
- `"minecraft:sharpness".Max Level`: old `I=16` -> new `I=9`
- `"minecraft:smite".Max Level`: old `I=21` -> new `I=10`
- `"minecraft:sweeping".Max Level`: old `I=20` -> new `I=8`
- `"minecraft:thorns".Max Level`: old `I=14` -> new `I=5`
- `"minecraft:unbreaking".Max Level`: old `I=14` -> new `I=8`

### Ported Max Level Values

Ported the old E2 `Max Level` values for enchantments that still exist in the current 1.20 config:

- Apotheosis/Ender IO: `apotheosis:capturing`, `apotheosis:icy_thorns`, `apotheosis:knowledge`, `apotheosis:life_mending`, `apotheosis:natures_blessing`, `apotheosis:rebounding`, `apotheosis:reflective`, `apotheosis:shield_bash`, `apotheosis:splitting`, `enderio:repellent`.
- Vanilla: `minecraft:protection`, `minecraft:fire_protection`, `minecraft:feather_falling`, `minecraft:blast_protection`, `minecraft:projectile_protection`, `minecraft:respiration`, `minecraft:thorns`, `minecraft:depth_strider`, `minecraft:frost_walker`, `minecraft:sharpness`, `minecraft:smite`, `minecraft:bane_of_arthropods`, `minecraft:knockback`, `minecraft:fire_aspect`, `minecraft:looting`, `minecraft:sweeping`, `minecraft:efficiency`, `minecraft:unbreaking`, `minecraft:fortune`, `minecraft:power`, `minecraft:punch`, `minecraft:luck_of_the_sea`, `minecraft:lure`, `minecraft:mending`.

Only `Max Level` was ported. New 1.20 fields such as `Max Loot Level`, `Discoverable`, `Lootable`, `Tradeable`, `Treasure`, and `Rarity` were left at current generated values because old E2 did not expose the same controls.

Removed-mod enchantments from old E2 were not recreated.

Old-only keys sample:
- `"advancedrocketry:spacebreathing".Max Level` = `18`
- `"advancedrocketry:spacebreathing".Max Power Function` = ``
- `"advancedrocketry:spacebreathing".Min Level` = `1`
- `"advancedrocketry:spacebreathing".Min Power Function` = ``
- `"apotheosis:berserk".Max Level` = `6`
- `"apotheosis:berserk".Max Power Function` = ``
- `"apotheosis:berserk".Min Level` = `1`
- `"apotheosis:berserk".Min Power Function` = ``
- `"apotheosis:capturing".Min Level` = `1`
- `"apotheosis:depth_miner".Max Level` = `12`
- `"apotheosis:depth_miner".Max Power Function` = ``
- `"apotheosis:depth_miner".Min Level` = `1`
- `"apotheosis:depth_miner".Min Power Function` = ``
- `"apotheosis:hell_infusion".Max Level` = `13`
- `"apotheosis:hell_infusion".Max Power Function` = ``
- `"apotheosis:hell_infusion".Min Level` = `1`
- `"apotheosis:hell_infusion".Min Power Function` = ``
- `"apotheosis:icy_thorns".Min Level` = `1`
- `"apotheosis:knowledge".Min Level` = `1`
- `"apotheosis:life_mending".Min Level` = `1`
- `"apotheosis:magic_protection".Max Level` = `6`
- `"apotheosis:magic_protection".Max Power Function` = ``
- `"apotheosis:magic_protection".Min Level` = `1`
- `"apotheosis:magic_protection".Min Power Function` = ``
- `"apotheosis:mounted_strike".Max Level` = `16`
- `"apotheosis:mounted_strike".Max Power Function` = ``
- `"apotheosis:mounted_strike".Min Level` = `1`
- `"apotheosis:mounted_strike".Min Power Function` = ``
- `"apotheosis:natures_blessing".Min Level` = `1`
- `"apotheosis:rebounding".Min Level` = `1`

New-only keys sample:
- `"apotheosis:bane_of_illagers".Discoverable` = `true`
- `"apotheosis:bane_of_illagers".Lootable` = `true`
- `"apotheosis:bane_of_illagers".Max Level` = `10`
- `"apotheosis:bane_of_illagers".Max Loot Level` = `5`
- `"apotheosis:bane_of_illagers".Max Power Function` = ``
- `"apotheosis:bane_of_illagers".Min Power Function` = ``
- `"apotheosis:bane_of_illagers".Rarity` = `UNCOMMON`
- `"apotheosis:bane_of_illagers".Tradeable` = `true`
- `"apotheosis:bane_of_illagers".Treasure` = `false`
- `"apotheosis:berserkers_fury".Discoverable` = `true`
- `"apotheosis:berserkers_fury".Lootable` = `true`
- `"apotheosis:berserkers_fury".Max Level` = `3`
- `"apotheosis:berserkers_fury".Max Loot Level` = `3`
- `"apotheosis:berserkers_fury".Max Power Function` = ``
- `"apotheosis:berserkers_fury".Min Power Function` = ``
- `"apotheosis:berserkers_fury".Rarity` = `VERY_RARE`
- `"apotheosis:berserkers_fury".Tradeable` = `true`
- `"apotheosis:berserkers_fury".Treasure` = `false`
- `"apotheosis:capturing".Discoverable` = `true`
- `"apotheosis:capturing".Lootable` = `true`
- `"apotheosis:capturing".Max Loot Level` = `5`
- `"apotheosis:capturing".Rarity` = `VERY_RARE`
- `"apotheosis:capturing".Tradeable` = `true`
- `"apotheosis:capturing".Treasure` = `false`
- `"apotheosis:chainsaw".Discoverable` = `true`
- `"apotheosis:chainsaw".Lootable` = `true`
- `"apotheosis:chainsaw".Max Level` = `1`
- `"apotheosis:chainsaw".Max Loot Level` = `1`
- `"apotheosis:chainsaw".Max Power Function` = ``
- `"apotheosis:chainsaw".Min Power Function` = ``

## enchantment_module.cfg -> ench.cfg

- Parsed old scalar values: 4
- Parsed new scalar values: 2
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 4
- New-only scalar keys: 2

Old-only keys sample:
- `general.Enable Cobwebs` = `true`
- `general.Item Merging` = `false`
- `general.Max Normal Power` = `20.0`
- `general.Max Power` = `75.0`

New-only keys sample:
- `client.Sculkshelf Noise Chance` = `200`
- `client.Show Enchanted Book Metadata` = `true`

## deadly.cfg -> adventure.cfg

- Parsed old scalar values: 451
- Parsed new scalar values: 14
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 451
- New-only scalar keys: 14

Old-only keys sample:
- `"random spawners".ancientwarfarenpc:aw_npc_bard` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_combat` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_courier` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_priest` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_siege_engineer` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_trader` = `1`
- `"random spawners".ancientwarfarenpc:aw_npc_worker` = `1`
- `"random spawners".ancientwarfarenpc:faction.archer` = `1`
- `"random spawners".ancientwarfarenpc:faction.archer.elite` = `1`
- `"random spawners".ancientwarfarenpc:faction.bard` = `1`
- `"random spawners".ancientwarfarenpc:faction.cavalry` = `1`
- `"random spawners".ancientwarfarenpc:faction.civilian.female` = `1`
- `"random spawners".ancientwarfarenpc:faction.civilian.male` = `1`
- `"random spawners".ancientwarfarenpc:faction.leader` = `1`
- `"random spawners".ancientwarfarenpc:faction.leader.elite` = `1`
- `"random spawners".ancientwarfarenpc:faction.mounted_archer` = `1`
- `"random spawners".ancientwarfarenpc:faction.priest` = `1`
- `"random spawners".ancientwarfarenpc:faction.siege_engineer` = `1`
- `"random spawners".ancientwarfarenpc:faction.soldier` = `1`
- `"random spawners".ancientwarfarenpc:faction.soldier.elite` = `1`
- `"random spawners".ancientwarfarenpc:faction.spellcaster` = `1`
- `"random spawners".ancientwarfarenpc:faction.trader` = `1`
- `"random spawners".animania:buck_alpine` = `1`
- `"random spawners".animania:buck_angora` = `1`
- `"random spawners".animania:buck_chinchilla` = `1`
- `"random spawners".animania:buck_cottontail` = `1`
- `"random spawners".animania:buck_dutch` = `1`
- `"random spawners".animania:buck_fainting` = `1`
- `"random spawners".animania:buck_havana` = `1`
- `"random spawners".animania:buck_jack` = `1`

New-only keys sample:
- `affixes.Cleave Players` = `false`
- `affixes.Disable Quark Tooltips for Affix Items` = `true`
- `affixes.Gem Boss Bonus` = `0.33`
- `affixes.Gem Drop Chance` = `0.045`
- `affixes.Random Affix Chance` = `0.075`
- `affixes.Torch Placement Item` = `minecraft:torch`
- `bosses.Boss Announce Ignore Y` = `false`
- `bosses.Boss Announce Range` = `96.0`
- `bosses.Boss Announce Volume` = `0.75`
- `bosses.Boss Auto-Aggro` = `false`
- `bosses.Boss Glowing On Spawn` = `true`
- `bosses.Boss Spawn Cooldown` = `3600`
- `bosses.Curse Boss Items` = `false`
- `spawners.Spawner Value Chance` = `0.11`

## apotheosis.cfg -> apotheosis.cfg

- Parsed old scalar values: 6
- Parsed new scalar values: 7
- Same key/value pairs: 4
- Same key but changed value/type: 0
- Old-only scalar keys: 2
- New-only scalar keys: 3

Old-only keys sample:
- `client.Enchantment Tooltips` = `true`
- `general.Enable Deadly Module` = `true`

New-only keys sample:
- `general.Enable Adventure Module` = `true`
- `general.Enable Village Module` = `true`
- `general.Give Book on First Join` = `true`

## names.cfg -> names.cfg

- Parsed old scalar values: 0
- Parsed new scalar values: 2
- Same key/value pairs: 0
- Same key but changed value/type: 0
- Old-only scalar keys: 0
- New-only scalar keys: 2

New-only keys sample:
- `formatting.Ownership Format` = `%s's`
- `formatting.Suffix Format` = `%s the %s`

## Recommended Next Apotheosis Steps

1. Inspect `adventure.cfg` manually against old `deadly.cfg`; this likely contains the most pack-impacting combat/affix/boss tuning.
2. Inspect `ench.cfg` against old `enchantment_module.cfg`; watch for changed names around enchantment caps, anvil behavior, and bookshelf mechanics.
3. Treat `spawner.cfg` as probably acceptable at generated defaults unless E2 intentionally changed a modifier value not represented in 1.20.
4. Do not port old-only keys unless a semantically equivalent key exists in the new file.
