from aocd import get_data
from queue import Queue

def get_grid_and_start():
  rows = get_data(year=2023, day=21).splitlines()
  start = (0, 0)
  grid = []
  for i, row in enumerate(rows):
    grid.append(list(row))
    if 'S' in row:
      start = (row.index('S'), i)

  print('---------- GRID ----------')
  print(grid)
  print('---------- START ----------')
  print(start)
  return grid, start

def get_neighbors(grid, current, step):
  neighbors = []
  for next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    next_row = current[0] + next[0]
    next_col = current[1] + next[1]
    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#':
      neighbors.append((next_row, next_col, step))

  return neighbors

def get_all_end_locations(steps):
  grid, start = get_grid_and_start()
  frontier = Queue()
  frontier.put([start])

  step = 0
  while step < steps:
    step += 1
    curr_steps = frontier.get()

    next = set()
    for curr_step in curr_steps:
      next_steps = get_neighbors(grid, curr_step, step)
      for n in next_steps:
        next.add(n)

    frontier.put(next)

  num_locations = len(frontier.get())
  print('---------- POSSIBLE LOCATIONS AFTER ' + str(steps) + ' STEPS ----------')
  print(num_locations)
  return num_locations

get_all_end_locations(64)