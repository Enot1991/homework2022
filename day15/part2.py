import re



def compute_score(recipe, ingredients):
    score = 1
    for i in range(4):
        attribute_score = 0
        for k, v in recipe.items():
            if v > 0:
                attribute_score += ingredients[k][i] * v
        attribute_score = max(attribute_score, 0)
        score *= attribute_score
    return score



def get_calories(recipe, ingredients):
    calories = 0
    for k, v in recipe.items():
        calories += ingredients[k][4] * v
    return calories



def add_ingredient(recipe, ingredients, cal_target):
    if len(recipe) == len(ingredients):
        return recipe
    max_score_recipe = None
    existing_spoons = 0
    for k, v in ingredients.items():
        if k in recipe:
            existing_spoons += recipe[k]
            continue
        max_score = None
        for i in range(1, min(40, 101 - existing_spoons)):
            recipe[k] = i
            if cal_target is not None and get_calories(recipe, ingredients) > cal_target:
                break
            recipe_copy = recipe.copy()
            add_ingredient(recipe_copy, ingredients, cal_target)
            if cal_target is not None and get_calories(recipe_copy, ingredients) != cal_target:
                continue
            score = compute_score(recipe_copy, ingredients)
            if max_score is None or score > max_score:
                max_score = score
                max_score_recipe = recipe_copy
        break
    if max_score_recipe is not None:
        for k, v in max_score_recipe.items():
            recipe[k] = v
    return recipe



input_pattern = r'(\w*): capacity ([-]?\d*), durability ([-]?\d*), flavor ([-]?\d*), texture ([-]?\d*), calories ([-]?\d*)'
ingredients = dict()
for line in open("input.txt"):
    match = re.match(input_pattern, line.strip())
    name = match.group(1)
    ingredients[name] = (int(match[2]), int(match[3]), int(match[4]), int(match[5]), int(match[6]))



recipe = add_ingredient({}, ingredients, 500)
f2 = open("output2.txt", "w")
f2.write(str(compute_score(recipe, ingredients)))
f2.close
