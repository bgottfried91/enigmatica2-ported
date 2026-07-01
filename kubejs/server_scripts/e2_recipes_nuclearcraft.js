// NuclearCraft recipes for Enigmatica 2 - 1.20.1

ServerEvents.recipes(event => {
  // E2 removed the obsidian-dust melt path and set obsidian to exactly one
  // ingot-equivalent bucket fraction.
  event.remove({ id: 'nuclearcraft:melter/obsidian' })
  event.remove({ id: 'nuclearcraft:melter/dusts_obsidian' })
  event.custom({
    type: 'nuclearcraft:melter',
    input: [
      {
        item: 'minecraft:obsidian'
      }
    ],
    outputFluids: [
      {
        amount: 144,
        tag: 'forge:molten_obsidian'
      }
    ],
    powerModifier: 1.0,
    radiation: 1.0,
    timeModifier: 1.0
  }).id('enigmatica2:nuclearcraft/melter/obsidian')

  // E2 buffed electrolysis by adding small tritium/deuterium byproducts.
  event.remove({ id: 'nuclearcraft:electrolyzer/heavy_water' })
  event.custom({
    type: 'nuclearcraft:electrolyzer',
    inputFluids: [
      {
        amount: 1000,
        tag: 'forge:heavy_water'
      }
    ],
    outputFluids: [
      {
        amount: 1000,
        tag: 'forge:deuterium'
      },
      {
        amount: 500,
        tag: 'forge:oxygen'
      },
      {
        amount: 50,
        tag: 'forge:tritium'
      }
    ],
    powerModifier: 1.0,
    radiation: 1.0,
    timeModifier: 1.0
  }).id('enigmatica2:nuclearcraft/electrolyzer/heavy_water')

  event.remove({ id: 'nuclearcraft:electrolyzer/water' })
  event.custom({
    type: 'nuclearcraft:electrolyzer',
    inputFluids: [
      {
        amount: 1000,
        tag: 'minecraft:water'
      }
    ],
    outputFluids: [
      {
        amount: 1000,
        tag: 'forge:hydrogen'
      },
      {
        amount: 500,
        tag: 'forge:oxygen'
      },
      {
        amount: 50,
        tag: 'forge:deuterium'
      }
    ],
    powerModifier: 1.0,
    radiation: 1.0,
    timeModifier: 1.0
  }).id('enigmatica2:nuclearcraft/electrolyzer/water')
})
