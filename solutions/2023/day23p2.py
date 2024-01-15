# s/o https://github.com/hyper-neutrino for saving me from brute force hell
from aocd import get_data

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

def get_decision_points(trail_map, start, end):
  points = [start, end]
  for r, row in enumerate(trail_map):
    for c, ch in enumerate(row):
      if ch == "#":
        continue
      neighbors = 0
      for next_row, next_col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= next_row < len(trail_map) and 0 <= next_col < len(trail_map[0]) and trail_map[next_row][next_col] != "#":
          neighbors += 1
      if neighbors >= 3:
        points.append((r, c))

  return points

def build_graph():
  trail_map, start, end = get_trail_map()
  points = get_decision_points(trail_map, start, end)
  graph = {pt: {} for pt in points}

  for start_row, start_col in points:
    stack = [(0, start_row, start_col)]
    seen = {(start_row, start_col)}

    while stack:
      n, r, c = stack.pop()
      
      if n != 0 and (r, c) in points:
        graph[(start_row, start_col)][(r, c)] = n
        continue

      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_row = r + dr
        next_col = c + dc
        if 0 <= next_row < len(trail_map) and 0 <= next_col < len(trail_map[0]) and trail_map[next_row][next_col] != "#" and (next_row, next_col) not in seen:
          stack.append((n + 1, next_row, next_col))
          seen.add((next_row, next_col))

  print('---------- GRAPH ----------')
  print(graph)
  return graph, start, end

def get_longest_path():
  graph, start, end = build_graph()
  seen = set()

  def dfs(pt):
    if pt == end:
      return 0

    longest = -float("inf")

    seen.add(pt)
    for next in graph[pt]:
      if next not in seen:
        longest = max(longest, dfs(next) + graph[pt][next])
    seen.remove(pt)

    return longest
  
  longest_path = dfs(start)
  print('---------- LONGEST PATH ----------')
  print(longest_path)
  return longest_path

get_longest_path()