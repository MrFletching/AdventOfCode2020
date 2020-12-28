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

    ingredients_without_allergens = []

    for ingredient, allergens in possible_ingredient_allergens.items():
        if not allergens:
            ingredients_without_allergens.append(ingredient)

    count = 0

    for f in foods:
        count += sum(1 for i in f.ingredients if i in ingredients_without_allergens)

    print(f'Count: {count}')





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
