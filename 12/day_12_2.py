#!/usr/bin/env python3
from collections import namedtuple

Instruction = namedtuple('Instruction', ['direction', 'magnitude'])

class Ship:
    def __init__(self):
        self.x = 0 # Positive is East
        self.y = 0 # Positive is North
        self.waypoint_x = 10
        self.waypoint_y = 1
    
    def move(self, instruction):
        if instruction.direction == 'N':
            self.waypoint_y += instruction.magnitude
        elif instruction.direction == 'S':
            self.waypoint_y -= instruction.magnitude
        elif instruction.direction == 'E':
            self.waypoint_x += instruction.magnitude
        elif instruction.direction == 'W':
            self.waypoint_x -= instruction.magnitude
        elif instruction.direction == 'L':
            self.rotate_waypoint(instruction.magnitude)
        elif instruction.direction == 'R':
            self.rotate_waypoint(-instruction.magnitude % 360)
        elif instruction.direction == 'F':
            self.move_forward(instruction.magnitude)
    
    def rotate_waypoint(self, degrees):
        if degrees == 90:
            temp_x = self.waypoint_x
            self.waypoint_x = -self.waypoint_y
            self.waypoint_y = temp_x
        elif degrees == 180:
            self.waypoint_x = -self.waypoint_x
            self.waypoint_y = -self.waypoint_y
        elif degrees == 270:
            temp_x = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = -temp_x

    def move_forward(self, magnitude):
        self.x += self.waypoint_x * magnitude
        self.y += self.waypoint_y * magnitude
    
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
