// Mekanism recipe adjustments and tool balance for 1.20.1

ServerEvents.recipes(event => {
  // ====== HIDE MEKANISM TOOL DUPLICATES ======
  // Hide bronze tools (we use Thermal Foundation instead)
  event.remove({ output: 'mekanismtools:bronze_pickaxe' })
  event.remove({ output: 'mekanismtools:bronze_axe' })
  event.remove({ output: 'mekanismtools:bronze_shovel' })
  event.remove({ output: 'mekanismtools:bronze_hoe' })
  event.remove({ output: 'mekanismtools:bronze_sword' })

  // Hide bronze armor
  event.remove({ output: 'mekanismtools:bronze_helmet' })
  event.remove({ output: 'mekanismtools:bronze_chestplate' })
  event.remove({ output: 'mekanismtools:bronze_leggings' })
  event.remove({ output: 'mekanismtools:bronze_boots' })

  // Hide steel tools (we use Thermal Foundation instead)
  event.remove({ output: 'mekanismtools:steel_pickaxe' })
  event.remove({ output: 'mekanismtools:steel_axe' })
  event.remove({ output: 'mekanismtools:steel_shovel' })
  event.remove({ output: 'mekanismtools:steel_hoe' })
  event.remove({ output: 'mekanismtools:steel_sword' })

  // Hide steel armor
  event.remove({ output: 'mekanismtools:steel_helmet' })
  event.remove({ output: 'mekanismtools:steel_chestplate' })
  event.remove({ output: 'mekanismtools:steel_leggings' })
  event.remove({ output: 'mekanismtools:steel_boots' })

  // ====== REPLACE PAXEL RECIPES ======
  // Bronze Paxel - use Thermal Foundation tools instead
  event.remove({ output: 'mekanismtools:bronze_paxel' })
  event.shaped('mekanismtools:bronze_paxel', [
    'BBB',
    'BBB',
    'BRR'
  ], {
    B: '#forge:ingots/bronze',
    R: '#forge:rods/wooden'
  }).id('enigmatica2:mekanism/bronze_paxel')

  // Steel Paxel - use Thermal Foundation tools instead
  event.remove({ output: 'mekanismtools:steel_paxel' })
  event.shaped('mekanismtools:steel_paxel', [
    'SSS',
    'SSS',
    'SRR'
  ], {
    S: '#forge:ingots/steel',
    R: '#forge:rods/wooden'
  }).id('enigmatica2:mekanism/steel_paxel')

  // ====== MEKANISM COMBINER BALANCE ======
  // 1.12 used six raw quartz/coal instead of the default modern dust costs.
  event.remove({ id: 'mekanism:processing/quartz/to_ore' })
  event.custom({
    type: 'mekanism:combining',
    mainInput: {
      amount: 6,
      ingredient: { item: 'minecraft:quartz' }
    },
    extraInput: {
      ingredient: { item: 'minecraft:netherrack' }
    },
    output: { item: 'minecraft:nether_quartz_ore' }
  }).id('enigmatica2:mekanism/quartz_ore_combining')

  event.remove({ id: 'mekanism:processing/coal/to_ore' })
  event.custom({
    type: 'mekanism:combining',
    mainInput: {
      amount: 6,
      ingredient: { item: 'minecraft:coal' }
    },
    extraInput: {
      ingredient: { tag: 'forge:cobblestone/normal' }
    },
    output: { item: 'minecraft:coal_ore' }
  }).id('enigmatica2:mekanism/coal_ore_combining')

  // Mekanism 10.4.16 reports these two built-in recipes as incomplete because
  // their tag inputs resolve empty in this pack. Recreate them with direct IDs.
  event.remove({ id: 'mekanism:injecting/concrete/pink' })
  event.custom({
    type: 'mekanism:injecting',
    chemicalInput: {
      amount: 1,
      gas: 'mekanism:water_vapor'
    },
    itemInput: {
      ingredient: { item: 'minecraft:pink_concrete_powder' }
    },
    output: { item: 'minecraft:pink_concrete' }
  }).id('enigmatica2:mekanism/injecting/concrete/pink')

  event.remove({ id: 'mekanism:rotary/sulfur_trioxide' })
  event.custom({
    type: 'mekanism:rotary',
    fluidInput: {
      amount: 1,
      fluid: 'mekanism:sulfur_trioxide'
    },
    fluidOutput: {
      amount: 1,
      fluid: 'mekanism:sulfur_trioxide'
    },
    gasInput: {
      amount: 1,
      gas: 'mekanism:sulfur_trioxide'
    },
    gasOutput: {
      amount: 1,
      gas: 'mekanism:sulfur_trioxide'
    }
  }).id('enigmatica2:mekanism/rotary/sulfur_trioxide')

  // Note: Astral Sorcery starmetal recipe removed (mod not in 1.20.1)
  // Note: old Forestry apatite combiner dupe fix is obsolete; Thermal apatite is the current canonical apatite.
})

// Note: Stack size adjustments in 1.20.1 are typically done via item JSON configs, not recipes
// If needed, these can be configured in mekanism's config files or via a data pack
