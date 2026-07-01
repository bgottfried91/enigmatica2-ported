// Startup-only item property changes from the original E2 scripts.
// These require a full game restart; /reload is not enough.

ItemEvents.modification(event => {
  const tierInstallers = [
    'mekanism:basic_tier_installer',
    'mekanism:advanced_tier_installer',
    'mekanism:elite_tier_installer',
    'mekanism:ultimate_tier_installer'
  ]

  tierInstallers.forEach(itemId => {
    event.modify(itemId, item => {
      item.maxStackSize = 16
    })
  })

  const mekanismUpgrades = [
    'mekanism:upgrade_energy',
    'mekanism:upgrade_filter',
    'mekanism:upgrade_muffling',
    'mekanism:upgrade_speed'
  ]

  mekanismUpgrades.forEach(itemId => {
    event.modify(itemId, item => {
      item.maxStackSize = 64
    })
  })

  event.modify('cyclic:mattock', item => {
    item.maxDamage = 4500
  })
})
