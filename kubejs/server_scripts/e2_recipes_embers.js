// Embers Rekindled recipe adjustments for 1.20.1
// Note: Original script hid old Embers tools; Embers Rekindled uses different tool IDs

ServerEvents.recipes(event => {
  // Original script hid Embers tools that conflicted with Thermal Foundation:
  // copper, silver, lead, aluminum, bronze, electrum, nickel, tin tools
  //
  // Embers Rekindled (1.20.1) was redesigned and no longer provides these tools.
  // Modern Embers tools: clockwork, dawnstone, lead (different set).
  // Verify if modern tools actually conflict with TF before adding JEI hides.
})
