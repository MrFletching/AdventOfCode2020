#!/usr/bin/env python3

LIST_SIZE = 25

def main():
    stream = read_stream('input.txt')
    
    first_invalid = find_first_invalid(stream)

    encryption_weakness = find_encryption_weakness(stream, first_invalid)

    print(f'Encryption weakness: {encryption_weakness}')

def read_stream(filename):
    with open(filename) as f:
        return [int(l) for l in f]

def find_first_invalid(stream):
    start_index = LIST_SIZE

    for i in range(start_index, len(stream)):
        if not is_valid(stream, i):
            return stream[i]

def is_valid(stream, index):
    start_index = index - LIST_SIZE

    number = stream[index]
    prev_numbers = stream[start_index:index]

    for i in range(LIST_SIZE-1):
        i_number = prev_numbers[i]
        for j in range(i+1, LIST_SIZE):
            j_number = prev_numbers[j]
            if i_number + j_number == number:
                return True
    
    return False

def find_encryption_weakness(stream, target):
    start_index = 0
    end_index = 1

    while (start_index < len(stream) - 1) and (end_index < len(stream) - 1):
        region = stream[start_index:end_index+1]
        total = sum(region)
        
        if total < target:
            end_index += 1
        elif total > target:
            start_index += 1
        else:
            return min(region) + max(region)



if __name__ == '__main__':
    main()