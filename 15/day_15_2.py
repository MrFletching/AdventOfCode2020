#!/usr/bin/env python3

def main():
    numbers = read_starting_numbers('input.txt')
    number_last_turn = {}
    turn = 1

    last_number = None

    for number in numbers:
        if last_number is not None:
            number_last_turn[last_number] = turn - 1

        last_number = number
        turn += 1

    while turn <= 30000000:
        next_number = get_next_number(number_last_turn, last_number, turn - 1)
        number_last_turn[last_number] = turn - 1
        last_number = next_number
        turn += 1
    
    print(f'Turn {turn-1}: {last_number}')


def get_next_number(number_last_turn, last_number, last_number_turn):
    if last_number in number_last_turn:
        return last_number_turn - number_last_turn[last_number]

    return 0



def read_starting_numbers(filename):
    with open(filename) as f:
        data = f.readline()

    numbers = data.split(',')
    numbers = [int(n) for n in numbers]
    return numbers



if __name__ == '__main__':
    main()
