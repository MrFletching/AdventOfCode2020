#!/usr/bin/env python3

def main():
    groups = read_groups('input.txt')

    total_count = 0

    for group in groups:
        everyone_answered = group[0]

        for person_answers in group:
            everyone_answered = everyone_answered & person_answers

        total_count += len(everyone_answered)

    print(f'Total Count: {total_count}')

def read_groups(filename):
    groups = []

    with open(filename) as f:
        answers = f.read()

    groups_answers = answers.split('\n\n')

    for group_answers in groups_answers:
        people_answers_raw = group_answers.split('\n')

        people_answers = []

        for person_answers_raw in people_answers_raw:
            people_answers_raw = person_answers_raw.strip()
            person_answers = set(person_answers_raw)
            people_answers.append(person_answers)

        groups.append(people_answers)

    return groups

if __name__ == '__main__':
    main()