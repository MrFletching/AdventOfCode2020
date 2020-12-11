#!/usr/bin/env python3

class SeatLayout:
    FLOOR = '.'
    EMPTY_SEAT = 'L'
    OCCUPIED_SEAT = '#'

    def __init__(self, rows):
        self.rows = rows
        self.width = len(self.rows[0])
        self.height = len(self.rows)
    
    def count_occupied_seats(self):
        return sum([r.count(self.OCCUPIED_SEAT) for r in self.rows])
    
    def simulate(self):
        changed = self.simulate_round()

        while changed:
            changed = self.simulate_round()
    
    def simulate_round(self):
        changed = False

        new_rows = [[' ']*self.width for row in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                new_rows[row][col] = self.get_new_state(row, col)

                if new_rows[row][col] != self.rows[row][col]:
                    changed = True

        self.rows = new_rows

        return changed
    
    def get_new_state(self, row, col):
        seat = self.rows[row][col]

        if seat == self.FLOOR:
            return self.FLOOR

        adjacent_occupied_seats = self.count_adjacent_occupied_seats(row, col)

        if seat == self.EMPTY_SEAT and adjacent_occupied_seats == 0:
            return self.OCCUPIED_SEAT
        
        if seat == self.OCCUPIED_SEAT and adjacent_occupied_seats >= 4:
            return self.EMPTY_SEAT

        return seat


    def count_adjacent_occupied_seats(self, row, col):
        min_row = max(row-1, 0)
        max_row = min(row+1, self.height-1)

        min_col = max(col-1, 0)
        max_col = min(col+1, self.width-1)

        occupied_count = 0

        for inspect_row in range(min_row, max_row+1):
            for inspect_col in range(min_col, max_col+1):
                if row == inspect_row and col == inspect_col:
                    continue

                if self.rows[inspect_row][inspect_col] == self.OCCUPIED_SEAT:
                    occupied_count += 1
        
        return occupied_count


    def print(self):
        for row in self.rows:
            print(''.join(row))
        print()


def main():
    seat_layout = read_seat_layout('input.txt')
    seat_layout.simulate()

    occupied_seats = seat_layout.count_occupied_seats()

    print(f'Occupied Seats: {occupied_seats}')


def read_seat_layout(filename):
    with open(filename) as f:
        return SeatLayout([list(l.rstrip()) for l in f])


if __name__ == '__main__':
    main()
