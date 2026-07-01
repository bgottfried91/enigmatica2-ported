#!/usr/bin/env bash
set -euo pipefail

memory_mb="${1:-10240}"
profile="${2:-}"
instances_root="${INSTANCES_ROOT:-/mnt/i/minecraft/Instances}"
name_glob="${PROFILE_GLOB:-Enigmatica 2 Ported*}"

if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required but was not found on PATH." >&2
  exit 1
fi

if [[ ! "$memory_mb" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 [memory_mb] [profile_path]" >&2
  echo "Example: $0 10240" >&2
  echo "Example: $0 12288 '/mnt/i/minecraft/Instances/Enigmatica 2 Ported (1)'" >&2
  exit 1
fi

if [[ -z "$profile" ]]; then
  profile="$(
    find "$instances_root" -maxdepth 2 -name minecraftinstance.json -path "*/$name_glob/minecraftinstance.json" -printf '%T@ %h\n' |
      sort -n |
      tail -1 |
      cut -d' ' -f2-
  )"
fi

if [[ -z "$profile" || ! -f "$profile/minecraftinstance.json" ]]; then
  echo "Could not find a CurseForge profile matching '$name_glob' under '$instances_root'." >&2
  exit 1
fi

instance_json="$profile/minecraftinstance.json"
tmp_file="$(mktemp "$instance_json.tmp.XXXXXX")"

jq --argjson memory "$memory_mb" '
  .allocatedMemory = $memory |
  .isMemoryOverride = true |
  .memoryAllocatedType = 1
' "$instance_json" > "$tmp_file"

mv "$tmp_file" "$instance_json"

echo "Set CurseForge memory override to ${memory_mb} MB:"
echo "$profile"
