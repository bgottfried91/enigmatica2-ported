// Recipe conflict resolution for Enigmatica 2
// Prevents duplicate/conflicting recipes between mods in 1.20.1

ServerEvents.recipes(event => {
  // Vanilla trapdoor: fix recipe conflict
  event.remove({ output: 'minecraft:oak_trapdoor' })
  event.shaped('minecraft:oak_trapdoor', [
    'PPP',
    'PPP'
  ], {
    P: '#minecraft:planks'
  }).id('enigmatica2:conflicts/oak_trapdoor')

  // Structurize Builder's Wand (Gold) - Scan Tool
  event.remove({ output: 'structurize:sceptergold' })
  event.shaped('structurize:sceptergold', [
    '  C',
    ' S ',
    'S  '
  ], {
    C: '#forge:ingots/copper',
    S: 'minecraft:stick'
  }).id('enigmatica2:conflicts/structurize_sceptergold')
  event.shaped('structurize:sceptergold', [
    'C  ',
    ' S ',
    '  S'
  ], {
    C: '#forge:ingots/copper',
    S: 'minecraft:stick'
  }).id('enigmatica2:conflicts/structurize_sceptergold_mirrored')

  // Structurize Builder's Wand (Steel) - Build Tool
  event.remove({ output: 'structurize:sceptersteel' })
  event.shaped('structurize:sceptersteel', [
    '  T',
    ' S ',
    'S  '
  ], {
    T: '#forge:ingots/tin',
    S: 'minecraft:stick'
  }).id('enigmatica2:conflicts/structurize_sceptersteel')
  event.shaped('structurize:sceptersteel', [
    'T  ',
    ' S ',
    '  S'
  ], {
    T: '#forge:ingots/tin',
    S: 'minecraft:stick'
  }).id('enigmatica2:conflicts/structurize_sceptersteel_mirrored')

  // Advanced Generators Iron Frame
  event.remove({ output: 'advgenerators:iron_frame' })
  event.shaped('2x advgenerators:iron_frame', [
    'I I',
    '   ',
    'I I'
  ], {
    I: '#forge:ingots/iron'
  }).id('enigmatica2:conflicts/advgen_iron_frame')

  // Mekanism Boiler Casing (updated item ID for 1.20.1)
  event.remove({ output: 'mekanism:boiler_casing' })
  event.shaped('8x mekanism:boiler_casing', [
    'SSS',
    'SIS',
    'SSS'
  ], {
    S: '#forge:ingots/steel',
    I: '#forge:ingots/iron'
  }).id('enigmatica2:conflicts/mekanism_boiler_casing')

  // Metal storage block conflicts - remove duplicates from mods
  // Note: Old metadata notation (e.g., :1, :7) is invalid in 1.20.1
  // Keeping only removals that use valid modern item IDs

  // Embers metal blocks
  event.remove({ output: 'embers:lead_block' })
  event.remove({ output: 'embers:silver_block' })
})
