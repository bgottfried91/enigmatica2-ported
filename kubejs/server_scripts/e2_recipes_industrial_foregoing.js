// Industrial Foregoing BioReactor compatibility for the E2 1.20.1 port.
// Modern IF reads BioReactor inputs from the industrialforegoing:bioreactor item tag.

ServerEvents.tags('item', event => {
  const bioreactorInputs = [
    'minecraft:apple', 'minecraft:beetroot', 'minecraft:beetroot_seeds', 'minecraft:carrot',
    'minecraft:melon_seeds', 'minecraft:potato', 'minecraft:pumpkin_seeds',
    'minecraft:sweet_berries', 'minecraft:wheat', 'minecraft:wheat_seeds',

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
    'croptopia:banana', 'croptopia:cashew', 'croptopia:cherry', 'croptopia:cinnamon',
    'croptopia:coconut', 'croptopia:coffee_beans', 'croptopia:date', 'croptopia:dragonfruit',
    'croptopia:fig', 'croptopia:grapefruit', 'croptopia:lemon', 'croptopia:lime',
    'croptopia:mango', 'croptopia:nectarine', 'croptopia:orange', 'croptopia:peach',
    'croptopia:pear', 'croptopia:pecan', 'croptopia:persimmon', 'croptopia:plum',
    'croptopia:walnut',

    'croptopia:artichoke_seed', 'croptopia:asparagus_seed', 'croptopia:bellpepper_seed',
    'croptopia:blackbean_seed', 'croptopia:blackberry_seed', 'croptopia:blueberry_seed',
    'croptopia:broccoli_seed', 'croptopia:cabbage_seed', 'croptopia:cantaloupe_seed',
    'croptopia:cauliflower_seed', 'croptopia:celery_seed', 'croptopia:corn_seed',
    'croptopia:cranberry_seed', 'croptopia:cucumber_seed', 'croptopia:currant_seed',
    'croptopia:eggplant_seed', 'croptopia:elderberry_seed', 'croptopia:garlic_seed',
    'croptopia:grape_seed', 'croptopia:greenbean_seed', 'croptopia:honeydew_seed',
    'croptopia:hops_seed', 'croptopia:kale_seed', 'croptopia:kiwi_seed',
    'croptopia:leek_seed', 'croptopia:lettuce_seed', 'croptopia:olive_seed',
    'croptopia:onion_seed', 'croptopia:peanut_seed', 'croptopia:pineapple_seed',
    'croptopia:radish_seed', 'croptopia:raspberry_seed', 'croptopia:rhubarb_seed',
    'croptopia:rice_seed', 'croptopia:rutabaga_seed', 'croptopia:saguaro_seed',
    'croptopia:squash_seed', 'croptopia:strawberry_seed', 'croptopia:tomatillo_seed',
    'croptopia:tomato_seed', 'croptopia:turnip_seed', 'croptopia:yam_seed',
    'croptopia:zucchini_seed', 'croptopia:mustard_seed', 'croptopia:chile_pepper_seed',
    'croptopia:turmeric_seed', 'croptopia:ginger_seed', 'croptopia:basil_seed',
    'croptopia:oat_seed', 'croptopia:barley_seed', 'croptopia:soybean_seed',
    'croptopia:vanilla_seeds', 'croptopia:pepper_seed', 'croptopia:tea_seed'
  ]

  bioreactorInputs.forEach(item => event.add('industrialforegoing:bioreactor', item))
})
