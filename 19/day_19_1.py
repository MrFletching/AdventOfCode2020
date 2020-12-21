#!/usr/bin/env python3

def main():
    rules, messages = read_input('input.txt')
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
    does_match, next_index = does_message_match_rule(rules, message)

    # Only valid if there is nothing else
    return does_match and next_index == len(message)

def does_message_match_rule(rules, message, rule_id=0, start_index=0):
    rule = rules[rule_id]
    message_part = message[start_index:]

    if type(rule) is str:
        if message_part[0] == rule:
            return True, start_index+1
        else:
            return False, None
    else:
        for rule_part in rule:
            current_index = start_index

            for rule_id in rule_part:
                does_match, current_index = does_message_match_rule(rules, message, rule_id, current_index)

                if not does_match:
                    break
            
            if does_match:
                return True, current_index
        
        return False, None


if __name__ == '__main__':
    main()
