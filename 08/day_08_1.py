#!/usr/bin/env python3
from collections import namedtuple

Instruction = namedtuple('Instruction', ['operation', 'argument'])

class Computer:

    def __init__(self, program):
        self.program = program
        self.accumulator = 0
        self.instruction_pointer = 0
        self.ran_instructions = [False for instruction in program]

        self.operation_functions = {
            'nop': lambda arg: None,
            'acc': self.run_acc,
            'jmp': self.run_jmp
        }

    def run_until_loop(self):
        while not self.ran_instructions[self.instruction_pointer]:
            self.ran_instructions[self.instruction_pointer] = True
            self.run_next_instruction()

    def run_next_instruction(self):
        instruction = self.program[self.instruction_pointer]

        instruction_func = self.operation_functions[instruction.operation]
        instruction_func(instruction.argument)

        if instruction.operation != 'jmp':
            self.instruction_pointer += 1
    
    def run_acc(self, arg):
        self.accumulator += arg
    
    def run_jmp(self, arg):
        self.instruction_pointer += arg


def main():
    program = read_program('input.txt')

    computer = Computer(program)
    computer.run_until_loop()

    print(f'Accumulator: {computer.accumulator}')

def read_program(filename):
    program = []

    with open(filename) as f:
        for line in f:
            program.append(parse_instruction(line))

    return program

def parse_instruction(line):
    parts = line.split()
    return Instruction(operation=parts[0], argument=int(parts[1]))


if __name__ == '__main__':
    main()