#!/usr/bin/env python3

def main():
    rules = read_rules('input.txt')

    bags_inside_shiny_gold = count_bags_inside('shiny gold', rules)

    print(f'Bags inside shiny gold bag: {bags_inside_shiny_gold}')

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

def count_bags_inside(bag_type, rules):
    rule = next((r for r in rules if r['outer_bag_type'] == bag_type))

    count = 0

    for inner_bag in rule['inner_bags']:
        count += inner_bag['quantity'] * (count_bags_inside(inner_bag['type'], rules) + 1)
    
    return count


if __name__ == '__main__':
    main()