from aocd import get_data

KNOWN_TILES = set()

def get_grid():
  raw_data = get_data(day=16, year=2023).split('\n')
  grid = []
  for row in raw_data:
    grid.append([tile for tile in row])

  print('---------- GRID ----------')
  for row in grid:
    print(''.join(row))
  
  return grid

def move_up(x, y):
  return (x - 1, y, 'up')

def move_down(x, y):
  return (x + 1, y, 'down')

def move_left(x, y):
  return (x, y - 1, 'left')

def move_right(x, y):
  return (x, y + 1, 'right')

def check_tile(grid, energized_tiles, coords, direction):
  x = coords[0]
  y = coords[1]

  if x < 0 or x >= len(grid):
    return False, []
  if y < 0 or y >= len(grid[0]):
    return False, []
  if (x, y, direction) in KNOWN_TILES:
    return False, []
  
  KNOWN_TILES.add((x, y, direction))
  energized_tiles.add((x, y))
  
  tile = grid[x][y]
  if tile == '.':
    if direction == 'right':
      return True, [move_right(x, y)]
    elif direction == 'left':
      return True, [move_left(x, y)]
    elif direction == 'up':
      return True, [move_up(x, y)]
    elif direction == 'down':
      return True, [move_down(x, y)]
  elif tile == '/':
    if direction == 'right':
      return True, [move_up(x, y)]
    elif direction == 'left':
      return True, [move_down(x, y)]
    elif direction == 'up':
      return True, [move_right(x, y)]
    elif direction == 'down':
      return True, [move_left(x, y)]
  elif tile == '\\':
    if direction == 'right':
      return True, [move_down(x, y)]
    elif direction == 'left':
      return True, [move_up(x, y)]
    elif direction == 'up':
      return True, [move_left(x, y)]
    elif direction == 'down':
      return True, [move_right(x, y)]
  elif tile == '|':
    if direction == 'up':
      return True, [move_up(x, y)]
    elif direction == 'down':
      return True, [move_down(x, y)]
    elif direction == 'left' or direction == 'right':
      return True, [move_up(x, y), move_down(x, y)]
  elif tile == '-':
    if direction == 'left':
      return True, [move_left(x, y)]
    elif direction == 'right':
      return True, [move_right(x, y)]
    elif direction == 'up' or direction == 'down':
      return True, [move_left(x, y), move_right(x, y)]

def get_energized_tiles():
  grid = get_grid()
  energized_tiles = set()

  curr_tile = (0, 0)
  direction = 'right'
  additional_beams = []
  has_next = True

  while has_next:
    has_next, moves = check_tile(grid, energized_tiles, curr_tile, direction)
    if len(moves) > 0:
      curr_tile = (moves[0][0], moves[0][1])
      direction = moves[0][2]
      if len(moves) > 1:
        additional_beams.append(moves[1:])

    if not has_next and len(additional_beams) > 0:
      has_next = True
      move = additional_beams.pop(0)
      curr_tile = (move[0][0], move[0][1])
      direction = move[0][2]

  print('---------- ENERGIZED TILES ----------')
  print(len(energized_tiles))
  return len(energized_tiles)

get_energized_tiles()