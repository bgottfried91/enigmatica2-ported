# In Control Config Port Notes

Generated continuation artifact for config value porting.

## File State

Old E2 1.12:

- `incontrol/experience.json`: empty `[]`
- `incontrol/loot.json`: empty `[]`
- `incontrol/potentialspawn.json`: empty `[]`
- `incontrol/spawn.json`: non-empty
- `incontrol/summonaid.json`: empty `[]`
- `incontrol/main.cfg`: old config file, no direct 1.20 JSON counterpart

New 1.20 Packwiz baseline:

- `config/incontrol/*.json` files are all empty `[]`.
- `defaultconfigs/incontrol-server.toml` is tracked for newly created worlds.

## Old Rules Found

Old `spawn.json` had:

- A deny rule for a long list of numeric dimensions:
  - `-2`, `100` through `150` with several gaps.
- A deny rule for `quark:frog` with `"mincount": "20"`.
- A deny rule for `quark:foxhound` with `"mincount": "20"`.

## Porting Guidance

Do not blindly copy the old `spawn.json`.

Reasons:

- 1.12 numeric dimension IDs do not map directly to 1.20 resource-location dimensions.
- Many old dimensions were probably RFTools/void/legacy dimensions that no longer exist or have renamed IDs.
- Quark entity IDs may have changed or the mobs may not exist in the same form in the 1.20 Quark version.
- In Control's schema may differ in 1.20; validate against current mod docs or generated examples before applying rules.

Recommended next steps:

1. Decide whether the old dimension-deny rule still has pack intent. It likely prevented hostile spawns in machine/utility/void dimensions.
2. Map that intent to actual current dimensions, not old IDs. Candidate dimensions visible in generated config/logs include:
   - `minecraft:overworld`
   - `minecraft:the_nether`
   - `minecraft:the_end`
   - `compactmachines:compact_world`
   - `lostcities:lostcity`
   - `nuclearcraft:wasteland`
   - `twilightforest:twilight_forest`
   - `bloodmagic:dungeon`
3. Check current Quark entity IDs before re-adding frog/foxhound spawn caps.
4. If rules are ported, edit `config/incontrol/spawn.json`, run `packwiz refresh`, then create a fresh test world to ensure no schema errors.
