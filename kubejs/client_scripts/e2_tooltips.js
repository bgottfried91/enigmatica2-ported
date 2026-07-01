// Tooltips ported from the original E2 scripts where the target items still exist.

ItemEvents.tooltip(event => {
  event.add('bloodmagic:defaultdemoncrystal', 'Obtained through the Gathering of the Forsaken Souls ritual.')

  const resonanceCrystals = [
    'bloodmagic:corrosivedemoncrystal',
    'bloodmagic:destructivedemoncrystal',
    'bloodmagic:steadfastdemoncrystal',
    'bloodmagic:vengefuldemoncrystal'
  ]

  resonanceCrystals.forEach(item => {
    event.add(item, 'Obtained through the Resonance of the Faceted Crystal ritual.')
  })
})
