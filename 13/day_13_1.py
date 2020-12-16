#!/usr/bin/env python3
import math

def main():
    earliest_timestamp, bus_ids = read_input('input.txt')

    earliest_bus_id = None
    earliest_bus_timestamp = None

    for bus_id in bus_ids:
        next_bus = math.ceil(earliest_timestamp / bus_id) * bus_id
        print(f'Bus {bus_id}: {next_bus}')

        if (not earliest_bus_timestamp) or (next_bus < earliest_bus_timestamp):
            earliest_bus_id = bus_id
            earliest_bus_timestamp = next_bus
    
    print(f'Earliest Bus: {earliest_bus_id}')
    print(f'Next Timestamp: {earliest_bus_timestamp}')

    wait = earliest_bus_timestamp - earliest_timestamp

    print(f'Wait time: {wait}')

    result = earliest_bus_id * wait

    print(f'Result: {result}')


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    earliest_timestamp = int(lines[0])
    bus_ids = lines[1].split(',')
    bus_ids = [int(i) for i in bus_ids if i != 'x']

    return (earliest_timestamp, bus_ids)



if __name__ == '__main__':
    main()