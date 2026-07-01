// Immersive Engineering recipe adjustments for 1.20.1
// Scaffolding recipes

ServerEvents.recipes(event => {
  // Crude Oil Unification - preserve E2 distillation outputs.
  event.remove({ id: 'immersivepetroleum:distillationtower/oil' })
  event.custom({
    type: 'immersivepetroleum:distillation',
    byproducts: [
      {
        chance: '0.07',
        item: 'immersivepetroleum:bitumen'
      }
    ],
    energy: 4096,
    input: {
      amount: 75,
      tag: 'forge:crude_oil'
    },
    results: [
      {
        amount: 9,
        fluid: 'immersivepetroleum:lubricant'
      },
      {
        amount: 27,
        fluid: 'immersivepetroleum:diesel'
      },
      {
        amount: 39,
        fluid: 'immersivepetroleum:gasoline'
      }
    ],
    time: 20
  }).id('enigmatica2:ie/crude_oil_distillation')

  // Aluminum Scaffolding - produces 4 scaffolding blocks
  event.remove({ output: 'immersiveengineering:alu_scaffolding_standard' })
  event.shaped('4x immersiveengineering:alu_scaffolding_standard', [
    'R  ',
    'SR ',
    'SSR'
  ], {
    R: '#forge:rods/aluminum',
    S: '#immersiveengineering:scaffoldings/aluminum'
  }).id('enigmatica2:ie/aluminum_scaffolding')
  event.shaped('4x immersiveengineering:alu_scaffolding_standard', [
    '  R',
    ' RS',
    'RSS'
  ], {
    R: '#forge:rods/aluminum',
    S: '#immersiveengineering:scaffoldings/aluminum'
  }).id('enigmatica2:ie/aluminum_scaffolding_mirrored')

  // Steel Scaffolding - produces 4 scaffolding blocks
  event.remove({ output: 'immersiveengineering:steel_scaffolding_standard' })
  event.shaped('4x immersiveengineering:steel_scaffolding_standard', [
    'R  ',
    'SR ',
    'SSR'
  ], {
    R: '#forge:rods/steel',
    S: '#immersiveengineering:scaffoldings/steel'
  }).id('enigmatica2:ie/steel_scaffolding')
  event.shaped('4x immersiveengineering:steel_scaffolding_standard', [
    '  R',
    ' RS',
    'RSS'
  ], {
    R: '#forge:rods/steel',
    S: '#immersiveengineering:scaffoldings/steel'
  }).id('enigmatica2:ie/steel_scaffolding_mirrored')
})
