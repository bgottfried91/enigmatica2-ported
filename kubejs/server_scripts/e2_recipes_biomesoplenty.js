// Biomes O' Plenty recipe adjustments for 1.20.1
// Note: Original script relied on mods no longer in 1.20.1 pack

ServerEvents.recipes(event => {
  // JEI hide: amber (biomesoplenty:gem:7 in old 1.12) — doesn't exist in 1.20.1 BOP, no action needed

  // Original honey recipes used BoP hive variants — these don't exist in 1.20.1.
  // Vanilla Minecraft now provides honey_block and honeycomb.
  // BoP in 1.20.1 has no hive blocks.

  // Forestry Centrifuge recipes — Forestry mod is NOT in 1.20.1 pack. Retired.
  // - BoP flesh -> various meats
  // - BoP honey_block -> honey drops + Thermal Foundation materials (old numeric IDs)

  // Thermal Expansion Centrifuge for honey — also requires TE API check.
  // Deferred pending TE Centrifuge recipe format verification.
})
