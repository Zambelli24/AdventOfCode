# s/o https://github.com/hyper-neutrino for the help

from aocd import get_data

def get_universe():
  raw_data = get_data(day=11, year=2023)
  universe = []

  for row in raw_data.split('\n'):
    curr_row = []

    for char in row:
      curr_row.append(char)
  
    universe.append(curr_row)

  empty_cols = []
  for i in range(len(universe[0])):
    col = [row[i] for row in universe]
    if len(set(col)) == 1:
      empty_cols.append(i)

  empty_rows = []
  for i in range(len(universe)):
    if len(set(universe[i])) == 1:
      empty_rows.append(i)

  print('---------- UNIVERSE ----------')
  print(universe)
  return universe, empty_cols, empty_rows

def get_all_galaxies(universe):
  all_galaxies = []
  for i in range(len(universe)):
    for j in range(len(universe[i])):
      if universe[i][j] == '#':
        all_galaxies.append((i, j))
        
  print('---------- COUNT OF ALL GALAXIES ----------')
  print(len(all_galaxies))
  return all_galaxies

def get_sum_shortest_paths():
  universe, empty_cols, empty_rows = get_universe()
  all_galaxies = get_all_galaxies(universe)

  sum_shortest_paths = 0
  scale = 2
  for i, (row1, col1) in enumerate(all_galaxies):
    for (row2, col2) in all_galaxies[:i]:
      for row in range(min(row1, row2), max(row1, row2)):
        sum_shortest_paths += scale if row in empty_rows else 1
      for col in range(min(col1, col2), max(col1, col2)):
        sum_shortest_paths += scale if col in empty_cols else 1
  
  print('---------- SUM SHORTEST PATHS ----------')
  print(sum_shortest_paths)
  return sum_shortest_paths

get_sum_shortest_paths()