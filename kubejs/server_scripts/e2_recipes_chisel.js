// Chisel recipe adjustments for 1.20.1
// Note: Original script attempted to add chisel variations; most source items no longer exist

ServerEvents.recipes(event => {
  // Original script added chisel variations:
  // - basalt (quark, IC2) — IC2 not in pack; quark basalt exists but variations already available
  // - marble (quark) — quark marble exists; variations already available
  // - limestone (quark) — quark limestone exists; variations already available
  // - sootymarble (astral sorcery) — Astral Sorcery not in 1.20.1 pack; retired
  // - castlebrickrune (twilight forest) — Castle rune brick doesn't exist in TF 1.20.1; retired
  // - castlebrickdoor (twilight forest) — Castle door doesn't exist in TF 1.20.1; retired
  //
  // In 1.20.1, chisel variations are loaded natively from registered blocks.
  // No manual registration via KubeJS is needed or possible.
  // The variations (chisel:basalt/*, chisel:marble/*, etc.) are available by default.
})
