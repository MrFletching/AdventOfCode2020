#!/usr/bin/env python3
from collections import namedtuple
import math

ACTIVE = '#'
INACTIVE = '.'

class System:
    def __init__(self, state):
        self.state = state
    
    def get_bounding_cubes(self):
        mins = [math.inf,math.inf,math.inf,math.inf]
        maxs = [0,0,0,0]

        for cube in self.state:
            for dimension in range(4):
                if cube[dimension] < mins[dimension]:
                    mins[dimension] = cube[dimension]
                
                if cube[dimension] > maxs[dimension]:
                    maxs[dimension] = cube[dimension]
        
        return (tuple(mins), tuple(maxs))
    
    def do_cycle(self):
        bounding_cubes = self.get_bounding_cubes()

        new_state = set()

        for x in range(bounding_cubes[0][0] -1, bounding_cubes[1][0] + 2):
            for y in range(bounding_cubes[0][1] -1, bounding_cubes[1][1] + 2):
                for z in range(bounding_cubes[0][2] -1, bounding_cubes[1][2] + 2):
                    for w in range(bounding_cubes[0][3] -1, bounding_cubes[1][3] + 2):
                        cube = (x,y,z,w)
                        if self.is_cube_active(cube):
                            new_state.add(cube)
        
        self.state = new_state
    
    def is_cube_active(self, cube):
        active_neighbours = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        
                        if (cube[0] + dx, cube[1] + dy, cube[2] + dz, cube[3] + dw) in self.state:
                            active_neighbours += 1

        if cube in self.state:
            return active_neighbours == 2 or active_neighbours == 3
        else:
            return active_neighbours == 3

    def print_state(self):
        bounding_cubes = self.get_bounding_cubes()

        new_state = set()

        for w in range(bounding_cubes[0][3], bounding_cubes[1][3] + 1):
            for z in range(bounding_cubes[0][2], bounding_cubes[1][2] + 1):
                print(f'z={z}, w={w}')

                for y in range(bounding_cubes[0][1], bounding_cubes[1][1] + 1):
                    for x in range(bounding_cubes[0][0], bounding_cubes[1][0] + 1):
                        cube = (x,y,z)
                        if cube in self.state:
                            print(ACTIVE, end='')
                        else:
                            print(INACTIVE, end='')
                    
                    print()
                
                print()
    
    def count_active_cubes(self):
        return len(self.state)
            


def main():
    state = read_initial_state('input.txt')
    system = System(state)

    # system.print_state()
    for i in range(6):
        system.do_cycle()

    active_cubes = system.count_active_cubes()
    print(f'Active Cubes: {active_cubes}')


def read_initial_state(filename):
    state = set()

    y = 0
    z = 0
    w = 0

    with open(filename) as f:
        for line in f:
            x = 0
            for char in line:
                if char == ACTIVE:
                    state.add((x, y, z, w))
                x += 1
            y += 1
    
    return state


if __name__ == '__main__':
    main()
