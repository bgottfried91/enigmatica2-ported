# Thermal Fluid Transposer Port

Old machine: Thermal Expansion 1.12 Fluid Transposer.

Modern replacement: Thermal 1.20 Bottler (`thermal:bottler`), which accepts item + fluid inputs and produces item outputs.

## Sources Checked

- `ThermalExpansion-1.12.2-5.5.7.1-universal.jar`
  - Decompiled `cofh.thermalexpansion.util.managers.machine.TransposerManager`
  - Decompiled integration plugins that call `TransposerManager.addFillRecipe`
- `RedstoneArsenal-1.12.2-2.6.6.1-universal.jar`
  - Decompiled `cofh.redstonearsenal.item.ItemMaterial`
- Current Thermal 1.20 Bottler recipes in `thermal_expansion-1.20.1-11.0.1.29.jar`

## Implemented

Added in `kubejs/server_scripts/e2_recipes_thermal_bottler.js`:

| Old source | Old input | Old fluid | Old output | 1.20 Bottler recipe |
| --- | --- | --- | --- | --- |
| Redstone Arsenal + Thermal Expansion integration | `dustElectrum` | 500 mB redstone | `dustElectrumFlux` | `#forge:dusts/electrum` + 500 mB `thermal:redstone` -> `redstone_arsenal:flux_dust` |
| Redstone Arsenal + Thermal Expansion integration | diamond | 500 mB redstone | `gemCrystalFlux` | `#forge:gems/diamond` + 500 mB `thermal:redstone` -> `redstone_arsenal:flux_gem` |

These preserve old material cost. Current Thermal produces `thermal:redstone` from redstone dust at 100 mB per dust, so 500 mB equals five redstone dust.

## Already Covered By Current Thermal Bottler

Current Thermal already includes these relevant Bottler recipes, so they were not duplicated:

- Concrete powder + water -> concrete, all 16 colors.
- Glass bottle + water -> water bottle.
- Glass bottle + `#forge:experience` -> experience bottle.
- Dirt + water -> mud.
- Cobblestone + water -> mossy cobblestone.
- Stone bricks + water -> mossy stone bricks.

## Not Ported

These old Fluid Transposer entries were not ported because the modern item/fluid target is missing, obsolete, or better covered by current mechanics:

- Old Thermal elemental crystal conversions using Cryotheum:
  - `crystalRedstone`, `crystalGlowstone`, `crystalEnder`, `dustCryotheum`, `dustBlizz`, `dustBlitz`, `dustBasalz`, and Thermal 1.12 fertilizer/biomass/bioblend items do not have direct current Thermal 1.20 item equivalents in this pack.
- Potion transposer recipes:
  - Current Thermal Bottler already covers standard water and XP bottle cases; the old per-potion transposer behavior was part of Thermal's removed potion-fluid system.
- Seed oil extraction from every ore-dictionary `seed*` entry:
  - The modern Thermal Bottler is not an extraction machine, and current Thermal no longer exposes a direct equivalent seed-oil extraction path through Bottler.
- Biomes O Plenty 1.12 transposer recipes:
  - Old BOP mud/dried sand items do not map cleanly to current BOP 1.20 items. Current Thermal already has vanilla mud via Bottler.
- AbyssalCraft, GregTech/Tech Reborn hot ingot, and other old integration recipes:
  - The relevant mods/items are not present in the current 1.20 pack or do not have direct equivalents.
- Florb fill recipes:
  - Florbs are not present in the current Thermal 1.20 pack.

## Fluid Availability

The implemented recipes use `thermal:redstone`, which is already producible in the current pack:

- Thermal Magma Crucible: `#forge:dusts/redstone` -> 100 mB `thermal:redstone`.
- Thermal Magma Crucible: redstone block -> 900 mB `thermal:redstone`.

Other related fluids found but not required for the implemented recipes:

- NuclearCraft provides `#forge:redstone`, `#forge:molten_redstone`, `#forge:glowstone`, and `#forge:cryotheum`.
- TConstruct provides `#forge:ender` from molten ender.
