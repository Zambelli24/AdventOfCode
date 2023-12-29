from aocd import get_data

def get_dig_plan():
  raw_data = get_data(day=18).split('\n')
  dig_plan = []
  for line in raw_data:
    direction, distance, color = line.split(' ')
    dig_plan.append((direction, int(distance), color))

  print('---------- DIG PLAN ----------')
  print(dig_plan)
  return dig_plan

def get_trench_edge():
  dig_plan = get_dig_plan()
  
  edges = set()
  curr_edge = (0, 0, '7')
  edges.add(curr_edge)

  min_row = 0
  min_col = 0
  max_row = 0
  max_col = 0

  for i, instruction in enumerate(dig_plan):
    direction = instruction[0]
    distance = instruction[1]
    
    for d in range(distance):
      modified_direction = direction

      if d == distance - 1:
        if i < len(dig_plan) - 1:
          next_direction = dig_plan[i + 1][0]
        else:
          next_direction = dig_plan[0][0]

        combo = direction + next_direction
        if combo == 'LU' or combo == 'DR':
          modified_direction = 'l'
        elif combo == 'LD' or combo == 'UR':
          modified_direction = 'F'
        elif combo == 'RU' or combo == 'DL':
          modified_direction = 'J'
        elif combo == 'RD' or combo == 'UL':
          modified_direction = '7'

      if direction == 'R':
        curr_edge = (curr_edge[0], curr_edge[1] + 1, modified_direction)
      elif direction == 'L':
        curr_edge = (curr_edge[0], curr_edge[1] - 1, modified_direction)
      elif direction == 'U':
        curr_edge = (curr_edge[0] - 1, curr_edge[1], modified_direction)
      elif direction == 'D':
        curr_edge = (curr_edge[0] + 1, curr_edge[1], modified_direction)
      
      edges.add(curr_edge)
      if curr_edge[0] < min_row:
        min_row = curr_edge[0]
      if curr_edge[1] < min_col:
        min_col = curr_edge[1]
      if curr_edge[0] > max_row:
        max_row = curr_edge[0]
      if curr_edge[1] > max_col:
        max_col = curr_edge[1]

  print('---------- TRENCH EDGES ----------')
  print(edges)
  return edges, (min_row, max_row), (min_col, max_col)
      
def count_inversions(row_points, col):
  count = 0

  left_points = [edge for edge in row_points if edge[1] < col]
  for point in left_points:
    if point[2] in 'UDF7':
      count += 1

  return count

def calculate_area():
  cubic_meters = 0
  trench_edges, rows, cols = get_trench_edge()
  for row in range(rows[0], rows[1]+1):
    points = sorted([p for p in trench_edges if p[0] == row])
    cubic_meters += len(points)

    for col in range(cols[0], cols[1]+1):
      col_values = [p[1] for p in points]
      if col not in col_values and min(col_values) < col < max(col_values):
        inversions = count_inversions(points, col)
        cubic_meters += inversions % 2

  print('---------- CUBIC METERS ----------')
  print(cubic_meters)
  return cubic_meters

calculate_area()