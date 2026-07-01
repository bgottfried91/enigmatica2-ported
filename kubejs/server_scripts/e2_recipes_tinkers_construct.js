// Tinkers' Construct compatibility for the E2 1.20.1 port.
// Retired from the 1.12 script: tconstruct:rack no longer exists, Chisel cobalt
// no longer owns the canonical cobalt block, and removed-mod fuels are absent.

ServerEvents.recipes(event => {
  event.custom({
    type: 'tconstruct:alloy',
    inputs: [
      {
        amount: 90,
        tag: 'forge:molten_iron'
      },
      {
        amount: 125,
        fluid: 'jaopca:molten.coal'
      }
    ],
    result: {
      amount: 90,
      tag: 'forge:molten_steel'
    },
    temperature: 1000
  }).id('enigmatica2:tconstruct/alloys/molten_steel')

  const fuels = [
    {
      id: 'sulfuric_acid',
      fluid: { amount: 25, tag: 'forge:sulfuric_acid' },
      duration: 400,
      rate: 10,
      temperature: 4000
    },
    {
      id: 'refined_fuel',
      fluid: { amount: 25, fluid: 'thermal:refined_fuel' },
      duration: 600,
      rate: 15,
      temperature: 4100
    },
    {
      id: 'diesel',
      fluid: { amount: 25, tag: 'forge:diesel' },
      duration: 400,
      rate: 10,
      temperature: 3900
    },
    {
      id: 'gasoline',
      fluid: { amount: 25, tag: 'forge:gasoline' },
      duration: 400,
      rate: 10,
      temperature: 3900
    }
  ]

  fuels.forEach(fuel => {
    event.custom({
      type: 'tconstruct:melting_fuel',
      duration: fuel.duration,
      fluid: fuel.fluid,
      rate: fuel.rate,
      temperature: fuel.temperature
    }).id(`enigmatica2:tconstruct/fuels/${fuel.id}`)
  })
})
