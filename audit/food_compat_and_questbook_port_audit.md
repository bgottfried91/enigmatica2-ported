# Food Compatibility and Questbook Port Audit

## Scope

- Food sources checked: Minecraft, Croptopia, MineColonies, Thermal Cultivation, and Tinkers' Construct.
- Questbook source checked: `../Enigmatica 2 - E2/config/betterquesting/DefaultQuests.json`.

## Croptopia Recipe Compatibility

Croptopia is already partly tag-driven. Its recipes frequently consume tags such as:

- `forge:cheeses`
- `forge:milks`
- `forge:butters`
- `forge:flour`
- `forge:doughs`
- `forge:salts`
- `forge:water_bottles`
- `forge:corn`
- `forge:rice`
- `forge:onions`
- `forge:garlic`
- `forge:tomatoes`
- `forge:lettuce`
- `forge:fruits`
- `forge:vegetables`
- `croptopia:beef_replacements`
- `croptopia:chicken_replacements`
- `croptopia:pork_replacements`
- `croptopia:meat_replacements`

This means the easiest compatibility path is to add equivalent food items from MineColonies, Thermal Cultivation, and Tinkers' Construct to the tags Croptopia already uses. This should make most Croptopia recipes accept those items without replacing the recipes.

Croptopia still hard-codes some ingredients. The most common direct item ingredients are vanilla staples or Croptopia-specific intermediates:

- `minecraft:sugar`
- `minecraft:egg`
- `minecraft:glass_bottle`
- `minecraft:bread`
- `minecraft:bowl`
- `minecraft:potato`
- `minecraft:beef`
- `minecraft:carrot`
- `minecraft:porkchop`
- `croptopia:pepper`
- `croptopia:cinnamon`
- `croptopia:whipping_cream`
- `croptopia:bacon`
- `croptopia:toast`
- `croptopia:peanut_butter`

If we want every equivalent food to work everywhere, tag additions alone will not be enough. The practical split should be:

1. Add cross-mod ingredients to Croptopia's existing tags.
2. Only rewrite recipes where a direct item blocks an important equivalent, such as bread/toast, eggs, bacon, or pepper.
3. Avoid rewriting recipe outputs or Croptopia's cooking tools unless a specific conflict appears in JEI.

## Suggested Tag Additions

### MineColonies

High-value additions:

- `minecolonies:butter` -> `forge:butters`
- `minecolonies:cheddar_cheese`, `minecolonies:feta_cheese`, `minecolonies:creamcheese` -> `forge:cheeses`
- `minecolonies:large_milk_bottle`, `minecolonies:large_soy_milk_bottle` -> `forge:milks`
- `minecolonies:tofu` -> `forge:tofu`, `croptopia:meat_replacements`
- `minecolonies:soysauce` -> `forge:soy_sauces`
- `minecolonies:tortillas` -> `forge:tortillas`
- `minecolonies:raw_noodle` -> `forge:noodles`
- `minecolonies:yogurt` -> `forge:yoghurts`
- `minecolonies:rice` -> `forge:rice`, `forge:grain/rice`, `forge:crops/rice`
- `minecolonies:corn` -> `forge:corn`, `forge:grain/corn`, `forge:crops/corn`
- `minecolonies:tomato` -> `forge:tomatoes`, `forge:vegetables/tomato`, `forge:crops/tomato`
- `minecolonies:onion` -> `forge:onions`, `forge:vegetables/onion`, `forge:crops/onion`
- `minecolonies:garlic` -> `forge:garlic`, `forge:vegetables/garlic`, `forge:crops/garlic`
- `minecolonies:cabbage` -> `forge:cabbage`, `forge:vegetables/cabbage`, `forge:crops/cabbage`
- `minecolonies:eggplant` -> `forge:eggplants`, `forge:vegetables/eggplant`, `forge:crops/eggplant`
- `minecolonies:bell_pepper` -> `forge:bellpeppers`, `forge:fruits/bellpepper`, `forge:crops/bellpepper`
- `minecolonies:soybean` -> `forge:soybeans`, `forge:vegetables/soybean`, `forge:crops/soybean`
- `minecolonies:butternut_squash` -> `forge:squashes`, `forge:vegetables/squash`, `forge:crops/squash`

Potential additions needing a balance/semantic call:

- `minecolonies:cornmeal` -> maybe `forge:flour`
- `minecolonies:bread_dough`, `minecolonies:muffin_dough`, etc. -> maybe `forge:doughs`, but these may be too specific.
- `minecolonies:peas`, `minecolonies:chickpea`, `minecolonies:durum`, `minecolonies:mint`, `minecolonies:nether_pepper` have no obvious Croptopia equivalent tag used broadly.

### Thermal Cultivation

Thermal already adds many `forge:crops/*` tags, but Croptopia recipes often use plural ingredient tags instead. Add Thermal crops to Croptopia-style tags:

- `thermal:barley` -> `forge:barley`
- `thermal:corn` -> `forge:corn`, `forge:grain/corn`
- `thermal:rice` -> `forge:rice`, `forge:grain/rice`
- `thermal:tomato` -> `forge:tomatoes`, `forge:vegetables/tomato`
- `thermal:onion` -> `forge:onions`, `forge:vegetables/onion`
- `thermal:eggplant` -> `forge:eggplants`, `forge:vegetables/eggplant`
- `thermal:bell_pepper` -> `forge:bellpeppers`, `forge:fruits/bellpepper`, `forge:crops/bellpepper`
- `thermal:green_bean` -> `forge:greenbeans`, `forge:vegetables/greenbean`, `forge:crops/greenbean`
- `thermal:spinach` -> `forge:spinach`, `forge:vegetables/spinach`
- `thermal:strawberry` -> `forge:strawberries`, `forge:fruits/strawberry`
- `thermal:peanut` -> `forge:peanuts`, `forge:nuts`
- `thermal:radish` -> `forge:radishes`, `forge:vegetables/radish`
- `thermal:hops` -> `forge:hops`
- `thermal:coffee` -> probably `forge:coffee_beans`
- `thermal:tea` -> probably `forge:tea_leaves`
- `thermal:cheese_wedge` -> `forge:cheeses`
- `thermal:peanut_butter` has no existing Croptopia `forge:peanut_butters` tag to hook into.

### Tinkers' Construct

Food-like TConstruct items found:

- `tconstruct:cheese_ingot`
- `tconstruct:bacon`
- `tconstruct:meat_soup`
- `tconstruct:mushroom_stew_bucket`
- `tconstruct:rabbit_stew_bucket`
- `tconstruct:meat_soup_bucket`

Recommended initial additions:

- `tconstruct:cheese_ingot` -> `forge:cheeses`
- `tconstruct:bacon` -> `croptopia:pork_replacements`

Do not tag the bucket soups into Croptopia recipe ingredients unless a specific recipe needs them; bucketed foods are not ingredient-equivalent to bowls of stew.

## Implementation Recommendation

Use a KubeJS item tag script, probably a new `kubejs/server_scripts/e2_tags_food_compat.js`, rather than recipe replacement as the first pass.

That keeps the change low-risk:

- no JEI recipe ID churn,
- no custom output behavior,
- no recipe ordering issues,
- easy to extend if another food mod is added later.

After that, check JEI for specific misses. If important recipes still reject obvious equivalents, handle those with targeted recipe replacements.

## BetterQuesting Port Notes

The old E2 source questbook is:

- `../Enigmatica 2 - E2/config/betterquesting/DefaultQuests.json`

Current stats:

- 25 quest lines
- 863 quest records
- Tasks are mostly `bq_standard:retrieval`
- Rewards are mostly `bq_standard:item`
- There are many `bq_standard:loot_chest` rewards

Task types found:

- `bq_standard:retrieval`: 866
- `bq_standard:checkbox`: 30
- `bq_standard:hunt`: 2
- `bq_standard:location`: 1

Reward types found:

- `bq_standard:item`: 806
- `bq_standard:choice`: 95
- `bq_standard:command`: 16
- `bq_standard:xp`: 11

Major reward/task namespaces that will need migration or deletion:

- `harvestcraft`
- `thaumcraft`
- `extrautils2`
- `ic2`
- `thermalexpansion`
- `thermaldynamics`
- `thermalfoundation`
- `enderio`
- `forestry`
- `advancedrocketry`
- `libvulpes`
- `actuallyadditions`
- `environmentaltech`
- `ancientwarfare*`

Recommended port process:

1. Generate an item namespace audit from `DefaultQuests.json`.
2. Create an ID mapping table for mods that still exist under new IDs, such as AE2, Thermal, Mekanism, Botania, Blood Magic, Immersive Engineering, TConstruct, NuclearCraft, and RFTools.
3. Mark rewards from removed mods as one of: delete, replace with modern equivalent, or replace with loot chest.
4. Convert quests mechanically after the mapping table exists.
5. Review quest text and chapter flow manually, because many descriptions reference 1.12 mechanics or removed mods.
6. Rebuild reward loot tables separately, likely with fewer low-value random rewards.

The questbook looks portable, but rewards should be treated as a redesign pass, not a blind conversion.
