# s/o https://github.com/hyper-neutrino for a great explanation of part 2

from aocd import get_data
from collections import deque

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

def get_next_steps(current):
  neighbors = []
  for next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    next_row = current[0] + next[0]
    next_col = current[1] + next[1]
    neighbors.append((next_row, next_col))

  return neighbors

def get_reachable_locations(grid, start, steps):
  reached = {start}
  queue = deque([(start[0], start[1], steps)])
  end_locations = set()

  while queue:
    row, col, step = queue.popleft()

    if step % 2 == 0:
      end_locations.add((row, col))
    if step == 0:
      continue

    next_steps = get_next_steps((row, col))
    for next_row, next_col in next_steps:
      if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#' and (next_row, next_col) not in reached:
        queue.append((next_row, next_col, step - 1))
        reached.add((next_row, next_col))

  num_locations = len(end_locations)
  print('---------- POSSIBLE LOCATIONS AFTER ' + str(steps) + ' STEPS ----------')
  print(num_locations)
  return num_locations

def calculate_infinite_reachable_locations():
  grid, start = get_grid_and_start()
  steps = 26501365

  num_locations = 0
  grid_width = len(grid)
  inf_grid_width = steps // grid_width - 1

  num_odd_grids = (inf_grid_width // 2 * 2 + 1) ** 2
  num_even_grids = ((inf_grid_width + 1) // 2 * 2) ** 2
  odd_locations = get_reachable_locations(grid, start, inf_grid_width * 2 + 1)
  even_locations = get_reachable_locations(grid, start, inf_grid_width * 2)
  num_locations += num_odd_grids * odd_locations + num_even_grids * even_locations

  top_corner = get_reachable_locations(grid, (grid_width - 1, start[1]), grid_width - 1)
  right_corner = get_reachable_locations(grid, (start[0], 0), grid_width - 1)
  bottom_corner = get_reachable_locations(grid, (0, start[1]), grid_width - 1)
  left_corner = get_reachable_locations(grid, (start[0], grid_width - 1), grid_width - 1)
  num_locations += top_corner + right_corner + bottom_corner + left_corner

  top_right_edge_sm = get_reachable_locations(grid, (grid_width - 1, 0), grid_width // 2 - 1)
  top_left_edge_sm = get_reachable_locations(grid, (grid_width - 1, grid_width - 1), grid_width // 2 - 1)
  bottom_right_edge_sm = get_reachable_locations(grid, (0, 0), grid_width // 2 - 1)
  bottom_left_edge_sm = get_reachable_locations(grid, (0, grid_width - 1), grid_width // 2 - 1)
  num_locations += (inf_grid_width + 1) * (top_right_edge_sm + top_left_edge_sm + bottom_right_edge_sm + bottom_left_edge_sm)

  top_right_edge_lg = get_reachable_locations(grid, (grid_width - 1, 0), grid_width * 3 // 2 - 1)
  top_left_edge_lg = get_reachable_locations(grid, (grid_width - 1, grid_width - 1), grid_width * 3 // 2 - 1)
  bottom_right_edge_lg = get_reachable_locations(grid, (0, 0), grid_width * 3 // 2 - 1)
  bottom_left_edge_lg = get_reachable_locations(grid, (0, grid_width - 1), grid_width * 3 // 2 - 1)
  num_locations += inf_grid_width * (top_right_edge_lg + top_left_edge_lg + bottom_right_edge_lg + bottom_left_edge_lg)
  
  print('---------- TOTAL INFINITE REACHABLE LOCATIONS ----------')
  print(num_locations)
  return num_locations

calculate_infinite_reachable_locations()