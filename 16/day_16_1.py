#!/usr/bin/env python3
from __future__ import annotations
from typing import List
import re

Ticket = List[int]

class Range:
    def __init__(self, from_value: int, to_value: int):
        self.from_value = from_value
        self.to_value = to_value
    
    def includes(self, value: int) -> bool:
        return (value >= self.from_value) and (value <= self.to_value)
    
    def __str__(self):
        return f'{self.from_value}-{self.to_value}'


class Rule:
    def __init__(self, field: str, range1: Range, range2: Range):
        self.field = field
        self.range1 = range1
        self.range2 = range2
    
    def matches(self, value) -> bool:
        return self.range1.includes(value) or self.range2.includes(value)
    
    def __str__(self):
        return f'{self.field}: {self.range1} or {self.range2}'


class Notes:
    def __init__(self):
        self.rules: List[Rule] = []
        self.my_ticket: Ticket = None
        self.nearby_tickets: List[Ticket] = []
    
    def add_rule(self, rule: Rule):
        self.rules.append(rule)
    
    def set_my_ticket(self, my_ticket: Ticket):
        self.my_ticket = my_ticket
    
    def add_nearby_ticket(self, nearby_ticket: Ticket):
        self.nearby_tickets.append(nearby_ticket)

    @staticmethod
    def read(filename: str) -> Notes:
        notes = Notes()
        with open(filename) as f:
            raw_notes = f.read()
        
        notes_sections = [section.rstrip() for section in raw_notes.split('\n\n')]
        rules_section = notes_sections[0].split('\n')
        my_ticket_section = notes_sections[1].split('\n')
        nearby_tickets_section = notes_sections[2].split('\n')

        for rule_line in rules_section:
            rule = Notes.parse_rule(rule_line)
            notes.add_rule(rule)
        
        my_ticket = Notes.parse_ticket(my_ticket_section[1])
        notes.set_my_ticket(my_ticket)

        for ticket_line in nearby_tickets_section[1:]:
            ticket = Notes.parse_ticket(ticket_line)
            notes.add_nearby_ticket(ticket)
        
        return notes

    @staticmethod
    def parse_rule(line: str) -> Rule:
        match = re.search(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        field = match.group(1)
        range1_from = int(match.group(2))
        range1_to   = int(match.group(3))
        range2_from = int(match.group(4))
        range2_to   = int(match.group(5))

        range1 = Range(range1_from, range1_to)
        range2 = Range(range2_from, range2_to)

        return Rule(field, range1, range2)
    
    @staticmethod
    def parse_ticket(line: str) -> Ticket:
        return [int(v) for v in line.split(',')]



def main():
    notes = Notes.read('input.txt')

    total = 0

    for ticket in notes.nearby_tickets:
        total += sum_invalid_fields(ticket, notes.rules)
    
    print(f'Ticket scanning error rate: {total}')


def sum_invalid_fields(ticket: Ticket, rules: List[Rule]):
    total = 0

    for value in ticket:
        matches_a_rule = False

        for rule in rules:
            if rule.matches(value):
                matches_a_rule = True
                break

        if not matches_a_rule:
            total += value
    
    return total



if __name__ == '__main__':
    main()
