#!/usr/bin/env python3

def main():
    adapters = read_adapters('input.txt')

    built_in_adapter = max(adapters) + 3
    adapters.append(built_in_adapter)

    joltage_difference_counts = {
        1: 0,
        2: 0,
        3: 0,
    }

    last_joltage = 0

    for joltage in range(built_in_adapter + 1):
        if joltage in adapters:
            joltage_difference = joltage - last_joltage
            joltage_difference_counts[joltage_difference] += 1
            last_joltage = joltage
    
    result = joltage_difference_counts[1] * joltage_difference_counts[3]
    print(f'Result: {result}')


def read_adapters(filename):
    with open(filename) as f:
        return [int(l) for l in f]


if __name__ == '__main__':
    main()
