#!/usr/bin/env python3

class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.rows = rows
        self.width = len(self.rows[0])
        self.height = len(self.rows)
        self.set_orientation(0)
    
    def set_orientation(self, orientation):
        self.oriented_rows = [[' '] * self.width for i in range(self.height)]

        self.flipped = orientation // 4 == 1
        
        self.rotation = orientation % 4

        for y in range(self.width):
            for x in range(self.height):

                if self.rotation == 0:
                    old_x = x
                    old_y = y
                
                elif self.rotation == 1:
                    old_x = self.height - y - 1
                    old_y = x

                elif self.rotation == 2:
                    old_x = self.width - x - 1
                    old_y = self.height - y - 1

                elif self.rotation == 3:
                    old_x = y
                    old_y = self.width - x - 1

                if self.flipped:
                    old_x = self.width - old_x - 1

                # print(f'old_x: {old_x}, old_y: {old_y}')


                self.oriented_rows[y][x] = self.rows[old_y][old_x]
        
        self.set_edges()
    
    def set_edges(self):
        self.top = ''.join(self.oriented_rows[0])
        self.bottom = ''.join(self.oriented_rows[-1])
        self.left = ''.join([r[0] for r in self.oriented_rows])
        self.right = ''.join([r[-1] for r in self.oriented_rows])
    
    def __str__(self):
        s = f'Tile {self.id}:\n'

        for row in self.oriented_rows:
            s += ''.join(row) + '\n'
        
        return s


class Grid:
    def __init__(self):
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.rows = [[None]]

    def insert_tile(self, tile, x, y):
        if x < self.x_min:
            for row in self.rows:
                row[0:0] = [None] * (self.x_min - x)
            
            self.x_min = x
        
        if x > self.x_max:
            for row in self.rows:
                row.extend([None] * (x - self.x_max))
            
            self.x_max = x

        if y < self.y_min:
            for i in range(self.y_min - y):
                self.rows.insert(0, [None] * (self.x_max - self.x_min + 1))
            
            self.y_min = y
        
        if y > self.y_max:
            for i in range(y - self.y_max):
                self.rows.append([None] * (self.x_max - self.x_min + 1))
            
            self.y_max = y
        
        self.rows[y - self.y_min][x - self.x_min] = tile
    
    def attempt_to_insert_tile(self, tile):
        for y in range(self.y_min - 1, self.y_max + 2):
            for x in range(self.x_min - 1, self.x_max + 2):
                # print(f'Trying to insert tile {tile.id} into ({x},{y})')

                if self.does_tile_fit_at(tile, x, y):
                    # print(f'Inserting tile {tile.id} into ({x},{y})')
                    self.insert_tile(tile, x, y)
                    return True

        return False
    
    def get_tile_at(self, x, y):
        if x < self.x_min or x > self.x_max or y < self.y_min or y > self.y_max:
            return None
        
        return self.rows[y - self.y_min][x - self.x_min]

    def does_tile_fit_at(self, tile, x, y):
        tile_above = self.get_tile_at(x, y-1)
        tile_below = self.get_tile_at(x, y+1)
        tile_left = self.get_tile_at(x-1, y)
        tile_right = self.get_tile_at(x+1, y)

        if not tile_above and not tile_below and not tile_left and not tile_right:
            # No tiles to fit against
            return False
        
        if tile_above and tile_above.bottom != tile.top:
            return False
        
        if tile_below and tile_below.top != tile.bottom:
            return False
    
        if tile_left and tile_left.right != tile.left:
            return False
        
        if tile_right and tile_right.left != tile.right:
            return False
        
        return True
    
    def multiply_corners(self):
        top_left = self.get_tile_at(self.x_min, self.y_min)
        top_right = self.get_tile_at(self.x_max, self.y_min)
        bottom_left = self.get_tile_at(self.x_min, self.y_max)
        bottom_right = self.get_tile_at(self.x_max, self.y_max)

        return top_left.id * top_right.id * bottom_left.id * bottom_right.id
    
    def __str__(self):
        s = ''
        for row in self.rows:
            for tile in row:
                if tile:
                    s += str(tile.id) + ' '
                else:
                    s += 'NONE '
            s += '\n'
        return s



def main():
    grid = Grid()

    tiles = read_tiles('input.txt')

    first_tile = tiles.pop(0)
    grid.insert_tile(first_tile, 0, 0)

    while tiles:
        tile = tiles.pop(0)

        # print(f'Trying to insert tile {tile.id}')

        for orientation in range(8):
            tile.set_orientation(orientation)
            inserted = grid.attempt_to_insert_tile(tile)

            if inserted:
                break

        if not inserted:
            tiles.append(tile)
    
    result = grid.multiply_corners()

    print(f'Result: {result}')



def read_tiles(filename):
    with open(filename) as f:
        data = f.read()
    
    raw_tiles = data.split('\n\n')

    tiles = [parse_tile(t) for t in raw_tiles]
    return tiles

def parse_tile(raw_tile):
    raw_tiles_lines = raw_tile.splitlines()
    tile_id_line = raw_tiles_lines[0]
    tile_id = int(''.join([c for c in tile_id_line if c.isdigit()]))

    tile_rows = [list(r) for r in raw_tiles_lines[1:]]

    return Tile(tile_id, tile_rows)

if __name__ == '__main__':
    main()
