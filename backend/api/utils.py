def delete_old_ingredients(recipe):
    old_ingredients = recipe.ingredients.all()
    for old_ingredient in old_ingredients:
        if old_ingredient.recipes.count() == 1:
            old_ingredient.delete()
