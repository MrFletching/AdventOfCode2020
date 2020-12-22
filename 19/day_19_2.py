#!/usr/bin/env python3

def main():
    rules, messages = read_input('input.txt')
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    valid_count = sum(is_valid_message(rules, m) for m in messages)
    print(f'Valid messages: {valid_count}')

def read_input(filename):
    with open(filename) as f:
        data = f.read().rstrip()
    
    rules_section, messages_section = data.split('\n\n')

    raw_rules = rules_section.split('\n')
    messages = messages_section.split('\n')

    rules = {}

    for raw_rule in raw_rules:
        rule_split = raw_rule.split(': ')
        rule_id = int(rule_split[0])
        rule_def = rule_split[1]

        if rule_def[0] == '"':
            rule_def = rule_def.replace('"', '')
        else:
            rule_parts = rule_def.split('|')
            rule_def = [[int(v) for v in p.split()] for p in rule_parts]

        rules[rule_id] = rule_def

    return rules, messages


def is_valid_message(rules, message):
    new_possible_indices = does_message_match_rule(rules, message)

    # Only valid if there is nothing else
    valid = len(message) in new_possible_indices

    # print(f'{message}: {valid}')
    return valid

def does_message_match_rule(rules, message, rule_id=0, start_index=0, depth=0):
    rule = rules[rule_id]
    message_part = message[start_index:]

    indent = '    ' * depth
    # print(f'{indent}Testing {message_part} against {rule_id}')

    if type(rule) is str:
        if message_part and message_part[0] == rule:
            # print(f'{indent}Match')
            return [start_index+1]
        else:
            # print(f'{indent}No Match')
            return []
    else:

        all_next_indices = []

        for rule_part in rule:
            current_indices = [start_index]

            for rule_part_id in rule_part:
                # print(f'{indent}Rule: {rule_part_id}, Indices: {current_indices}')
                next_indices = []

                for current_index in current_indices:
                    new_possible_indices = does_message_match_rule(rules, message, rule_part_id, current_index, depth+1)
                    next_indices += new_possible_indices
                current_indices = next_indices
            
            all_next_indices += next_indices

        if all_next_indices:
                return all_next_indices
        
        return []


if __name__ == '__main__':
    main()
