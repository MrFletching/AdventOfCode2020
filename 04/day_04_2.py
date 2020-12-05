#!/usr/bin/env python3
import re

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

    if not is_int_between(passport['byr'], 1920, 2002):
        return False

    if not is_int_between(passport['iyr'], 2010, 2020):
        return False

    if not is_int_between(passport['eyr'], 2020, 2030):
        return False

    hgt_unit = passport['hgt'][-2:]
    hgt_value = passport['hgt'][:-2]

    if hgt_unit not in ['cm', 'in']:
        return False

    if hgt_unit == 'cm' and not is_int_between(hgt_value, 150, 193):
        return False
    
    if hgt_unit == 'in' and not is_int_between(hgt_value, 59, 76):
        return False

    if not re.match('^#[0-9a-f]{6}$', passport['hcl']):
        return False
    
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    if not re.match('^\d{9}$', passport['pid']):
        return False

    return True

def is_int_between(val_str, val_min, val_max):
    try:
        val = int(val_str)
    except ValueError:
        return False
    
    return val >= val_min and val <= val_max

if __name__ == '__main__':
    main()
