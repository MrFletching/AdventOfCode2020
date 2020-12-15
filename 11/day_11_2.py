#!/usr/bin/env python3

class SeatLayout:
    FLOOR = '.'
    EMPTY_SEAT = 'L'
    OCCUPIED_SEAT = '#'

    def __init__(self, rows):
        self.rows = rows
        self.width = len(self.rows[0])
        self.height = len(self.rows)
        self.build_visible_map()
    
    def build_visible_map(self):
        self.visible_map = []

        for row in range(self.height):
            row_visible_map = []

            for col in range(self.width):
                visible_seats = self.get_visible_seats(row, col)
                row_visible_map.append(visible_seats)

            self.visible_map.append(row_visible_map)

    def get_visible_seats(self, row, col):
        visible_cells = []
        for delta_x in [-1,0,1]:
            for delta_y in [-1, 0, 1]:

                if delta_x == 0 and delta_y == 0:
                    continue

                x = col + delta_x
                y = row + delta_y

                while x >= 0 and x < self.width and y >= 0 and y < self.height:

                    if self.rows[y][x] != self.FLOOR:
                        visible_cells.append((y, x))
                        break
                    
                    x += delta_x
                    y += delta_y
        
        return visible_cells

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
        
        if seat == self.OCCUPIED_SEAT and adjacent_occupied_seats >= 5:
            return self.EMPTY_SEAT

        return seat


    def count_adjacent_occupied_seats(self, row, col):
        occupied_count = 0

        visible_seats = self.visible_map[row][col]

        for seat in visible_seats:
            row = seat[0]
            col = seat[1]
            if self.rows[row][col] == self.OCCUPIED_SEAT:
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
