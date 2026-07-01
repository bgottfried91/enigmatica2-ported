// Actually Additions / Actually Subtractions recipes for Enigmatica 2 - 1.20.1

ServerEvents.recipes(event => {
  // ====== BLACK QUARTZ ======
  // Restore E2's block-to-gem unpacking convenience recipes.
  event.shapeless('4x actuallyadditions:black_quartz', [
    'actuallyadditions:black_quartz_block'
  ]).id('enigmatica2:actuallyadditions/black_quartz_block_to_black_quartz')

  event.shapeless('4x actuallyadditions:black_quartz', [
    'actuallyadditions:chiseled_black_quartz_block'
  ]).id('enigmatica2:actuallyadditions/chiseled_black_quartz_to_black_quartz')

  event.shapeless('2x actuallyadditions:black_quartz', [
    'actuallyadditions:black_quartz_pillar_block'
  ]).id('enigmatica2:actuallyadditions/black_quartz_pillar_to_black_quartz')

  // ====== CRUSHER ======
  // E2 added Actually Additions crusher compatibility for AE2 certus quartz.
  event.custom({
    type: 'actuallyadditions:crushing',
    ingredient: { item: 'ae2:charged_certus_quartz_crystal' },
    result: [
      {
        chance: 1.0,
        result: {
          Count: 1,
          id: 'ae2:certus_quartz_dust'
        }
      },
      {
        chance: 0.0,
        result: {
          Count: 0,
          id: 'minecraft:air'
        }
      }
    ]
  }).id('enigmatica2:actuallyadditions/crushing/charged_certus_quartz')

  event.custom({
    type: 'actuallyadditions:crushing',
    ingredient: { item: 'ae2:certus_quartz_crystal' },
    result: [
      {
        chance: 1.0,
        result: {
          Count: 1,
          id: 'ae2:certus_quartz_dust'
        }
      },
      {
        chance: 0.0,
        result: {
          Count: 0,
          id: 'minecraft:air'
        }
      }
    ]
  }).id('enigmatica2:actuallyadditions/crushing/certus_quartz')
})
