#!/usr/bin/env python3

def main():
    values = read_values('input.txt')

    x, y, z = find_value_triplet(values)
    print(x * y * z)

def read_values(filename):
    with open(filename) as f:
        return [int(x) for x in f if x]

def find_value_triplet(values):
    for x in values:
        for y in values:
            for z in values:
                if x + y + z == 2020:
                    return (x, y, z)


if __name__ == '__main__':
    main()
