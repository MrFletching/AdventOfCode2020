#!/usr/bin/env python3
import math
from collections import namedtuple

BusIDPosition = namedtuple('BusIDPosition', ['id', 'position'])

def main():
    bus_ids = read_bus_ids('input.txt')
    timestamp = calculate_timestamp(bus_ids)

    print(f'Earliest Timestamp: {timestamp}')

def calculate_timestamp(bus_ids):
    first_bus = bus_ids[0]

    value = first_bus.id
    add_value = first_bus.id

    bus_ids = bus_ids[1:]

    while bus_ids:

        next_bus = bus_ids.pop(0)

        while (value + next_bus.position) % next_bus.id != 0:
            value += add_value
        
        add_value *= next_bus.id

    return value


def read_bus_ids(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    earliest_timestamp = int(lines[0])
    raw_bus_ids = lines[1].split(',')

    bus_ids = []

    for index, raw_id in enumerate(raw_bus_ids):
        try:
            bus_id = int(raw_id)
        except ValueError:
            bus_id = None
        
        if bus_id:
            bus_ids.append(BusIDPosition(bus_id, index))

    return bus_ids



if __name__ == '__main__':
    main()