#!/usr/bin/env python3
import re

def main():
    passwords = read_passwords('input.txt')

    valid_passwords = list(filter(is_valid, passwords))
    valid_count = len(valid_passwords)
    print(valid_count)

def read_passwords(filename):
    passwords = []
    with open(filename) as f:
        for line in f:
            if line:
                password = parse_line(line)
                passwords.append(password)

    return passwords

def parse_line(line):
    match = re.search("^(\d+)-(\d+) (.): (.*)$", line)
    return {
        'min': int(match.group(1)),
        'max': int(match.group(2)),
        'char': match.group(3),
        'password': match.group(4)
    }

def is_valid(password):
    char_count = password['password'].count(password['char'])
    return char_count >= password['min'] and char_count <= password['max']

if __name__ == '__main__':
    main()