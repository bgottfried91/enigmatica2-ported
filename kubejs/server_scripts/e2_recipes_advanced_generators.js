ServerEvents.recipes(event => {
  event.remove({ id: 'advgenerators:crafting/controller' })

  event.shaped('advgenerators:controller', [
    'IRI',
    'RQR',
    'IRI'
  ], {
    I: '#forge:ingots/iron',
    R: 'minecraft:redstone_block',
    Q: '#forge:gems/quartz'
  }).id('enigmatica2:advgenerators/controller')
})
