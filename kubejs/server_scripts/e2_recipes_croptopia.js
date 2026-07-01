// Croptopia integration with Immersive Engineering for 1.20.1
// Mirrors Harvestcraft compatibility: crops → ethanol, seeds → plant oil

ServerEvents.recipes(event => {
  event.remove({ id: 'croptopia:salt_from_water_bottle' })
  event.remove({ id: 'croptopia:salt_from_smoking_water_bottle' })

  event.shapeless('croptopia:salt', [
    'croptopia:cooking_pot',
    '#forge:water_bottles'
  ]).id('enigmatica2:croptopia/salt_from_water_bottle_crafting')

  event.smelting('minecraft:bread', 'croptopia:dough')
    .xp(0.35)
    .cookingTime(200)
    .id('enigmatica2:croptopia/bread_from_dough_smelting')

  event.smoking('minecraft:bread', 'croptopia:dough')
    .xp(0.35)
    .cookingTime(100)
    .id('enigmatica2:croptopia/bread_from_dough_smoking')

  event.campfireCooking('minecraft:bread', 'croptopia:dough')
    .xp(0.35)
    .cookingTime(600)
    .id('enigmatica2:croptopia/bread_from_dough_campfire')

  // ====== CROPTOPIA CROPS → ETHANOL ======
  // Convert all Croptopia crops to ethanol via IE Fermenter
  const crops = [
    'croptopia:artichoke', 'croptopia:asparagus', 'croptopia:bellpepper', 'croptopia:blackbean',
    'croptopia:blackberry', 'croptopia:blueberry', 'croptopia:broccoli', 'croptopia:cabbage',
    'croptopia:cantaloupe', 'croptopia:cauliflower', 'croptopia:celery', 'croptopia:corn',
    'croptopia:cranberry', 'croptopia:cucumber', 'croptopia:currant', 'croptopia:eggplant',
    'croptopia:elderberry', 'croptopia:garlic', 'croptopia:grape', 'croptopia:greenbean',
    'croptopia:honeydew', 'croptopia:hops', 'croptopia:kale', 'croptopia:kiwi',
    'croptopia:leek', 'croptopia:lettuce', 'croptopia:olive', 'croptopia:onion',
    'croptopia:peanut', 'croptopia:pineapple', 'croptopia:radish', 'croptopia:raspberry',
    'croptopia:rhubarb', 'croptopia:rice', 'croptopia:rutabaga', 'croptopia:saguaro',
    'croptopia:squash', 'croptopia:strawberry', 'croptopia:tomatillo', 'croptopia:tomato',
    'croptopia:turnip', 'croptopia:yam', 'croptopia:zucchini', 'croptopia:mustard',
    'croptopia:chile_pepper', 'croptopia:turmeric', 'croptopia:ginger', 'croptopia:basil',
    'croptopia:oat', 'croptopia:barley', 'croptopia:soybean', 'croptopia:pepper',
    'croptopia:tea', 'croptopia:almond', 'croptopia:apricot', 'croptopia:avocado',
    'croptopia:banana', 'croptopia:cashew', 'croptopia:cherry',
    'croptopia:cinnamon', 'croptopia:coconut', 'croptopia:coffee_beans', 'croptopia:date',
    'croptopia:dragonfruit', 'croptopia:fig', 'croptopia:grapefruit',
    'croptopia:lemon', 'croptopia:lime',
    'croptopia:mango', 'croptopia:nectarine', 'croptopia:orange',
    'croptopia:peach', 'croptopia:pear',
    'croptopia:pecan', 'croptopia:persimmon', 'croptopia:plum'
  ]

  crops.forEach(crop => {
    event.custom({
      type: 'immersiveengineering:fermenter',
      energy: 6400,
      fluid: {
        amount: 80,
        fluid: 'immersiveengineering:ethanol'
      },
      input: {
        item: crop
      }
    }).id(`enigmatica2:croptopia/fermenter_${crop.replace('croptopia:', '')}`)
  })

  // ====== CROPTOPIA SEEDS → PLANT OIL ======
  // Convert all Croptopia seeds to plant oil via IE Squeezer
  const seeds = [
    'croptopia:artichoke_seed', 'croptopia:asparagus_seed', 'croptopia:bellpepper_seed', 'croptopia:blackbean_seed',
    'croptopia:blackberry_seed', 'croptopia:blueberry_seed', 'croptopia:broccoli_seed', 'croptopia:cabbage_seed',
    'croptopia:cantaloupe_seed', 'croptopia:cauliflower_seed', 'croptopia:celery_seed', 'croptopia:corn_seed',
    'croptopia:cranberry_seed', 'croptopia:cucumber_seed', 'croptopia:currant_seed', 'croptopia:eggplant_seed',
    'croptopia:elderberry_seed', 'croptopia:garlic_seed', 'croptopia:grape_seed', 'croptopia:greenbean_seed',
    'croptopia:honeydew_seed', 'croptopia:hops_seed', 'croptopia:kale_seed', 'croptopia:kiwi_seed',
    'croptopia:leek_seed', 'croptopia:lettuce_seed', 'croptopia:olive_seed', 'croptopia:onion_seed',
    'croptopia:peanut_seed', 'croptopia:pineapple_seed', 'croptopia:radish_seed', 'croptopia:raspberry_seed',
    'croptopia:rhubarb_seed', 'croptopia:rice_seed', 'croptopia:rutabaga_seed', 'croptopia:saguaro_seed',
    'croptopia:squash_seed', 'croptopia:strawberry_seed', 'croptopia:tomatillo_seed', 'croptopia:tomato_seed',
    'croptopia:turnip_seed', 'croptopia:yam_seed', 'croptopia:zucchini_seed', 'croptopia:mustard_seed',
    'croptopia:chile_pepper_seed', 'croptopia:turmeric_seed', 'croptopia:ginger_seed', 'croptopia:basil_seed',
    'croptopia:oat_seed', 'croptopia:barley_seed', 'croptopia:soybean_seed', 'croptopia:vanilla_seeds',
    'croptopia:pepper_seed', 'croptopia:tea_seed'
  ]

  seeds.forEach(seed => {
    event.custom({
      type: 'immersiveengineering:squeezer',
      energy: 6400,
      fluid: {
        amount: 60,
        fluid: 'immersiveengineering:plantoil'
      },
      input: {
        item: seed
      }
    }).id(`enigmatica2:croptopia/squeezer_${seed.replace('croptopia:', '').replace('_seed', '')}`)
  })
})
