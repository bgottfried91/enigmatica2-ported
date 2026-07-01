// Applied Energistics 2 recipe adjustments for 1.20.1

ServerEvents.recipes(event => {
  // ====== AE2 PRESSES VIA THERMAL PRESS ======
  // Original E2 allowed processor presses to be made in the TE Compactor press mode.
  // Modern Thermal uses type thermal:press; schemas verified from thermal_foundation.
  event.custom({
    type: 'thermal:press',
    ingredient: { item: 'ae2:quartz_block' },
    result: [{ item: 'ae2:calculation_processor_press' }],
    energy: 50000
  }).id('enigmatica2:ae2/thermal_press_calculation_processor_press')

  event.custom({
    type: 'thermal:press',
    ingredient: { item: 'minecraft:diamond_block' },
    result: [{ item: 'ae2:engineering_processor_press' }],
    energy: 50000
  }).id('enigmatica2:ae2/thermal_press_engineering_processor_press')

  event.custom({
    type: 'thermal:press',
    ingredient: { tag: 'forge:plates/steel' },
    result: [{ item: 'ae2:logic_processor_press' }],
    energy: 50000
  }).id('enigmatica2:ae2/thermal_press_logic_processor_press')

  event.custom({
    type: 'thermal:press',
    ingredient: { item: 'minecraft:sandstone' },
    result: [{ item: 'ae2:silicon_press' }],
    energy: 50000
  }).id('enigmatica2:ae2/thermal_press_silicon_press')

  // ====== AE2 SILICON VIA THERMAL PRESS ======
  // Original E2 used TE Compactor mint mode: sand -> AE2 silicon.
  event.custom({
    type: 'thermal:press',
    ingredient: { item: 'minecraft:sand' },
    result: [{ item: 'ae2:silicon' }],
    energy: 2000
  }).id('enigmatica2:ae2/thermal_press_silicon')

  // ====== CHARGED CERTUS QUARTZ TO DUST ======
  // Convert charged certus quartz crystal to certus dust via Thermal Expansion Pulverizer
  // Original: mods.thermalexpansion.Pulverizer.addRecipe(<appliedenergistics2:material:2>, <appliedenergistics2:material:1>, 2000, <appliedenergistics2:material:2>, 20);
  // Old material IDs: material:1 = charged certus quartz, material:2 = fluix dust (both output and secondary)
  // New IDs: ae2:charged_certus_quartz_crystal (input), ae2:certus_quartz_dust (output)
  event.custom({
    type: 'thermal:pulverizer',
    ingredient: { item: 'ae2:charged_certus_quartz_crystal' },
    result: [
      { item: 'ae2:certus_quartz_dust' },
      { item: 'ae2:certus_quartz_dust', chance: 0.2 }
    ]
  }).id('enigmatica2:ae2/charged_certus_to_dust')
})
