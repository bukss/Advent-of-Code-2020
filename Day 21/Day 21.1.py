from aoc_utils import load_raw
import re
from collections import defaultdict

f = load_raw()
allergens = defaultdict(list)
allergen_ingredients = set()

for recipe in f.splitlines():
    try:
        alls = re.search(r"\(contains (.*)\)", recipe).group(1).split(", ")
    except:
        continue
    
    recipe = re.sub(r"\(contains .*\)", "", recipe)
    foods = set(recipe.split())
    [allergens[allergy].append(foods) for allergy in alls]

for k, v in allergens.items():
    ingreds = v[0].intersection(*v[1:])
    allergen_ingredients = allergen_ingredients.union(ingreds)

def count_ingreds(ingred):
    return f.split().count(ingred)

nonallergen_counts = {}
for food in f.splitlines():
    food = re.sub(r"\(contains .*\)", "", food)
    ingredients = food.split()
    for ingredient in ingredients:
        if ingredient not in allergen_ingredients:
            nonallergen_counts[ingredient] = count_ingreds(ingredient)

print(sum(nonallergen_counts.values()))