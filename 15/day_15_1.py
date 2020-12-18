#!/usr/bin/env python3

def main():
    numbers = read_starting_numbers('input.txt')

    while len(numbers) != 2020:
        next_number = get_next_number(numbers)
        numbers.append(next_number)

        turn = len(numbers)

    print(f'Turn {turn}: {next_number}')


def get_next_number(numbers):
    last_number = numbers[-1]
    numbers_reversed = numbers[-2::-1]

    for pos, num in enumerate(numbers_reversed):
        if num == last_number:
            return pos + 1

    return 0





def read_starting_numbers(filename):
    with open(filename) as f:
        data = f.readline()

    numbers = data.split(',')
    numbers = [int(n) for n in numbers]
    return numbers



if __name__ == '__main__':
    main()
