# Lost Cities Config Port Notes

Compared old E2 1.12 `config/lostcities/*.cfg` against current Lost Cities 1.20 profile JSONs.

## Ported Values

- `config/lostcities/profiles/default.json`
  - `cities.cityChance`: `0.01` -> `0.02`
  - Explosion profile restored to old E2 values: `explosionChance = 0.005`, `miniExplosionChance = 0.07`, `explosionMaxRadius = 50`, `explosionMinRadius = 17`, `miniExplosionMaxRadius = 15`.
- `config/lostcities/profiles/wasteland.json`
  - Same city density and explosion-radius/chance values as old E2 `profile_wasteland.cfg`.
- `config/lostcities/profiles/safe.json`
  - Same city density and explosion-radius/chance values as old E2 `profile_safe.cfg`.
- `config/lostcities/profiles/atlantis.json`
  - Same city density and explosion-radius/chance values as old E2 `profile_atlantis.cfg`.
- `config/lostcities/profiles/rarecities.json`
  - `cities.cityChance`: `0.001` -> `0.002`
  - Explosion profile restored to old E2 rare-city values.
- `config/lostcities/profiles/onlycities.json`
  - City values already matched old E2; explosion profile restored to old E2 values.
- `config/lostcities/profiles/tallbuildings.json`
  - `cities.cityChance`: `0.01` -> `0.02`
  - `explosions.explosionChance`: `0.006` -> `0.008`
  - `explosions.explosionMinRadius`: `15` -> `17`
- `config/lostcities/profiles/nodamage.json`
  - `cities.cityChance`: `0.01` -> `0.02`
  - Kept no-damage explosion chances at `0.0`, but restored old E2 radius values still exposed by the schema.
- `config/lostcities/profiles/ancient.json`
  - Same no-damage handling as `nodamage.json`.
- `config/lostcities/profiles/cavern.json`
  - `cities.cityChance`: `0.01` -> `0.02`
- `config/lostcities/profiles/space.json`
  - `cities.cityChance`: `0.699999988079071` -> `0.6`
- `config/lostcities/profiles/biosphere.json`
  - `cities.cityMaxRadius`: `65` -> `90`
  - `cities.cityChance`: `0.800000011920929` -> `0.7`

## Not Ported

- Old `general.cfg` dimension ID/profile list settings do not map directly to current namespaced dimension profile config. Current `config/lostcities/common.toml` already points generated Lost Cities dimensions at biosphere-style profiles.
- Old `chisel`, `realistic`, `waterbubbles`, and `water_empty` profile configs do not have direct current profile files in this pack.
- Current 1.20-only profiles such as `largecities`, `void_outside`, and `biosphere_caves` were left at generated/current values.
- BOP old GUI/default-world-type settings were not ported; modern BOP no longer exposes a direct default-world-type config in the tracked common/generation config.
