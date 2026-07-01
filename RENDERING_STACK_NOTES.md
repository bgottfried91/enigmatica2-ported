# Rendering Stack Notes

This pack is Forge 1.20.1, so the shader stack uses Oculus rather than the
upstream Iris mod. Iris does not publish Forge builds for this target; Oculus is
the Forge/FML port of Iris.

## Added

- Embeddium: client-side Sodium-derived renderer/performance mod.
- Oculus: client-side Iris-compatible shader loader for Forge/FML.
- Distant Horizons: long-distance LOD renderer. Packwiz selected a shared
  Fabric/Forge 1.20.1 jar.
- Bliss Shaders: packaged as a Packwiz-managed shaderpack under
  `shaderpacks/bliss-shader.pw.toml`.

## Compatibility Notes

- Do not add upstream Iris to this Forge instance. Use Oculus for Forge 1.20.1.
- Distant Horizons shader support requires modern Iris-compatible shader support
  and a shaderpack that is built with Distant Horizons support in mind.
- Bliss supports Iris/OptiFine-style shader loading and 1.20.x, but it still
  needs in-game validation with Distant Horizons enabled.
- Oculus/Embeddium are client-side. Distant Horizons can run client-side only,
  or on both client and server to provide server-sent LOD data.

## Recommended First-Run Checks

1. Confirm the game reaches the title screen with Embeddium, Oculus, and Distant
   Horizons installed together.
2. Open Video Settings and confirm the Embeddium video settings UI is present.
3. Open Shader Packs and select Bliss.
4. In Distant Horizons settings, start conservatively:
   - Enable Distant Horizons rendering.
   - Use a moderate LOD distance first, then increase after confirming stability.
   - Let LODs build before judging visual seams or performance.
5. Test a normal overworld view, Nether, and a modded-machine-heavy base.
6. If shader horizon/LOD blending looks wrong, first test with shaders disabled,
   then test Bliss with lower DH quality/distance before assuming a mod conflict.

## Optional Follow-Up Mods

These are plausible additions after the core stack is stable:

- ImmediatelyFast: lightweight client rendering optimization. Usually low risk.
- Entity Culling: can improve rendering performance, but may need config
  whitelists for modded block entities or entities with unusual render bounds.

Do not add Rubidium or Sodium alongside Embeddium.
