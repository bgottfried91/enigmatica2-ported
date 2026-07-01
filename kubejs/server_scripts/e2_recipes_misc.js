// Miscellaneous recipes for Enigmatica 2 - 1.20.1
// Various crafting recipes and material conversions

ServerEvents.recipes(event => {
  // ====== VANILLA RECIPES ======

  // Bread recipe for Minecolony bakers
  event.shaped('minecraft:bread', [
    'GGG'
  ], {
    G: '#forge:crops/wheat'
  }).id('enigmatica2:misc/bread')

  // String removal (prevent crafting)
  event.remove({ output: 'minecraft:string', input: '#minecraft:wool' })

  // Nametag from paper and flax
  event.shaped('minecraft:name_tag', [
    ' PF',
    'PDP',
    'PP '
  ], {
    P: '#forge:paper',
    F: '#forge:crops/flax',
    D: '#forge:dyes/black'
  }).id('enigmatica2:misc/nametag')

  // Elytra crafting
  event.shaped('minecraft:elytra', [
    'BLB',
    'BCB',
    'D D'
  ], {
    B: 'minecraft:black_banner',
    L: 'minecraft:leather_chestplate',
    C: 'minecraft:popped_chorus_fruit',
    D: 'actuallyadditions:diamatine_crystal'
  }).id('enigmatica2:misc/elytra')

  // Boats from planks
  event.shaped('minecraft:oak_boat', [
    'P P',
    'PPP'
  ], {
    P: '#minecraft:planks'
  }).id('enigmatica2:misc/boat')

  // ====== WOOL DYEING - Any 8 wool + dye = 8 dyed wool ======
  // Individual explicit recipes for each color (for debugging)

  event.shaped('8x minecraft:white_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/white'
  }).id('enigmatica2:misc/wool_white')

  event.shaped('8x minecraft:orange_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/orange'
  }).id('enigmatica2:misc/wool_orange')

  event.shaped('8x minecraft:magenta_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/magenta'
  }).id('enigmatica2:misc/wool_magenta')

  event.shaped('8x minecraft:light_blue_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/light_blue'
  }).id('enigmatica2:misc/wool_light_blue')

  event.shaped('8x minecraft:yellow_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/yellow'
  }).id('enigmatica2:misc/wool_yellow')

  event.shaped('8x minecraft:lime_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/lime'
  }).id('enigmatica2:misc/wool_lime')

  event.shaped('8x minecraft:pink_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/pink'
  }).id('enigmatica2:misc/wool_pink')

  event.shaped('8x minecraft:gray_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/gray'
  }).id('enigmatica2:misc/wool_gray')

  event.shaped('8x minecraft:light_gray_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/light_gray'
  }).id('enigmatica2:misc/wool_light_gray')

  event.shaped('8x minecraft:cyan_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/cyan'
  }).id('enigmatica2:misc/wool_cyan')

  event.shaped('8x minecraft:purple_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/purple'
  }).id('enigmatica2:misc/wool_purple')

  event.shaped('8x minecraft:blue_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/blue'
  }).id('enigmatica2:misc/wool_blue')

  event.shaped('8x minecraft:brown_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/brown'
  }).id('enigmatica2:misc/wool_brown')

  event.shaped('8x minecraft:green_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/green'
  }).id('enigmatica2:misc/wool_green')

  event.shaped('8x minecraft:red_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/red'
  }).id('enigmatica2:misc/wool_red')

  event.shaped('8x minecraft:black_wool', [
    'WWW',
    'WDW',
    'WWW'
  ], {
    W: '#minecraft:wool',
    D: '#forge:dyes/black'
  }).id('enigmatica2:misc/wool_black')

  // ====== URANIUM BLOCK ======

  event.shaped('immersiveengineering:storage_uranium', [
    'UUU',
    'UUU',
    'UUU'
  ], {
    U: '#forge:ingots/uranium'
  }).id('enigmatica2:misc/uranium_block')

  event.shapeless('9x immersiveengineering:ingot_uranium', ['#forge:storage_blocks/uranium'])
    .id('enigmatica2:misc/uranium_ingots')

  // ====== BOOKSHELF CONVERSION ======

  event.shapeless('minecraft:bookshelf', ['#forge:bookshelves'])
    .id('enigmatica2:misc/bookshelf_conversion')

  // ====== TORCHMASTER ======

  event.remove({ output: 'torchmaster:megatorch' })
  event.shaped('torchmaster:megatorch', [
    'III',
    'DLD',
    'MMM'
  ], {
    I: 'immersiveengineering:treated_wood_horizontal',
    D: '#forge:storage_blocks/diamond',
    L: '#minecraft:logs',
    M: '#forge:storage_blocks/iron'
  }).id('enigmatica2:misc/mega_torch')

  // ====== FARMING FOR BLOCKHEADS ======

  event.remove({ output: 'farmingforblockheads:market' })
  event.shaped('farmingforblockheads:market', [
    'PWP',
    'LEL',
    'LLL'
  ], {
    P: '#minecraft:planks',
    W: '#minecraft:wool',
    L: '#minecraft:logs',
    E: '#forge:storage_blocks/emerald'
  }).id('enigmatica2:misc/farming_market')

  // ====== BIOMES O' PLENTY ======

  event.shaped('16x biomesoplenty:origin_grass_block', [
    'SGS',
    'OOO',
    'SGS'
  ], {
    S: '#minecraft:sand',
    G: 'minecraft:grass_block',
    O: 'biomesoplenty:origin_sapling'
  }).id('enigmatica2:misc/bop_origin_grass')

  // ====== CHEST CONVERSION - Any 2 chests → 2 vanilla chests ======

  event.shapeless('2x minecraft:chest', ['#forge:chests/wood', '#forge:chests/wood'])
    .id('enigmatica2:misc/chest_conversion')

  // ====== SHAPELESS RECIPES ======

  // Bronze from ingots
  event.shapeless('thermal:bronze_ingot', ['#forge:ingots/copper', '#forge:ingots/copper', '#forge:ingots/copper', '#forge:ingots/tin'])
    .id('enigmatica2:misc/bronze_ingot')

  // ====== HIDE NUGGETS ======
  event.remove({ output: 'immersiveengineering:nugget_copper' })
  event.remove({ output: 'embers:copper_nugget' })
  event.remove({ output: 'embers:lead_nugget' })
  event.remove({ output: 'embers:silver_nugget' })

  // Note: Removed recipes:
  // - Uranium storage block (doesn't exist in IE 1.20.1)
  // - Quark marble wall (no marble in Quark 1.20.1)
  // - BOP loamy/sandy dirt (no longer exist in BOP 1.20.1)
  // - Environmental Tech recipes (mod doesn't exist)
})
