// Fluid compatibility recipes for Enigmatica 2 - 1.20.1

ServerEvents.recipes(event => {
  const moltenCompat = [
    {
      material: 'refined_obsidian',
      fluid: 'tconstruct:molten_refined_obsidian',
      fluidTag: 'forge:molten_refined_obsidian',
      energy: {
        nugget: 500,
        ingot: 5000,
        block: 40000
      }
    },
    {
      material: 'refined_glowstone',
      fluid: 'tconstruct:molten_refined_glowstone',
      fluidTag: 'forge:molten_refined_glowstone',
      energy: {
        nugget: 500,
        ingot: 5000,
        block: 40000
      }
    }
  ]

  const forms = [
    { form: 'nugget', tag: 'nuggets', amount: 10 },
    { form: 'ingot', tag: 'ingots', amount: 90 },
    { form: 'block', tag: 'storage_blocks', amount: 810 }
  ]

  moltenCompat.forEach(material => {
    forms.forEach(form => {
      const itemTag = `forge:${form.tag}/${material.material}`

      event.custom({
        type: 'thermal:crucible',
        ingredient: {
          tag: itemTag
        },
        result: [
          {
            fluid: material.fluid,
            amount: form.amount
          }
        ],
        energy: material.energy[form.form]
      }).id(`enigmatica2:fluid_compatibility/thermal_crucible/${material.material}_${form.form}`)

      event.custom({
        type: 'nuclearcraft:melter',
        input: [
          {
            tag: itemTag
          }
        ],
        outputFluids: [
          {
            amount: form.amount,
            tag: material.fluidTag
          }
        ],
        powerModifier: 1.0,
        radiation: 1.0,
        timeModifier: 1.0
      }).id(`enigmatica2:fluid_compatibility/nuclearcraft_melter/${material.material}_${form.form}`)
    })
  })
})
