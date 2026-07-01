// Complete OreDictATM port for 1.20.1
// Wood and block consolidation with conversion recipes
// Only includes items from mods that exist in 1.20.1

ServerEvents.tags('item', event => {
  // ====== VANILLA WOOD CONSOLIDATION ======

  // Vanilla planks
  event.add('forge:planks', 'minecraft:oak_planks')
  event.add('forge:planks', 'minecraft:spruce_planks')
  event.add('forge:planks', 'minecraft:birch_planks')
  event.add('forge:planks', 'minecraft:jungle_planks')
  event.add('forge:planks', 'minecraft:acacia_planks')
  event.add('forge:planks', 'minecraft:dark_oak_planks')
  event.add('forge:planks', 'minecraft:mangrove_planks')
  event.add('forge:planks', 'minecraft:cherry_planks')
  event.add('forge:planks', 'minecraft:bamboo_planks')
  event.add('forge:planks', 'minecraft:crimson_planks')
  event.add('forge:planks', 'minecraft:warped_planks')

  // ====== BIOMES O' PLENTY WOOD ======
  event.add('forge:planks', 'biomesoplenty:fir_planks')
  event.add('forge:planks', 'biomesoplenty:redwood_planks')
  event.add('forge:planks', 'biomesoplenty:mahogany_planks')
  event.add('forge:planks', 'biomesoplenty:palm_planks')
  event.add('forge:planks', 'biomesoplenty:willow_planks')
  event.add('forge:planks', 'biomesoplenty:dead_planks')
  event.add('forge:planks', 'biomesoplenty:empyreal_planks')
  event.add('forge:planks', 'biomesoplenty:jacaranda_planks')
  event.add('forge:planks', 'biomesoplenty:maple_planks')
  event.add('forge:planks', 'biomesoplenty:magic_planks')
  event.add('forge:planks', 'biomesoplenty:pine_planks')
  event.add('forge:planks', 'biomesoplenty:umbran_planks')
  event.add('forge:planks', 'biomesoplenty:hellbark_planks')

  // ====== CHISEL WOOD ======
  const chiselWoodTypes = ['oak', 'spruce', 'birch', 'jungle']
  const chiselPlankVariants = [
    'braced_planks',
    'crude_horizontal_planks',
    'crude_vertical_planks',
    'encased_large_planks',
    'encased_planks',
    'large_planks',
    'vertical_planks'
  ]
  chiselWoodTypes.forEach(wood => {
    chiselPlankVariants.forEach(variant => {
      event.add('forge:planks', `chisel:planks_${wood}/${variant}`)
    })
  })

  // ====== TWILIGHT FOREST ======
  event.add('forge:planks', 'twilightforest:twilight_oak_planks')
  event.add('forge:planks', 'twilightforest:canopy_planks')
  event.add('forge:planks', 'twilightforest:mangrove_planks')
  event.add('forge:planks', 'twilightforest:dark_planks')
  event.add('forge:planks', 'twilightforest:time_planks')
  event.add('forge:planks', 'twilightforest:transformation_planks')
  event.add('forge:planks', 'twilightforest:mining_planks')
  event.add('forge:planks', 'twilightforest:sorting_planks')

  // ====== EMBERS ======
  event.add('forge:planks', 'embers:sealed_planks')

  // ====== CURRENT 1.20 WOOD FAMILIES ======
  event.add('forge:planks', 'ars_nouveau:archwood_planks')
  event.add('forge:planks', 'integrateddynamics:menril_planks')
  event.add('forge:planks', 'thermal:rubberwood_planks')

  const tconstructPlanks = [
    'tconstruct:bloodshroom_planks',
    'tconstruct:enderbark_planks',
    'tconstruct:greenheart_planks',
    'tconstruct:skyroot_planks'
  ]
  tconstructPlanks.forEach(planks => event.add('forge:planks', planks))

  const botaniaPlanks = [
    'botania:dreamwood_planks',
    'botania:livingwood_planks',
    'botania:mossy_dreamwood_planks',
    'botania:mossy_livingwood_planks',
    'botania:shimmerwood_planks'
  ]
  botaniaPlanks.forEach(planks => event.add('forge:planks', planks))

  // ====== CRAFTING TABLES ======
  event.add('forge:crafting_tables', 'minecraft:crafting_table')

  // ====== CHESTS - All Types ======
  event.add('forge:chests', 'minecraft:chest')
  event.add('forge:chests', 'minecraft:ender_chest')
  event.add('forge:chests', 'minecraft:trapped_chest')

  // Quark chests
  event.add('forge:chests', 'quark:oak_chest')
  event.add('forge:chests', 'quark:spruce_chest')
  event.add('forge:chests', 'quark:birch_chest')
  event.add('forge:chests', 'quark:jungle_chest')
  event.add('forge:chests', 'quark:acacia_chest')
  event.add('forge:chests', 'quark:dark_oak_chest')
  event.add('forge:chests', 'quark:oak_trapped_chest')
  event.add('forge:chests', 'quark:spruce_trapped_chest')
  event.add('forge:chests', 'quark:birch_trapped_chest')
  event.add('forge:chests', 'quark:jungle_trapped_chest')
  event.add('forge:chests', 'quark:acacia_trapped_chest')
  event.add('forge:chests', 'quark:dark_oak_trapped_chest')

  // Twilight Forest wood chests
  const twilightForestChests = [
    'twilightforest:twilight_oak_chest',
    'twilightforest:canopy_chest',
    'twilightforest:mangrove_chest',
    'twilightforest:dark_chest',
    'twilightforest:time_chest',
    'twilightforest:transformation_chest',
    'twilightforest:mining_chest',
    'twilightforest:sorting_chest'
  ]
  twilightForestChests.forEach(chest => event.add('forge:chests', chest))

  // ====== WOOD CHESTS ONLY ======
  event.add('forge:chests/wood', 'minecraft:chest')
  event.add('forge:chests/wood', 'minecraft:trapped_chest')
  event.add('forge:chests/wood', 'quark:oak_chest')
  event.add('forge:chests/wood', 'quark:spruce_chest')
  event.add('forge:chests/wood', 'quark:birch_chest')
  event.add('forge:chests/wood', 'quark:jungle_chest')
  event.add('forge:chests/wood', 'quark:acacia_chest')
  event.add('forge:chests/wood', 'quark:dark_oak_chest')
  event.add('forge:chests/wood', 'quark:oak_trapped_chest')
  event.add('forge:chests/wood', 'quark:spruce_trapped_chest')
  event.add('forge:chests/wood', 'quark:birch_trapped_chest')
  event.add('forge:chests/wood', 'quark:jungle_trapped_chest')
  event.add('forge:chests/wood', 'quark:acacia_trapped_chest')
  event.add('forge:chests/wood', 'quark:dark_oak_trapped_chest')

  twilightForestChests.forEach(chest => event.add('forge:chests/wood', chest))

  // ====== TRAPPED CHESTS ======
  event.add('forge:chests/trapped', 'minecraft:trapped_chest')
  event.add('forge:chests/trapped', 'quark:oak_trapped_chest')
  event.add('forge:chests/trapped', 'quark:spruce_trapped_chest')
  event.add('forge:chests/trapped', 'quark:birch_trapped_chest')
  event.add('forge:chests/trapped', 'quark:jungle_trapped_chest')
  event.add('forge:chests/trapped', 'quark:acacia_trapped_chest')
  event.add('forge:chests/trapped', 'quark:dark_oak_trapped_chest')

  // ====== BEDS ======
  event.add('forge:beds', 'minecraft:white_bed')
  event.add('forge:beds', 'minecraft:light_gray_bed')
  event.add('forge:beds', 'minecraft:gray_bed')
  event.add('forge:beds', 'minecraft:black_bed')
  event.add('forge:beds', 'minecraft:brown_bed')
  event.add('forge:beds', 'minecraft:red_bed')
  event.add('forge:beds', 'minecraft:orange_bed')
  event.add('forge:beds', 'minecraft:yellow_bed')
  event.add('forge:beds', 'minecraft:lime_bed')
  event.add('forge:beds', 'minecraft:green_bed')
  event.add('forge:beds', 'minecraft:cyan_bed')
  event.add('forge:beds', 'minecraft:light_blue_bed')
  event.add('forge:beds', 'minecraft:blue_bed')
  event.add('forge:beds', 'minecraft:purple_bed')
  event.add('forge:beds', 'minecraft:magenta_bed')
  event.add('forge:beds', 'minecraft:pink_bed')

  // ====== TRAPDOORS ======
  event.add('forge:trapdoors/wood', 'minecraft:oak_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:spruce_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:birch_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:jungle_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:acacia_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:dark_oak_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:mangrove_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:cherry_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:bamboo_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:crimson_trapdoor')
  event.add('forge:trapdoors/wood', 'minecraft:warped_trapdoor')

  // BOP trapdoors
  event.add('forge:trapdoors/wood', 'biomesoplenty:dead_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:empyreal_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:fir_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:hellbark_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:jacaranda_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:magic_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:mahogany_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:maple_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:palm_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:pine_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:redwood_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:umbran_trapdoor')
  event.add('forge:trapdoors/wood', 'biomesoplenty:willow_trapdoor')

  // Twilight Forest trapdoors
  event.add('forge:trapdoors/wood', 'twilightforest:twilight_oak_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:canopy_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:mangrove_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:dark_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:time_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:transformation_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:mining_trapdoor')
  event.add('forge:trapdoors/wood', 'twilightforest:sorting_trapdoor')

  event.add('forge:trapdoors/wood', 'ars_nouveau:archwood_trapdoor')
  event.add('forge:trapdoors/wood', 'thermal:rubberwood_trapdoor')
  event.add('forge:trapdoors/wood', 'tconstruct:bloodshroom_trapdoor')
  event.add('forge:trapdoors/wood', 'tconstruct:enderbark_trapdoor')
  event.add('forge:trapdoors/wood', 'tconstruct:greenheart_trapdoor')
  event.add('forge:trapdoors/wood', 'tconstruct:skyroot_trapdoor')

  // ====== DOORS ======
  event.add('forge:doors/wood', 'minecraft:oak_door')
  event.add('forge:doors/wood', 'minecraft:spruce_door')
  event.add('forge:doors/wood', 'minecraft:birch_door')
  event.add('forge:doors/wood', 'minecraft:jungle_door')
  event.add('forge:doors/wood', 'minecraft:acacia_door')
  event.add('forge:doors/wood', 'minecraft:dark_oak_door')
  event.add('forge:doors/wood', 'minecraft:mangrove_door')
  event.add('forge:doors/wood', 'minecraft:cherry_door')
  event.add('forge:doors/wood', 'minecraft:bamboo_door')
  event.add('forge:doors/wood', 'minecraft:crimson_door')
  event.add('forge:doors/wood', 'minecraft:warped_door')

  // BOP doors
  event.add('forge:doors/wood', 'biomesoplenty:dead_door')
  event.add('forge:doors/wood', 'biomesoplenty:empyreal_door')
  event.add('forge:doors/wood', 'biomesoplenty:fir_door')
  event.add('forge:doors/wood', 'biomesoplenty:hellbark_door')
  event.add('forge:doors/wood', 'biomesoplenty:jacaranda_door')
  event.add('forge:doors/wood', 'biomesoplenty:magic_door')
  event.add('forge:doors/wood', 'biomesoplenty:mahogany_door')
  event.add('forge:doors/wood', 'biomesoplenty:maple_door')
  event.add('forge:doors/wood', 'biomesoplenty:palm_door')
  event.add('forge:doors/wood', 'biomesoplenty:pine_door')
  event.add('forge:doors/wood', 'biomesoplenty:redwood_door')
  event.add('forge:doors/wood', 'biomesoplenty:umbran_door')
  event.add('forge:doors/wood', 'biomesoplenty:willow_door')

  // Twilight Forest doors
  event.add('forge:doors/wood', 'twilightforest:twilight_oak_door')
  event.add('forge:doors/wood', 'twilightforest:canopy_door')
  event.add('forge:doors/wood', 'twilightforest:mangrove_door')
  event.add('forge:doors/wood', 'twilightforest:dark_door')
  event.add('forge:doors/wood', 'twilightforest:time_door')
  event.add('forge:doors/wood', 'twilightforest:transformation_door')
  event.add('forge:doors/wood', 'twilightforest:mining_door')
  event.add('forge:doors/wood', 'twilightforest:sorting_door')

  event.add('forge:doors/wood', 'ars_nouveau:archwood_door')
  event.add('forge:doors/wood', 'integrateddynamics:menril_door')
  event.add('forge:doors/wood', 'thermal:rubberwood_door')
  event.add('forge:doors/wood', 'tconstruct:bloodshroom_door')
  event.add('forge:doors/wood', 'tconstruct:enderbark_door')
  event.add('forge:doors/wood', 'tconstruct:greenheart_door')
  event.add('forge:doors/wood', 'tconstruct:skyroot_door')
})

// ====== CONVERSION RECIPES ======
// Allow crafting any item from a tag into a vanilla standard item

ServerEvents.recipes(event => {
  // Any trapdoor → Oak trapdoor
  event.shapeless('minecraft:oak_trapdoor', ['#forge:trapdoors/wood'])
    .id('enigmatica2:oredict_atm/trapdoor_conversion')

  // Any trapped chest → Vanilla trapped chest
  event.shapeless('minecraft:trapped_chest', ['#forge:chests/trapped'])
    .id('enigmatica2:oredict_atm/trapped_chest_conversion')

  // Any chest → Vanilla chest
  event.shapeless('minecraft:chest', ['#forge:chests/wood'])
    .id('enigmatica2:oredict_atm/chest_conversion')

  // Any bed → White bed
  event.shapeless('minecraft:white_bed', ['#forge:beds'])
    .id('enigmatica2:oredict_atm/bed_conversion')

  // Any wood door → Oak door
  event.shapeless('minecraft:oak_door', ['#forge:doors/wood'])
    .id('enigmatica2:oredict_atm/door_conversion')
})
