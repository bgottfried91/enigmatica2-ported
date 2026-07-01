# Enigmatica 2 Ported Notes

Active test profile: `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)`
Packwiz source: `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1`

## Current Status

- Current Packwiz version: `1.0.2`
- Latest exported CurseForge zip: `/tmp/enigmatica2-ported-1.20.1-v1.0.2.zip`
- Active imported CurseForge profile: `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)`
- Older duplicate profile `/mnt/i/minecraft/Instances/Enigmatica 2 Ported` was deleted.
- CurseForge memory override helper exists at `tools/fix-curseforge-memory.sh`.
- Active profile memory is set to `10240` MB with per-profile override enabled.
- Packwiz source now uses root-level instance paths (`config/...`, `kubejs/...`) so CurseForge export produces correct `overrides/config/...` and `overrides/kubejs/...` paths.
- Local-only notes, reference scripts, and tools are ignored by `.packwizignore` and should not ship in exported zips.

## Config Change Queue

| Status | Area | Change | Source/Test Profile | Canonicalized |
|---|---|---|---|---|
| Done | Video settings | Disable VSync by default in Minecraft video settings. Later investigate why VSync causes screen flashing. | `Enigmatica 2 Ported (1)` | Yes, `config/defaultoptions/options.txt` |
| Done | Controls | Set default `OreExcavation` category `Excavate` key to `` ` ``. | `Enigmatica 2 Ported (1)` | Yes, `config/defaultoptions/keybindings.txt` |
| Done | Video settings | Set default Minecraft GUI scale to `3`. | `Enigmatica 2 Ported (1)` | Yes, `config/defaultoptions/options.txt` |
| Todo | JER / NuclearCraft | Test whether JER categories work despite JEI startup error for `nuclearcraft:wasteland` biome key. Do not patch NuclearCraft worldgen unless functionality is actually broken. | `Enigmatica 2 Ported (1)` | No |

## Script Porting Queue

Original E2 scripts were not ported into the 1.20.1 pack. They are copied as non-loaded references under `reference/original-e2-scripts/`.

Track script work in `SCRIPT_PORTING_AUDIT.md`. The current source target is KubeJS `kubejs/server_scripts/*.js`. CraftTweaker has been removed from the Packwiz source.

### Script Migration Status

- KubeJS added to Packwiz source: `mods/kubejs.pw.toml`
- Rhino dependency added to Packwiz source: `mods/rhino.pw.toml`
- CraftTweaker removed from Packwiz source.
- First translated script added: `kubejs/server_scripts/e2_recipes_advanced_generators.js`
- First translated script purpose: port original E2 `AdvancedGenerators.zs` controller recipe so `advgenerators:controller` costs redstone blocks instead of redstone dust.
- Tested in imported CurseForge profile on `2026-06-23`.
- KubeJS server log confirmed:
  - `Loaded script server_scripts:e2_recipes_advanced_generators.js`
  - `Loaded 1/1 KubeJS server scripts ... with 0 errors and 0 warnings`
  - `Server resource reload complete!`
- User completed new world creation test successfully after importing `v1.0.2`.
- KubeJS generated default example scripts in the active profile under `kubejs/startup_scripts/example.js` and `kubejs/client_scripts/example.js`; these are not in Packwiz source and can be deleted from the active profile to reduce log noise.

## Status Values

- `Todo`: noted, not tested
- `Testing`: changed in imported profile, needs validation
- `Accepted`: works in imported profile, needs copy to Packwiz overrides
- `Done`: copied to Packwiz source and `packwiz refresh` run
- `Rejected`: tested and not keeping
- `Blocked`: needs research or dependency decision

## Workflow

1. Make config changes in the active imported profile.
2. Test in-game until the behavior is confirmed.
3. Copy accepted config files into the Packwiz source at their instance-root paths, such as `config/...` or `kubejs/...`. Packwiz will place them under the top-level CurseForge `overrides/` folder during export.
4. Run `packwiz refresh` in the Packwiz source.
5. Bump `pack.toml` only when preparing a new import/export build.

## Handoff Notes

- Continue porting original E2 scripts from `reference/original-e2-scripts/` into KubeJS.
- Do not copy old `.zs` files into loaded folders; treat them as intent/reference only.
- Use `SCRIPT_PORTING_AUDIT.md` as the script queue and update each row as scripts are ported, deferred, or retired.
- Recommended next targets:
  - Material/tag unification scaffolding from `OreDict.zs` and `OreDictATM.zs`.
  - Plate recipe unification from `Plates.zs`.
  - Existing-mod recipe conflict fixes from `RecipeConflicts.zs`.
  - Mekanism/Thermal/Immersive Engineering processing balance after validating current 1.20 recipe IDs.
- Validate current item IDs from the imported profile jars, JEI, or KubeJS `/kjs hand`; old 1.12 metadata IDs are not reliable.
- After each small script batch, export a new versioned zip, reimport through CurseForge, run `tools/fix-curseforge-memory.sh 10240`, then check `logs/kubejs/server.log`.

## Local Helper Scripts

- `tools/fix-curseforge-memory.sh [memory_mb] [profile_path]`: sets the newest `Enigmatica 2 Ported*` CurseForge profile to use a per-profile memory override. Defaults to `10240` MB.

## KubeJS Recipe Debugging Pattern

**When debugging KubeJS recipe failures:**

1. **First pass:** Write each recipe as an explicit line (not in a loop). KubeJS error messages report exact line numbers - loops obscure which recipe failed.
   
   ```javascript
   // GOOD for debugging - errors point to exact recipes
   event.shapeless(recipe1, [...])
   event.shapeless(recipe2, [...])
   event.shapeless(recipe3, [...])
   ```

   ```javascript
   // BAD for debugging - error line numbers are ambiguous
   recipes.forEach(r => event.shapeless(...))
   ```

2. **Verify it works:** Run `/reload` and check logs for errors. Fix identified issues.

3. **Second pass (cleanup):** Once all recipes work, restore loop structures if they improve readability.

Example: `e2_recipes_plates.js` was debugged by writing out 14 shapeless recipes explicitly, identified that `thermal:aluminum_plate` and `thermal:steel_plate` don't exist in 1.20.1, removed those lines, then restored the loop structure for cleaner code.
