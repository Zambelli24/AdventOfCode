from aocd import get_data

def get_rock_formation():
  raw_data = get_data(day=14, year=2023)
  rock_formation = []
  
  for row in raw_data.split('\n'):
    rock_formation.append([char for char in row])

  return rock_formation

def get_shifted_rocks():
  rock_formation = get_rock_formation()

  shifted_rocks = rock_formation
  for i, row in enumerate(rock_formation):
    for j, rock in enumerate(row):
      if rock == 'O':
        above = i - 1
        while above >= 0 and shifted_rocks[above][j] == '.':
          shifted_rocks[above][j] = 'O'
          shifted_rocks[above+1][j] = '.'
          above -= 1
        
  print('---------- SHIFTED ROCKS ----------')
  for row in shifted_rocks:
    print(''.join(row))
  return shifted_rocks

def get_total_load():
  shifted_rocks = get_shifted_rocks()
  total_load = 0

  for i, row in enumerate(shifted_rocks):
    row_load = len(shifted_rocks) - i
    for rock in row:
      if rock == 'O':
        total_load += row_load
  
  print('---------- TOTAL LOAD ----------')
  print(total_load)
  return total_load

get_total_load()