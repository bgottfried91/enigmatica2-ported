// Hide duplicate items whose recipes are removed by the E2 compatibility scripts.

JEIEvents.hideItems(event => {
  const hiddenItems = [
    'mekanismtools:bronze_pickaxe',
    'mekanismtools:bronze_axe',
    'mekanismtools:bronze_shovel',
    'mekanismtools:bronze_hoe',
    'mekanismtools:bronze_sword',
    'mekanismtools:bronze_helmet',
    'mekanismtools:bronze_chestplate',
    'mekanismtools:bronze_leggings',
    'mekanismtools:bronze_boots',
    'mekanismtools:steel_pickaxe',
    'mekanismtools:steel_axe',
    'mekanismtools:steel_shovel',
    'mekanismtools:steel_hoe',
    'mekanismtools:steel_sword',
    'mekanismtools:steel_helmet',
    'mekanismtools:steel_chestplate',
    'mekanismtools:steel_leggings',
    'mekanismtools:steel_boots',
    'embers:copper_plate',
    'embers:lead_plate',
    'embers:silver_plate',
    'embers:iron_plate',
    'immersiveengineering:plate_constantan',
    'immersiveengineering:plate_copper',
    'immersiveengineering:plate_electrum',
    'immersiveengineering:plate_gold',
    'immersiveengineering:plate_iron',
    'immersiveengineering:plate_lead',
    'immersiveengineering:plate_nickel',
    'immersiveengineering:plate_silver'
  ]

  hiddenItems.forEach(item => event.hide(item))
})
