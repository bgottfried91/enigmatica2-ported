// Material Unification: Consolidate plates to Thermal Foundation standard
// Plates from Embers, IE, NuclearCraft, and other mods redirected to TF plates

ServerEvents.recipes(event => {
  // Remove Embers plates
  const embersPlates = [
    'embers:copper_plate',
    'embers:lead_plate',
    'embers:silver_plate',
    'embers:iron_plate'
  ]

  embersPlates.forEach(plate => {
    event.remove({ output: plate })
  })

  // Remove IE Metal Press plates
  const ieMetalPlates = [
    'immersiveengineering:plate_constantan',
    'immersiveengineering:plate_copper',
    'immersiveengineering:plate_electrum',
    'immersiveengineering:plate_gold',
    'immersiveengineering:plate_iron',
    'immersiveengineering:plate_lead',
    'immersiveengineering:plate_nickel',
    'immersiveengineering:plate_silver'
  ]

  ieMetalPlates.forEach(plate => {
    event.remove({ output: plate })
  })

  // Remove NuclearCraft common duplicate plates where Thermal equivalents exist
  const nuclearCraftPlates = [
    'nuclearcraft:bronze_plate',
    'nuclearcraft:copper_plate',
    'nuclearcraft:iron_plate',
    'nuclearcraft:lead_plate',
    'nuclearcraft:tin_plate'
  ]

  nuclearCraftPlates.forEach(plate => {
    event.remove({ output: plate })
  })

  const metalPressPlateMaterials = [
    'iron',
    'gold',
    'copper',
    'tin',
    'silver',
    'lead',
    'nickel',
    'electrum',
    'invar',
    'bronze',
    'constantan'
  ]

  metalPressPlateMaterials.forEach(material => {
    event.remove({ id: `immersiveengineering:metalpress/plate_${material}` })
    event.custom({
      type: 'immersiveengineering:metal_press',
      energy: 2400,
      input: { tag: `forge:ingots/${material}` },
      mold: 'immersiveengineering:mold_plate',
      result: { item: `thermal:${material}_plate` }
    }).id(`enigmatica2:plates/metal_press_${material}_plate`)
  })

  const nuclearCraftPressurizerMaterials = [
    { material: 'iron', input: { item: 'minecraft:iron_ingot' }, removeId: 'nuclearcraft:pressurizer/iron_ingot' },
    { material: 'gold', input: { item: 'minecraft:gold_ingot' } },
    { material: 'copper', input: { item: 'minecraft:copper_ingot' }, removeId: 'nuclearcraft:pressurizer/copper_ingot' },
    { material: 'tin', input: { tag: 'forge:ingots/tin' }, removeId: 'nuclearcraft:pressurizer/ingots_tin' },
    { material: 'lead', input: { tag: 'forge:ingots/lead' }, removeId: 'nuclearcraft:pressurizer/ingots_lead' },
    { material: 'bronze', input: { tag: 'forge:ingots/bronze' }, removeId: 'nuclearcraft:pressurizer/ingots_bronze' }
  ]

  nuclearCraftPressurizerMaterials.forEach(recipe => {
    if (recipe.removeId) {
      event.remove({ id: recipe.removeId })
    }
    event.custom({
      type: 'nuclearcraft:pressurizer',
      input: [recipe.input],
      output: [
        {
          item: `thermal:${recipe.material}_plate`
        }
      ],
      powerModifier: 1.0,
      radiation: 1.0,
      timeModifier: 1.0
    }).id(`enigmatica2:plates/nuclearcraft_pressurizer_${recipe.material}_plate`)
  })

  // Add hammer recipes for Thermal plates using IE hammer
  // Note: aluminum_plate and steel_plate do not exist in Thermal 1.20.1
  const plateRecipes = [
    { ingot: 'minecraft:iron_ingot', plate: 'thermal:iron_plate' },
    { ingot: 'minecraft:gold_ingot', plate: 'thermal:gold_plate' },
    { ingot: '#forge:ingots/copper', plate: 'thermal:copper_plate' },
    { ingot: '#forge:ingots/tin', plate: 'thermal:tin_plate' },
    { ingot: '#forge:ingots/silver', plate: 'thermal:silver_plate' },
    { ingot: '#forge:ingots/lead', plate: 'thermal:lead_plate' },
    { ingot: '#forge:ingots/nickel', plate: 'thermal:nickel_plate' },
    { ingot: '#forge:ingots/bronze', plate: 'thermal:bronze_plate' },
    { ingot: '#forge:ingots/invar', plate: 'thermal:invar_plate' },
    { ingot: '#forge:ingots/electrum', plate: 'thermal:electrum_plate' },
    { ingot: '#forge:ingots/constantan', plate: 'thermal:constantan_plate' },
    { ingot: '#forge:ingots/signalum', plate: 'thermal:signalum_plate' },
    { ingot: '#forge:ingots/lumium', plate: 'thermal:lumium_plate' },
    { ingot: '#forge:ingots/enderium', plate: 'thermal:enderium_plate' }
  ]

  plateRecipes.forEach(recipe => {
    event.shapeless(recipe.plate, [recipe.ingot, 'immersiveengineering:hammer'])
      .id(`enigmatica2:plates/${recipe.plate.split(':')[1]}_from_hammer`)
  })
})
