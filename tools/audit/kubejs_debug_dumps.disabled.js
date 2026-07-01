// Experimental local debug helper. Do not leave this enabled during normal play.
//
// Prefer `/kubejs dump_registry minecraft:item` plus stdout-log parsing for
// item IDs. In the current imported instance, JsonIO.write(...) logged success
// but did not produce visible files.
//
// To use:
// 1. Copy this file to the imported instance as kubejs/server_scripts/z_audit_dumps.js
// 2. Run /reload
// 3. Check kubejs/config/ for audit_item_ids.json and audit_recipe_ids.json
// 4. Delete z_audit_dumps.js before continuing normal testing

ServerEvents.recipes(event => {
  const ForgeRegistries = Java.loadClass('net.minecraftforge.registries.ForgeRegistries')

  const itemLines = []
  const itemIds = ForgeRegistries.ITEMS.getKeys().iterator()
  while (itemIds.hasNext()) {
    itemLines.push(String(itemIds.next()))
  }
  itemLines.sort()
  JsonIO.write('kubejs/config/audit_item_ids.json', itemLines)
  console.log(`[E2 Audit] Wrote ${itemLines.length} item IDs to kubejs/config/audit_item_ids.json`)

  const recipeLines = ['id,type,output']
  event.forEachRecipe({}, recipe => {
    let id = String(recipe.getId())
    let type = String(recipe.getType())
    let output = ''
    try {
      output = String(recipe.getOriginalRecipeResult())
    } catch (ignored) {
      output = ''
    }
    recipeLines.push(`${id},${type},${output}`)
  })
  JsonIO.write('kubejs/config/audit_recipe_ids.json', recipeLines)
  console.log(`[E2 Audit] Wrote ${recipeLines.length - 1} recipe IDs to kubejs/config/audit_recipe_ids.json`)
})
