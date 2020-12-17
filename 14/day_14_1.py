#!/usr/bin/env python3
import re
from abc import ABC, abstractmethod

class Instruction(ABC):
    @abstractmethod
    def run_on(self):
        pass

class MaskInstruction(Instruction):
    def __init__(self, mask):
        self.mask = mask
    
    def run_on(self, system):
        system.set_mask(self.mask)

class MemInstruction(Instruction):
    def __init__(self, address, value):
        self.address = address
        self.value = value
    
    def run_on(self, system):
        system.store_value(self.address, self.value)

class System:
    def __init__(self):
        self.zero_mask = 0
        self.one_mask = 0
        self.memory = {}
    
    def run(self, program):
        for instruction in program:
            instruction.run_on(self)
    
    def store_value(self, address, value):
        masked_value = self.mask_value(value)
        self.memory[address] = masked_value

    def mask_value(self, value):
        return (value | self.one_mask) & ~self.zero_mask

    def set_mask(self, mask):
        self.zero_mask = 0
        self.one_mask = 0

        for pos, char in enumerate(mask[::-1]):
            if char == '0':
                self.zero_mask += 1 << pos
            elif char == '1':
                self.one_mask += 1 << pos
    
    def sum_memory(self):
        return sum(self.memory.values())

            

def main():
    program = read_program('input.txt')
    
    system = System()
    system.run(program)

    sum_memory = system.sum_memory()
    print(f'Sum of Memory: {sum_memory}')




def read_program(filename):
    with open(filename) as f:
        return [parse_instruction(line) for line in f]

def parse_instruction(line):
    match = re.search(r'^mask = ([X01]{36})$', line)

    if match:
        return MaskInstruction(match.group(1))
    
    match = re.search(r'^mem\[(\d+)\] = (\d+)$', line)

    if match:
        return MemInstruction(int(match.group(1)), int(match.group(2)))
    
    raise TypeError(f'Invalid Instruction: {line}')


if __name__ == '__main__':
    main()
