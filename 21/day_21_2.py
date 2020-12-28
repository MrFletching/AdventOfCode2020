#!/usr/bin/env python3
import re

class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

def main():
    foods = read_foods('input.txt')

    ingredients = set()
    allergens = set()
    for f in foods:
        ingredients |= f.ingredients
        allergens |= f.allergens
    
    possible_ingredient_allergens = {}

    for i in ingredients:
        possible_ingredient_allergens[i] = allergens.copy()
    
    for f in foods:
        for i in ingredients:
            if i not in f.ingredients:
                possible_ingredient_allergens[i] -= f.allergens

    remaining_allergens = allergens.copy()
    allergen_ingredients = []

    while remaining_allergens:
        allergen = remaining_allergens.pop()
        first_ingredient = None

        for i in ingredients:
            if allergen in possible_ingredient_allergens[i]:
                if first_ingredient:
                    # Put it back on the list, there's more than one possibility
                    remaining_allergens.add(allergen)
                    first_ingredient = None
                    break
                else:
                    first_ingredient = i
            
        if first_ingredient:
            allergen_ingredients.append((allergen, first_ingredient))
            
            
            possible_ingredient_allergens[first_ingredient] = set()
    
    allergen_ingredients.sort(key=lambda x: x[0])

    ingredients = [ai[1] for ai in allergen_ingredients]
    print(','.join(ingredients))






def read_foods(filename):
    with open(filename) as f:
        return [parse_food_line(line) for line in f]

def parse_food_line(line):
    match = re.search(r'(.+)\(contains (.+)\)', line)

    ingredients = set(match.group(1).split())
    allergens = set(match.group(2).split(', '))

    return Food(ingredients, allergens)


if __name__ == '__main__':
    main()
