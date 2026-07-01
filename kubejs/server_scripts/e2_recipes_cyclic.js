// Cyclic mod recipe adjustments
// Storage bag recipe and item balance

ServerEvents.recipes(event => {
  // Replace Storage Bag recipe with custom one using gold/redstone blocks
  event.remove({ output: 'cyclic:storage_bag' })

  event.shaped('cyclic:storage_bag', [
    'LSL',
    'LGL',
    'LRL'
  ], {
    L: '#forge:leather',
    S: '#forge:string',
    G: '#forge:storage_blocks/gold',
    R: '#forge:storage_blocks/redstone'
  }).id('enigmatica2:cyclic/storage_bag')

  // Note: Old 1.12 purple helmet and toxic heart items do not exist in Cyclic 1.20.1.
})
