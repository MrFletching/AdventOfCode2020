#!/usr/bin/env python3

cup_labels = '614752839'

def main():
    cups = [int(c) for c in cup_labels]

    current_cup_index = 0

    for move in range(100):
        print(f'-- move {move+1} --')
        current_cup = cups[current_cup_index]

        cups_str = ''
        for cup_index, cup in enumerate(cups):
            if cup_index == current_cup_index:
                cups_str += f'({cup}) '
            else:
                cups_str += f'{cup} '
        
        print(f'cups: {cups_str}')

        next_cups_indexes = []

        next_cups_indexes.append((current_cup_index + 1) % len(cups))
        next_cups_indexes.append((current_cup_index + 2) % len(cups))
        next_cups_indexes.append((current_cup_index + 3) % len(cups))

        next_cups = [
            cups[next_cups_indexes[0]],
            cups[next_cups_indexes[1]],
            cups[next_cups_indexes[2]]
        ]

        next_cups_indexes.sort()

        cups.pop(next_cups_indexes[2])
        cups.pop(next_cups_indexes[1])
        cups.pop(next_cups_indexes[0])

        next_cups_str = ', '.join([str(c) for c in next_cups])
        print(f'pick up: {next_cups_str}')

        cups_placed = False

        destination_cup = current_cup

        while not cups_placed:
            destination_cup -= 1
            if destination_cup < min(cups):
                destination_cup = max(cups)
            
            try:
                destination_cup_index = cups.index(destination_cup)
                cups_placed = True
            except ValueError:
                pass

        print(f'destination: {destination_cup}')

        cups = cups[:destination_cup_index+1] + next_cups + cups[destination_cup_index+1:]

        current_cup_index = cups.index(current_cup)
        current_cup_index = (current_cup_index + 1) % len(cups)

        print()


    ordered_cups = ''

    one_index = cups.index(1)

    for i in range(len(cups) - 1):
        cup_index = (one_index + i + 1) % len(cups)
        ordered_cups += str(cups[cup_index])

    print(ordered_cups)

if __name__ == '__main__':
    main()
