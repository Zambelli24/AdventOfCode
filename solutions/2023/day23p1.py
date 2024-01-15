from aocd import get_data
import sys

sys.setrecursionlimit(2500)

def get_trail_map():
  raw_data = get_data(year=2023, day=23).splitlines()
  trail_map = []
  start = None
  end = None

  for i, row in enumerate(raw_data):
    curr_row = []
    for j, char in enumerate(row):
      curr_row.append(char)
      if i == 0 and char == '.':
        start = (i, j)
      if i == len(raw_data) - 1 and char == '.':
        end = (i, j)
    trail_map.append(curr_row)

  print('---------- TRAIL MAP ----------')
  print(trail_map)
  print('---------- START ----------')
  print(start)
  print('---------- END ----------')
  print(end)

  return trail_map, start, end

def get_next_steps(trail_map, current, path):
  next_steps = []

  if trail_map[current[0]][current[1]] == '^':
    next_steps.append((current[0] - 1, current[1]))
  elif trail_map[current[0]][current[1]] == 'v':
    next_steps.append((current[0] + 1, current[1]))
  elif trail_map[current[0]][current[1]] == '<':
    next_steps.append((current[0], current[1] - 1))
  elif trail_map[current[0]][current[1]] == '>':
    next_steps.append((current[0], current[1] + 1))
  else:
    for next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      next_row = current[0] + next[0]
      next_col = current[1] + next[1]
      
      next_loc = trail_map[next_row][next_col]
      if next_loc != '#' and (next_row, next_col) not in path:
        can_move_left = next_col < current[1] and next_loc != '>'
        can_move_right = next_col > current[1] and next_loc != '<'
        can_move_up = next_row < current[0] and next_loc != 'v'
        can_move_down = next_row > current[0] and next_loc != '^'
        if can_move_left or can_move_right or can_move_up or can_move_down:
          next_steps.append((next_row, next_col))

  return next_steps

def get_all_paths(trail_map, start, end, path=[]):
    if start == end:
      return [path]
    
    path = path + [start]
    paths = []
    for next in get_next_steps(trail_map, start, path):
      if next not in path:
        new_paths = get_all_paths(trail_map, next, end, path)
        for new_path in new_paths:
          paths.append(new_path)

    return paths   

def get_longest_path():
  trail_map, start, end = get_trail_map()
  all_paths = get_all_paths(trail_map, start, end)
  
  longest = 0
  for path in all_paths:
    print(len(path))
    if len(path) > longest:
      longest = len(path)
  
  print('---------- LONGEST PATH ----------')
  print(longest)
  return longest

get_longest_path()