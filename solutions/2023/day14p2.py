# s/o https://github.com/hyper-neutrino for the help

from aocd import get_data

def get_rock_formation():
  return tuple(get_data(day=14, year=2023).splitlines())

def run_cycle(starting_rock_formation):
  grid = starting_rock_formation
  
  for _ in range(4):
      grid = tuple(map("".join, zip(*grid)))
      grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
      grid = tuple(row[::-1] for row in grid)
  
  return grid

def get_total_load():
  rock_formation = get_rock_formation()
  seen = {rock_formation}
  array = [rock_formation]

  cycle = 0
  while True:
      cycle += 1
      rock_formation = run_cycle(rock_formation)
      if rock_formation in seen:
          break
      seen.add(rock_formation)
      array.append(rock_formation)
      
  first = array.index(rock_formation)
      
  rock_formation = array[(1000000000 - first) % (cycle - first) + first]

  total_load = sum(row.count("O") * (len(rock_formation) - r) for r, row in enumerate(rock_formation))
  
  print('---------- TOTAL LOAD ----------')
  print(total_load)
  return total_load

get_total_load()