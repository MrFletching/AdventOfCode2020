#!/usr/bin/env python3
import unittest
from day_05_1 import Seat

class SeatTest(unittest.TestCase):

    def setUp(self):
        self.seats = [
            {'seat': Seat('FBFBBFFRLR'), 'row': 44, 'col': 5, 'seat_id': 357},
            {'seat': Seat('BFFFBBFRRR'), 'row': 70, 'col': 7, 'seat_id': 567},
            {'seat': Seat('FFFBBBFRRR'), 'row': 14, 'col': 7, 'seat_id': 119},
            {'seat': Seat('BBFFBBFRLL'), 'row': 102, 'col': 4, 'seat_id': 820},
        ]

    def test_convert_to_val(self):
        self.assertEqual(Seat.convert_to_val('FBFBBFF', 'B'), 44)
        self.assertEqual(Seat.convert_to_val('RLR', 'R'), 5)

    def test_get_row(self):
        for s in self.seats:
            self.assertEqual(s['seat'].get_row(), s['row'])

    def test_get_col(self):
        for s in self.seats:
            self.assertEqual(s['seat'].get_col(), s['col'])

    def test_get_seat_id(self):
        for s in self.seats:
            self.assertEqual(s['seat'].get_seat_id(), s['seat_id'])

if __name__ == '__main__':
    unittest.main()
