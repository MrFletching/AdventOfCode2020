#!/usr/bin/env python3

class Seat:

    def __init__(self, identifier):
        self.row_identifier = identifier[:7]
        self.col_identifier = identifier[7:]
    
    def get_row(self):
        return self.convert_to_val(self.row_identifier, 'B')
    
    def get_col(self):
        return self.convert_to_val(self.col_identifier, 'R')
    
    def get_seat_id(self):
        return self.get_row() * 8 + self.get_col()

    @staticmethod
    def convert_to_val(string, one_char):
        val = 0

        for char in string:
            val = val << 1
            if char == one_char:
                val += 1

        return val

def read_seats(filename):
    with open(filename) as f:
        return [Seat(line.rstrip()) for line in f]

def main():
    seats = read_seats('input.txt')

    max_seat_id = 0

    for seat in seats:
        seat_id = seat.get_seat_id()
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print(f'Max Seat ID: {max_seat_id}')

if __name__ == '__main__':
    main()
