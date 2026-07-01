ServerEvents.recipes(event => {
  const vanillaOresAndOutputs = {
    'minecraft:gold_ore': 'minecraft:gold_ingot',
    'minecraft:raw_gold': 'minecraft:gold_ingot',
    'minecraft:deepslate_gold_ore': 'minecraft:gold_ingot',
    'minecraft:iron_ore': 'minecraft:iron_ingot',
    'minecraft:raw_iron': 'minecraft:iron_ingot',
    'minecraft:deepslate_iron_ore': 'minecraft:iron_ingot',
    'minecraft:coal_ore': 'minecraft:coal',
    'minecraft:deepslate_coal_ore': 'minecraft:coal',
    'minecraft:lapis_ore': 'minecraft:lapis_lazuli',
    'minecraft:deepslate_lapis_ore': 'minecraft:lapis_lazuli',
    'minecraft:diamond_ore': 'minecraft:diamond',
    'minecraft:deepslate_diamond_ore': 'minecraft:diamond',
    'minecraft:redstone_ore': 'minecraft:redstone',
    'minecraft:deepslate_redstone_ore': 'minecraft:redstone',
    'minecraft:emerald_ore': 'minecraft:emerald',
    'minecraft:deepslate_emerald_ore': 'minecraft:emerald',
    'minecraft:nether_quartz_ore': 'minecraft:quartz'
  }

  for (const [ore, output] of Object.entries(vanillaOresAndOutputs)) {
    event.remove({ type: 'minecraft:smelting', input: ore })
    event.smelting(output, ore).xp(1).id(`enigmatica2:furnace/${ore.split(':')[1]}`)
  }
})
