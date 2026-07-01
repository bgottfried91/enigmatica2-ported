// Thermal Bottler recipes that replace old 1.12 Fluid Transposer integrations.

ServerEvents.recipes(event => {
  event.custom({
    type: 'thermal:bottler',
    ingredients: [
      { tag: 'forge:dusts/electrum' },
      { fluid: 'thermal:redstone', amount: 500 }
    ],
    result: [
      { item: 'redstone_arsenal:flux_dust' }
    ],
    energy: 2000
  }).id('enigmatica2:thermal/bottler/flux_dust')

  event.custom({
    type: 'thermal:bottler',
    ingredients: [
      { tag: 'forge:gems/diamond' },
      { fluid: 'thermal:redstone', amount: 500 }
    ],
    result: [
      { item: 'redstone_arsenal:flux_gem' }
    ],
    energy: 2000
  }).id('enigmatica2:thermal/bottler/flux_gem')
})
