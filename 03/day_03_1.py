#!/usr/bin/env python3

OPEN = '.'
TREE = '#'

def main():
    map = read_map('input.txt')
    trees = count_trees(map)
    print(trees)

def read_map(filename):
    with open(filename) as f:
        return [l.rstrip() for l in f]

def count_trees(map):
    x = 0
    y = 0

    map_width = len(map[0])

    count = 0

    while y < len(map):
        if map[y][x] == TREE:
            count += 1

        x = (x + 3) % map_width
        y += 1
    
    return count

if __name__ == '__main__':
    main()