// Thermal dynamo fuel balance ported from E2 1.12 Thermal Expansion defaults.

ServerEvents.recipes(event => {
  event.remove({ output: 'thermal:dynamo_lapidary' })
  event.remove({ output: 'thermal:dynamo_disenchantment' })

  event.shaped('thermal:dynamo_lapidary', [
    ' G ',
    'ICI',
    ' X '
  ], {
    G: '#forge:gears/signalum',
    I: '#forge:plates/electrum',
    C: 'thermal:dynamo_numismatic',
    X: '#forge:gems/emerald'
  }).id('enigmatica2:thermal/dynamo_lapidary')

  event.shaped('thermal:dynamo_disenchantment', [
    ' G ',
    'ICI',
    ' X '
  ], {
    G: '#forge:gears/signalum',
    I: '#forge:plates/gold',
    C: 'thermal:dynamo_magmatic',
    X: '#forge:gems/lapis'
  }).id('enigmatica2:thermal/dynamo_disenchantment')

  event.remove({ type: 'thermal:lapidary_fuel' })

  var lapidaryFuels = [
    ['forge:gems/quartz', 50000],
    ['forge:gems/black_quartz', 50000],
    ['forge:gems/certus_quartz', 50000],
    ['forge:gems/apatite', 50000],
    ['forge:gems/lapis', 100000],
    ['forge:gems/prismarine', 187500],
    ['forge:gems/fluix', 50000],
    ['forge:gems/emerald', 250000],
    ['forge:gems/amethyst', 250000],
    ['forge:gems/ruby', 250000],
    ['forge:gems/sapphire', 250000],
    ['forge:gems/source', 150000],
    ['forge:gems/psigem', 250000],
    ['forge:gems/carminite', 250000],
    ['forge:gems/ender_crystal', 250000],
    ['forge:gems/enticing_crystal', 250000],
    ['forge:gems/weather_crystal', 250000],
    ['forge:gems/prescient_crystal', 250000],
    ['forge:gems/pulsating_crystal', 250000],
    ['forge:gems/dragonstone', 1875000],
    ['forge:gems/mana_diamond', 1875000],
    ['forge:gems/vibrant_crystal', 625000],
    ['forge:gems/diamond', 1500000]
  ]

  lapidaryFuels.forEach(function(fuel) {
    var tag = fuel[0]
    var energy = fuel[1]
    var id = tag.split('/').pop()
    event.custom({
      type: 'thermal:lapidary_fuel',
      ingredient: { tag: tag },
      energy: energy
    }).id('enigmatica2:thermal/lapidary_fuel/' + id)
  })

  event.custom({
    type: 'thermal:lapidary_fuel',
    ingredient: { item: 'redstone_arsenal:flux_gem' },
    energy: 1875000
  }).id('enigmatica2:thermal/lapidary_fuel/flux_gem')

  event.custom({
    type: 'thermal:compression_fuel',
    ingredient: {
      fluid: 'thermal:refined_fuel',
      amount: 1000
    },
    energy: 2250000
  }).id('thermal:fuels/compression/compression_refined_fuel')

  event.custom({
    type: 'thermal:compression_fuel',
    ingredient: {
      fluid_tag: 'forge:crude_oil',
      amount: 1000
    },
    energy: 400000
  }).id('enigmatica2:thermal/compression_fuel/crude_oil')

  event.custom({
    type: 'thermal:compression_fuel',
    ingredient: {
      fluid: 'thermal:heavy_oil',
      amount: 1000
    },
    energy: 1500000
  }).id('enigmatica2:thermal/compression_fuel/heavy_oil')

  event.custom({
    type: 'thermal:compression_fuel',
    ingredient: {
      fluid: 'thermal:light_oil',
      amount: 1000
    },
    energy: 1000000
  }).id('enigmatica2:thermal/compression_fuel/light_oil')
})
