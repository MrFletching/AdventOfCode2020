#!/usr/bin/env python3
from collections import namedtuple

Instruction = namedtuple('Instruction', ['direction', 'magnitude'])

class Ship:
    def __init__(self):
        self.x = 0 # Positive is East
        self.y = 0 # Positive is North
        self.angle = 0 # East, positive is clockwise
    
    def move(self, instruction):
        if instruction.direction == 'N':
            self.y += instruction.magnitude
        if instruction.direction == 'S':
            self.y -= instruction.magnitude
        if instruction.direction == 'E':
            self.x += instruction.magnitude
        if instruction.direction == 'W':
            self.x -= instruction.magnitude
        if instruction.direction == 'L':
            self.angle += instruction.magnitude
            self.angle %= 360
        if instruction.direction == 'R':
            self.angle -= instruction.magnitude
            self.angle %= 360
        if instruction.direction == 'F':
            self.move_forward(instruction.magnitude)
    
    def move_forward(self, magnitude):
        if self.angle == 0:
            self.x += magnitude
        if self.angle == 90:
            self.y += magnitude
        if self.angle == 180:
            self.x -= magnitude
        if self.angle == 270:
            self.y -= magnitude
    
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)



def main():
    instructions = read_instructions('input.txt')

    ship = Ship()

    for instruction in instructions:
        ship.move(instruction)
    
    dist = ship.manhattan_distance()

    print(f'Manhattan distance: {dist}')
    


def read_instructions(filename):
    instructions = []
    with open(filename) as f:
        for line in f:
            direction = line[0]
            magnitude = int(line[1:])
            instructions.append(Instruction(direction, magnitude))
    return instructions





if __name__ == '__main__':
    main()
