// OreDict replacements using current 1.20.1 item IDs.

ServerEvents.tags('item', event => {
  event.add('forge:tools/forge_hammer', 'immersiveengineering:hammer')

  const boats = [
    'minecraft:oak_boat',
    'minecraft:spruce_boat',
    'minecraft:birch_boat',
    'minecraft:jungle_boat',
    'minecraft:acacia_boat',
    'minecraft:dark_oak_boat',
    'minecraft:mangrove_boat',
    'minecraft:cherry_boat',
    'biomesoplenty:dead_boat',
    'biomesoplenty:empyreal_boat',
    'biomesoplenty:fir_boat',
    'biomesoplenty:hellbark_boat',
    'biomesoplenty:jacaranda_boat',
    'biomesoplenty:magic_boat',
    'biomesoplenty:mahogany_boat',
    'biomesoplenty:maple_boat',
    'biomesoplenty:palm_boat',
    'biomesoplenty:pine_boat',
    'biomesoplenty:redwood_boat',
    'biomesoplenty:umbran_boat',
    'biomesoplenty:willow_boat',
    'immersivepetroleum:speedboat'
  ]
  boats.forEach(boat => event.add('forge:boats', boat))

  event.add('forge:raw_meats', 'twilightforest:raw_venison')
  event.add('forge:cooked_meats', 'twilightforest:cooked_venison')

  const bloodRunes = [
    'bloodmagic:blankrune',
    'bloodmagic:selfsacrificerune',
    'bloodmagic:sacrificerune',
    'bloodmagic:speedrune',
    'bloodmagic:altarcapacityrune',
    'bloodmagic:altarcapacityrune2',
    'bloodmagic:bettercapacityrune',
    'bloodmagic:bettercapacityrune2',
    'bloodmagic:orbcapacityrune',
    'bloodmagic:orbcapacityrune2',
    'bloodmagic:chargingrune',
    'bloodmagic:chargingrune2',
    'bloodmagic:dislocationrune',
    'bloodmagic:dislocationrune2',
    'bloodmagic:accelerationrune',
    'bloodmagic:accelerationrune2',
    'bloodmagic:sacrificerune2',
    'bloodmagic:selfsacrificerune2',
    'bloodmagic:speedrune2'
  ]
  bloodRunes.forEach(rune => event.add('forge:runes/blood', rune))

  event.add('forge:foods/cake', 'minecraft:cake')

  event.add('forge:gems/quartz', 'minecraft:quartz')
  event.add('forge:gems/apatite', 'thermal:apatite')
  event.add('forge:gems/certus_quartz', 'ae2:certus_quartz_crystal')
  event.add('forge:gems/certus_quartz', 'ae2:charged_certus_quartz_crystal')

  event.add('forge:storage_blocks/certus_quartz', 'ae2:quartz_block')
  event.add('forge:storage_blocks/certus_quartz', 'ae2:quartz_pillar')
  event.add('forge:storage_blocks/certus_quartz', 'ae2:chiseled_quartz_block')

  event.add('forge:stones/marble', 'chisel:marble/raw')
  event.add('forge:stones/mazestone', 'twilightforest:mazestone')
  event.add('forge:stones/mazestone', 'twilightforest:mazestone_brick')
})
