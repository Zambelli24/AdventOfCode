# s/o https://github.com/hyper-neutrino for the help - solution for part 1 not efficent enough for part 2

from aocd import get_data

direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def get_dig_plan():
  raw_data = get_data(day=18).split('\n')
  dig_plan = []
  for line in raw_data:
    _, _, hex = line.split(' ')
    hex = hex[2:-1]
    direction = 'RDLU'[int(hex[-1])]
    dig_plan.append((direction, int(hex[:-1], 16)))

  print('---------- DIG PLAN ----------')
  print(dig_plan)
  return dig_plan

def calculate_area():
  dig_plan = get_dig_plan()
  
  edges = [(0, 0)]
  edge_area = 0

  for instruction in dig_plan:
    direction = instruction[0]
    distance = instruction[1]

    dc, dr = direction_map[direction]

    edge_area += distance
    row, col = edges[-1]
    edges.append((row + dr * distance, col + dc * distance))

  total_area = abs(sum(edges[i][0] * (edges[i - 1][1] - edges[(i + 1) % len(edges)][1]) for i in range(len(edges)))) // 2
  inner_area = total_area - edge_area // 2 + 1

  print('---------- CUBIC METERS ----------')
  print(edge_area + inner_area)
  return edge_area + inner_area

calculate_area()