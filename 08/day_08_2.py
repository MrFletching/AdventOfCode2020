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
        while not self.is_finished() and not self.ran_instructions[self.instruction_pointer]:
            self.ran_instructions[self.instruction_pointer] = True
            self.run_next_instruction()
    
    def is_finished(self):
        return self.instruction_pointer == len(self.program)


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

    for instruction_index in range(len(program)):
        instruction = program[instruction_index]

        if instruction.operation not in ['nop', 'jmp']:
            continue

        modified_program = program.copy()

        new_operation = 'nop' if instruction.operation == 'jmp' else 'jmp'

        modified_program[instruction_index] = Instruction(operation=new_operation, argument=instruction.argument)

        computer = Computer(modified_program)
        computer.run_until_loop()

        if computer.is_finished():
            print('Finished!')
            break

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