#!/usr/bin/env python3

def main():
    groups = read_groups('input.txt')

    total_count = 0

    for group in groups:
        unique_answers = set(''.join(group))
        total_count += len(unique_answers)

    print(f'Total Count: {total_count}')

def read_groups(filename):
    groups = []

    with open(filename) as f:
        answers = f.read()

    groups_answers = answers.split('\n\n')

    for group_answers in groups_answers:
        people_answers = group_answers.split('\n')
        people_answers = list(filter(None, people_answers))
        groups.append(people_answers)

    return groups

if __name__ == '__main__':
    main()