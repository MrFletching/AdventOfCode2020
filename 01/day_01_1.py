#!/usr/bin/env python3

def main():
    values = read_values('input.txt')

    x, y = find_value_pair(values)

    print(x * y)

def read_values(filename):
    with open(filename) as f:
        return [int(x) for x in f if x]

def find_value_pair(values):
    for x in values:
        y = 2020 - x
        if y in values:
            return (x, y)
    return


if __name__ == '__main__':
    main()
