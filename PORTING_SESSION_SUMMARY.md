# Enigmatica 2 Port - Session Summary

## Current Handoff - 2026-06-24

- Packwiz source: `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1`
- Active test instance: `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)`
- Active KubeJS server scripts: 22 in both locations.
- Packwiz KubeJS startup scripts: 1. Active test instance also has the generated KubeJS `example.js`.
- Latest static audit: `0 errors, 0 warnings, 0 info`.
- Latest confirmed full restart: startup loaded 2/2 scripts, client loaded 2/2 scripts, and server loaded 22/22 scripts with 0 KubeJS errors and 0 KubeJS warnings. Recipe pass had 0 failed recipes.
- Pending test: gameplay spot-checks for new TConstruct recipes/fuels and startup item property changes.

Latest work:

- Confirmed the fresh 2026-06-25 launch loaded `21/21` KubeJS server scripts with `0 errors` and `0 warnings`; recipe pass had `0 failed recipes`.
- Reviewed `AkashicTome.zs`, `MorphOTool.zs`, and `Backpacks.zs`; all are done/no-op because current mods have native recipes or the old target items are absent.
- Added `e2_recipes_industrial_foregoing.js`.
- Ported Industrial Foregoing BioReactor compatibility using the modern `industrialforegoing:bioreactor` item tag.
- Retired old IF FluidDictionary and Protein Reactor entries because current IF 1.20.1 does not expose equivalent items/APIs.
- Added `e2_recipes_tinkers_construct.js`.
- Ported TConstruct molten steel alloying via modern `tconstruct:alloy` JSON using molten iron plus JAOPCA molten coal.
- Ported modern TConstruct melting fuels for sulfuric acid, refined fuel, diesel, and gasoline. Retired old pyrotheum, demonic metal, IC2, and Astral Sorcery fuel entries because those fluids are absent.
- Added `e2_item_properties.js` startup script.
- Ported startup-only Mekanism tier installer/upgrades stack sizes and Cyclic mattock durability.
- Added `e2_tooltips.js`.
- Ported current Blood Magic demon crystal guidance from `Tooltips.zs`; retired the old removed-mod tooltip entries.
- Reviewed and retired the small removed-mod scripts: `ExtraUtilities2.zs`, `AdvancedRocketry.zs`, `Bibliocraft.zs`, `BinniesMod.zs`, `extrabees.zs`, `MekanismBgott.zs`, and `Smeltables&Burnables.zs`.
- PlusTiC/PlusTiC Reforged work is intentionally skipped for now; checked releases do not provide a viable 1.20.1 Forge jar.

Recommended next steps:

1. Spot-check the new TConstruct molten steel recipe and added smeltery fuels in JEI/in-game.
2. Spot-check Mekanism installer/upgrade stack sizes and Cyclic mattock durability.
3. Do a JEI/client cleanup pass only after gameplay confirms which duplicates are actually noisy.

## Scripts Ported (Verified & Working ✅)

### 1. Furnace.zs → e2_recipes_furnace.js ✓
- **Status**: Ready to test
- **Changes**: Added support for Deepslate and Raw ore variants in 1.20.1
- **Content**: Smelting recipes for all vanilla ore types

### 2. Plates.zs → e2_recipes_plates.js ✓
- **Status**: Ready to test
- **Changes**: 
  - Consolidated to Thermal Foundation plates as standard
  - Removed recipes for mods not in 1.20.1 (IC2, Embers old recipes)
  - Added IE Hammer shapeless recipes for material unification
- **Content**: Material consolidation, recipe removals, shapeless crafting

### 3. OreDict.zs → e2_tags_material_unification.js ✓
- **Status**: Ready to test (partial port)
- **Changes**: 
  - Converted OreDict entries to Forge tags
  - Focused on mods that exist in 1.20.1
  - Skipped removed mods (Thaumcraft, IC2, Astral Sorcery, Forestry)
- **Content**: Boats, meat consolidation, blood runes, quartz varieties, cakes

### 4. Cyclic.zs → e2_recipes_cyclic.js ✓
- **Status**: Ready to test
- **Changes**: Updated mod ID from `cyclicmagic` to `cyclic`, crafted custom storage bag recipe
- **Content**: Storage bag recipe, item removal

### 5. AdvancedGenerators.zs → e2_recipes_advanced_generators.js ✓
- **Status**: Already tested and working (from previous session)
- **Content**: Controller circuit recipe

## Next Steps

### Immediate Testing Required
1. Export current Packwiz: `packwiz curseforge export` ✓ (done)
2. Import into CurseForge profile `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)`
3. Run `/mnt/i/minecraft/Instances/Enigmatica2-1.20.1/tools/fix-curseforge-memory.sh 10240`
4. Check `/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)/logs/kubejs/server.log` for errors
5. Test in-game: Create new world, verify recipes load without crashes

### Blocked/Deferred Scripts (Need Investigation)

**Requires Item ID Validation:**
- `RecipeConflicts.zs` (209 lines) - Many removed mods; need to check which are still in 1.20.1
- `MiscRecipes.zs` (255 lines) - Mixed replacements; needs mod-by-mod review
- `Mekanism.zs` (73 lines) - References Astral Sorcery (removed); rest may be valid
- `ImmersiveEngineering.zs` (27 lines) - Uses Immersive Petroleum API; needs validation
- `ThermalExpansion.zs` (75 lines) - Currently all commented out; no action needed
- `Embers.zs` (55 lines) - Embers Rekindled exists; API may have changed

**Not In 1.20.1:**
- `Thaumcraft.zs` - Mod removed (replaced by Ars Nouveau)
- `IndustrialCraft2.zs` - Mod removed (replaced by Industrial Foregoing)
- `ExtraUtilities2.zs` - Mod removed
- `Forestry.zs` derivatives - Mod removed
- `Backpacks.zs` - Replaced by Sophisticated Backpacks

**Commented Out / Low Priority:**
- `TempRecipes.zs` - Extra Cells not in pack
- `PlankWoodFix.zs` - All functional code is commented
- `JEICategories.zs` - JEI categories changed; re-evaluate later

## Testing Commands

Once game is running with current scripts:

```bash
# Verify server log
tail -100 "/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)/logs/kubejs/server.log" | grep -A5 -B5 "error\|Error\|ERROR"

# Check that all scripts loaded
grep "Loaded script" "/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)/logs/kubejs/server.log"
```

## Strategy Notes

**Philosophy Preserved:**
- Material consolidation (TF plates as standard, but multipath access)
- Tag-based unification instead of old OreDict
- Removal of duplicate variants to reduce JEI clutter
- Multi-tool compatibility (IE hammer, etc.)

**Known Limitations:**
- Cannot test actual recipe execution until game runs
- Item IDs and mod APIs in 1.20.1 differ from 1.12.2; manual validation needed for complex scripts
- Some recipes may need adjustment based on actual mod item names in 1.20.1

**Recommended Next Session:**
1. Run actual game test
2. Check KubeJS logs for any errors
3. Fix validation errors (likely item ID mismatches)
4. Port `RecipeConflicts.zs` focusing only on remaining mods
5. Port `MiscRecipes.zs` in chunks by mod source
