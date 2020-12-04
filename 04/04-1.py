#!/usr/bin/env python3

REQUIRED_FIELDS = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
]

def main():
    passports = read_passports('input.txt')

    valid_passports = [p for p in passports if is_valid(p)]
    print(f'Valid Passports: {len(valid_passports)}')

def read_passports(filename):
    f = open(filename)
    data = f.read()

    passport_strings = data.split('\n\n')

    passports = []
    
    for passport_string in passport_strings:
        passport = parse_passport_string(passport_string)
        passports.append(passport)
    
    return passports

def parse_passport_string(passport_string):
    key_values = passport_string.split()

    passport = {}

    for key_value in key_values:
        key, value = key_value.split(':', 1)
        passport[key] = value
    
    return passport

def is_valid(passport):
    for f in REQUIRED_FIELDS:
        if f not in passport:
            return False
    return True

if __name__ == '__main__':
    main()
