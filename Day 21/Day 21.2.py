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
    allergens[k] = v[0].intersection(*v[1:])

def remove_all(ingreds, tag, index):
    for k in ingreds:
        if tag in ingreds[k] and k != index:
            ingreds[k].remove(tag)

seen = set()
while any(len(i) > 1 for i in allergens.values()):
    for k, v in allergens.items():
        value = list(v)[0]
        if len(v) == 1 and value not in seen:
            seen.add(value)
            to_remove, ingred = value, k
            break

    remove_all(allergens, to_remove, ingred)

[print(k, v) for k, v in allergens.items()]
a = []
for food in sorted(allergens.keys()):
    a.append(list(allergens[food])[0])
print(",".join(a))