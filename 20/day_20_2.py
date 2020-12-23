#!/usr/bin/env python3

SEA_MONSTER = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

SEA_MONSTER_WIDTH = len(SEA_MONSTER[0])
SEA_MONSTER_HEIGHT = len(SEA_MONSTER)

def orient_image(rows, orientation):
    size = len(rows)
    oriented_rows = [[' '] * size for i in range(size)]
    flipped = orientation // 4 == 1
    rotation = orientation % 4

    for y in range(size):
        for x in range(size):

            if rotation == 0:
                old_x = x
                old_y = y
            
            elif rotation == 1:
                old_x = size - y - 1
                old_y = x

            elif rotation == 2:
                old_x = size - x - 1
                old_y = size - y - 1

            elif rotation == 3:
                old_x = y
                old_y = size - x - 1

            if flipped:
                old_x = size - old_x - 1

            oriented_rows[y][x] = rows[old_y][old_x]
    
    return oriented_rows



class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.rows = rows
        self.width = len(self.rows[0])
        self.height = len(self.rows)
        self.set_orientation(0)
    
    def set_orientation(self, orientation):
        self.oriented_rows = orient_image(self.rows, orientation)
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

                if self.does_tile_fit_at(tile, x, y):
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
    
    def get_image(self):
        tile_width = self.rows[0][0].width - 2
        tile_height = self.rows[0][0].height - 2

        tiles_wide = self.x_max - self.x_min + 1
        tiles_high = self.y_max - self.y_min + 1

        image_width = tile_width * tiles_wide
        image_height = tile_height * tiles_high

        image = [[' '] * image_width for i in range(image_height)]
        
        for y in range(image_height):
            for x in range(image_width):
                tile = self.rows[y // tile_height][x // tile_width]

                image[y][x] = tile.oriented_rows[(y % tile_height) + 1][(x % tile_width) + 1]
        
        return image

        
    
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

        for orientation in range(8):
            tile.set_orientation(orientation)
            inserted = grid.attempt_to_insert_tile(tile)

            if inserted:
                break

        if not inserted:
            tiles.append(tile)
    
    image = grid.get_image()

    for orientation in range(8):
        transformed_image = orient_image(image, orientation)
        sea_monsters = count_sea_monsters(transformed_image)

        if sea_monsters:
            break

    sea_monster_hashes = count_hashes(SEA_MONSTER)
    image_hashes = count_hashes(image)

    non_sea_monster_hashes = image_hashes - (sea_monster_hashes * sea_monsters)
    print(f'Non sea monster #s: {non_sea_monster_hashes}')




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


def count_sea_monsters(image):
    count = 0

    for y in range(0, len(image) - SEA_MONSTER_HEIGHT + 1):
        for x in range(0, len(image[0]) - SEA_MONSTER_WIDTH + 1):
            if is_sea_monster_at(image, x, y):
                count += 1
    
    return count


def is_sea_monster_at(image, x, y):
    for sy in range(SEA_MONSTER_HEIGHT):
        for sx in range(SEA_MONSTER_WIDTH):
            if SEA_MONSTER[sy][sx] == '#' and image[y+sy][x+sx] != '#':
                return False
    return True

def count_hashes(rows):
    return sum([sum(c == '#' for c in r) for r in rows])


if __name__ == '__main__':
    main()
