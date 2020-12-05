#!/usr/bin/env python3

OPEN = '.'
TREE = '#'

def main():
    map = read_map('input.txt')

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    result = 1

    for slope in slopes:
        trees = count_trees(map, slope)
        result *= trees

    print(result)

def read_map(filename):
    with open(filename) as f:
        return [l.rstrip() for l in f]

def count_trees(map, slope):
    x = 0
    y = 0

    map_width = len(map[0])

    count = 0

    while y < len(map):
        if map[y][x] == TREE:
            count += 1

        x = (x + slope[0]) % map_width
        y += slope[1]
    
    return count

if __name__ == '__main__':
    main()