# s/o https://github.com/womogenes for the help with part 2

from aocd import get_data

ABOVE = ['|', 'F', '7', 'S']
BELOW = ['|', 'J', 'L', 'S']
LEFT = ['-', 'F', 'L', 'S']
RIGHT = ['-', 'J', '7', 'S']

def get_starting_location(pipes):
  for i in range(len(pipes)):
    for j in range(len(pipes[i])):
      if pipes[i][j] == 'S':
        return (i, j)
      
def get_above(pipes, curr_loc):
  row, col = curr_loc
  if row > 0:
    if pipes[row - 1][col] in ABOVE:
      return (row - 1, col)
  else:
    return None
  
def get_below(pipes, curr_loc):
  row, col = curr_loc
  if row < len(pipes) - 1:
    if pipes[row + 1][col] in BELOW:
      return (row + 1, col)
  else:
    return False
  
def get_left(pipes, curr_loc):
  row, col = curr_loc
  if col > 0:
    if pipes[row][col - 1] in LEFT:
      return (row, col - 1)
  else:
    return None
  
def get_right(pipes, curr_loc):
  row, col = curr_loc
  if col < len(pipes[row]) - 1:
    if pipes[row][col + 1] in RIGHT:
      return (row, col + 1)
  else:
    return None
      
def get_next_step(pipes, prev_loc, curr_loc):
  prev_row, prev_col = prev_loc
  curr_row, curr_col = curr_loc
  if pipes[curr_row][curr_col] == 'S':
    loc = get_above(pipes, curr_loc)
    if loc != None:
      return pipes[loc[0]][loc[1]], loc
    
    loc = get_below(pipes, curr_loc)
    if loc != None:
      return pipes[loc[0]][loc[1]], loc
    
    loc = get_left(pipes, curr_loc)
    if loc != None:
      return pipes[loc[0]][loc[1]], loc
    
    loc = get_right(pipes, curr_loc)
    if loc != None:
      return pipes[loc[0]][loc[1]], loc
  
  elif pipes[curr_row][curr_col] == '|':
    if prev_row < curr_row:
      loc = get_below(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_above(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  elif pipes[curr_row][curr_col] == '-':
    if prev_col < curr_col:
      loc = get_right(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_left(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  elif pipes[curr_row][curr_col] == 'F':
    if prev_row > curr_row:
      loc = get_right(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_below(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  elif pipes[curr_row][curr_col] == 'J':
    if prev_row < curr_row:
      loc = get_left(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_above(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  elif pipes[curr_row][curr_col] == '7':
    if prev_col < curr_col:
      loc = get_below(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_left(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  elif pipes[curr_row][curr_col] == 'L':
    if prev_col > curr_col:
      loc = get_above(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    else:
      loc = get_right(pipes, curr_loc)
      return pipes[loc[0]][loc[1]], loc
    
  return None, None

def get_main_loop_and_map():
  raw_data = get_data(day=10, year=2023).split('\n')
  pipes = []
  for row in raw_data:
    pipes.append([char for char in row])

  main_loop = []
  prev = get_starting_location(pipes)
  curr = prev
  next = None
  
  while next != 'S':
    next, loc = get_next_step(pipes, prev, curr)
    prev = curr
    curr = loc
    main_loop.append({ 'pipe': next, 'location': loc })
  
  print('---------- MAIN LOOP ----------')
  print(main_loop)
  return main_loop, pipes

def count_inversions(all_pipes, main_loop, loc):
  i = loc[0]
  j = loc[1]
  line = all_pipes[i]
  count = 0

  for k in range(j):
    if (i, k) in main_loop:
      if line[k] in BELOW:
        count += 1

  return count
  
  
def get_enclosed_tiles():
  main_loop, all_pipes = get_main_loop_and_map()
  main_loop_coords = set()
  for pipe in main_loop:
    main_loop_coords.add(pipe['location'])

  enclosed_tiles = 0
  for i in range(len(all_pipes)):
    for j in range(len(all_pipes[i])):
      loc = (i, j)
      if loc not in main_loop_coords:
        inversions = count_inversions(all_pipes, main_loop_coords, loc)
        enclosed_tiles += inversions % 2
  
  print('---------- NUMBER OF ENCLOSED TILES ----------')
  print(enclosed_tiles)
  

get_enclosed_tiles()