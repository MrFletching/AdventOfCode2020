#!/usr/bin/env python3

def main():
    rules = read_rules('input.txt')

    contains_shiny_gold_count = 0

    for rule in rules:
        outer_bag_type = rule['outer_bag_type']
        if contains_bag(outer_bag_type, 'shiny gold', rules):
            contains_shiny_gold_count += 1

    print(f'Bags that contain shiny gold: {contains_shiny_gold_count}')

def read_rules(filename):
    with open(filename) as f:
        return [parse_rule(line.strip()) for line in f]

def parse_rule(rule_string):
    rule_string_parts = rule_string.split(' contain ', 2)
    outer_bag = parse_bag_type(rule_string_parts[0])

    inner_bags_string = rule_string_parts[1]

    if inner_bags_string == 'no other bags.':
        inner_bags = []
    else:
        inner_bags_split = inner_bags_string.split(',')
        inner_bags = list(map(parse_bag_quantity_type, inner_bags_split))

    return {
        'outer_bag_type': outer_bag,
        'inner_bags': inner_bags
    }

def parse_bag_type(string):
    string_parts = string.split()
    return ' '.join(string_parts[0:2])

def parse_bag_quantity_type(string):
    string_parts = string.split()

    return {
        'quantity': int(string_parts[0]),
        'type': ' '.join(string_parts[1:3])
    }

def contains_bag(outer_bag_type, search_bag_type, rules):
    rule = next((r for r in rules if r['outer_bag_type'] == outer_bag_type))

    for inner_bag in rule['inner_bags']:
        if inner_bag['type'] == search_bag_type:
            return True
        
        if contains_bag(inner_bag['type'], search_bag_type, rules):
            return True
    
    return False


if __name__ == '__main__':
    main()