// Cross-mod food ingredient tags for Croptopia recipes.

ServerEvents.tags('item', event => {
  const addMany = (tag, items) => {
    items.forEach(item => event.add(tag, item))
  }

  addMany('forge:butters', [
    'minecolonies:butter'
  ])

  addMany('forge:cheeses', [
    'minecolonies:cheddar_cheese',
    'minecolonies:creamcheese',
    'minecolonies:feta_cheese',
    'thermal:cheese_wedge',
    'tconstruct:cheese_ingot'
  ])

  addMany('forge:milks', [
    'minecolonies:large_milk_bottle',
    'minecolonies:large_soy_milk_bottle'
  ])

  addMany('forge:tofu', [
    'minecolonies:tofu'
  ])

  addMany('forge:soy_sauces', [
    'minecolonies:soysauce'
  ])

  addMany('forge:tortillas', [
    'minecolonies:tortillas'
  ])

  addMany('forge:noodles', [
    'minecolonies:raw_noodle'
  ])

  addMany('forge:yoghurts', [
    'minecolonies:yogurt'
  ])

  addMany('croptopia:meat_replacements', [
    'minecolonies:tofu'
  ])

  addMany('croptopia:pork_replacements', [
    'tconstruct:bacon'
  ])

  addMany('forge:rice', [
    'minecolonies:rice',
    'thermal:rice'
  ])
  addMany('forge:grain/rice', [
    'minecolonies:rice',
    'thermal:rice'
  ])
  addMany('forge:crops/rice', [
    'minecolonies:rice'
  ])

  addMany('forge:corn', [
    'minecolonies:corn',
    'thermal:corn'
  ])
  addMany('forge:grain/corn', [
    'minecolonies:corn',
    'thermal:corn'
  ])
  addMany('forge:crops/corn', [
    'minecolonies:corn'
  ])

  addMany('forge:tomatoes', [
    'minecolonies:tomato',
    'thermal:tomato'
  ])
  addMany('forge:vegetables/tomato', [
    'minecolonies:tomato',
    'thermal:tomato'
  ])
  addMany('forge:crops/tomato', [
    'minecolonies:tomato'
  ])

  addMany('forge:onions', [
    'minecolonies:onion',
    'thermal:onion'
  ])
  addMany('forge:vegetables/onion', [
    'minecolonies:onion',
    'thermal:onion'
  ])
  addMany('forge:crops/onion', [
    'minecolonies:onion'
  ])

  addMany('forge:garlic', [
    'minecolonies:garlic'
  ])
  addMany('forge:vegetables/garlic', [
    'minecolonies:garlic'
  ])
  addMany('forge:crops/garlic', [
    'minecolonies:garlic'
  ])

  addMany('forge:cabbage', [
    'minecolonies:cabbage'
  ])
  addMany('forge:vegetables/cabbage', [
    'minecolonies:cabbage'
  ])
  addMany('forge:crops/cabbage', [
    'minecolonies:cabbage'
  ])

  addMany('forge:eggplants', [
    'minecolonies:eggplant',
    'thermal:eggplant'
  ])
  addMany('forge:vegetables/eggplant', [
    'minecolonies:eggplant',
    'thermal:eggplant'
  ])
  addMany('forge:crops/eggplant', [
    'minecolonies:eggplant'
  ])

  addMany('forge:bellpeppers', [
    'minecolonies:bell_pepper',
    'thermal:bell_pepper'
  ])
  addMany('forge:fruits/bellpepper', [
    'minecolonies:bell_pepper',
    'thermal:bell_pepper'
  ])
  addMany('forge:crops/bellpepper', [
    'minecolonies:bell_pepper',
    'thermal:bell_pepper'
  ])

  addMany('forge:soybeans', [
    'minecolonies:soybean'
  ])
  addMany('forge:vegetables/soybean', [
    'minecolonies:soybean'
  ])
  addMany('forge:crops/soybean', [
    'minecolonies:soybean'
  ])

  addMany('forge:squashes', [
    'minecolonies:butternut_squash'
  ])
  addMany('forge:vegetables/squash', [
    'minecolonies:butternut_squash'
  ])
  addMany('forge:crops/squash', [
    'minecolonies:butternut_squash'
  ])

  addMany('forge:barley', [
    'thermal:barley'
  ])

  addMany('forge:greenbeans', [
    'thermal:green_bean'
  ])
  addMany('forge:vegetables/greenbean', [
    'thermal:green_bean'
  ])
  addMany('forge:crops/greenbean', [
    'thermal:green_bean'
  ])

  addMany('forge:spinach', [
    'thermal:spinach'
  ])
  addMany('forge:vegetables/spinach', [
    'thermal:spinach'
  ])

  addMany('forge:strawberries', [
    'thermal:strawberry'
  ])
  addMany('forge:fruits/strawberry', [
    'thermal:strawberry'
  ])

  addMany('forge:peanuts', [
    'thermal:peanut'
  ])
  addMany('forge:nuts', [
    'thermal:peanut'
  ])

  addMany('forge:radishes', [
    'thermal:radish'
  ])
  addMany('forge:vegetables/radish', [
    'thermal:radish'
  ])

  addMany('forge:hops', [
    'thermal:hops'
  ])

  addMany('forge:coffee_beans', [
    'thermal:coffee'
  ])

  addMany('forge:tea_leaves', [
    'thermal:tea'
  ])
})
