// Integrated Dynamics recipe adjustments for 1.20.1
// Note: Original script was entirely commented out; old item IDs no longer exist in 1.20.1

ServerEvents.recipes(event => {
  // Original squeezer/mechanical_squeezer recipes for aluminum/osmium were all commented out
  // in the 1.12.2 source and referenced non-existent 1.20.1 item IDs:
  // - mekanism:oreblock (does not exist; replaced by modern ore IDs)
  // - mekanism:dust:2 (numeric ID format obsolete; use mekanism:dust_osmium, etc.)
  // - thermalfoundation:ore:4 (numeric ID format obsolete; use thermal:lead_ore, etc.)
  // - thermalfoundation:material:68 (numeric ID format obsolete; use thermal:lead_dust, etc.)
  //
  // If squeezer recipes are needed, create custom recipes referencing current item IDs.
})
