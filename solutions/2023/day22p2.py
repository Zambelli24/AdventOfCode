# s/o https://github.com/hyper-neutrino for saving me time and headaches on this one
from aocd import get_data
from collections import deque

def overlaps(a, b):
  return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

def convert_to_key(brick):
  return ''.join(str(x) for x in brick)

def get_shifted_bricks():
  raw_data = get_data(year=2023, day=22).splitlines()
  bricks = []

  for row in raw_data:
    start, end = row.split('~')
    x1, y1, z1 = start.split(',')
    x2, y2, z2 = end.split(',')
    bricks.append(([int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)]))

  bricks.sort(key=lambda brick: brick[2])

  for i, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:i]:
      if overlaps(brick, check):
        max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

  bricks.sort(key=lambda brick: brick[2])

  print('---------- SHIFTED BRICKS ----------')
  print(bricks)
  return bricks

def get_total_fallen_bricks():
  total_fallen = 0
  bricks = get_shifted_bricks()

  supporting = {i: set() for i in range(len(bricks))}
  supported_by = {i: set() for i in range(len(bricks))}

  for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
      if overlaps(lower, upper) and upper[2] == lower[5] + 1:
        supporting[i].add(j)
        supported_by[j].add(i)

  for i in range(len(bricks)):
    support_by_one_bricks = deque(j for j in supporting[i] if len(supported_by[j]) == 1)
    falling = set(support_by_one_bricks)
    falling.add(i)
    
    while support_by_one_bricks:
      j = support_by_one_bricks.popleft()
      for k in supporting[j] - falling:
        if supported_by[k] <= falling:
          support_by_one_bricks.append(k)
          falling.add(k)
    
    total_fallen += len(falling) - 1

  print('---------- TOTAL FALLEN BRICKS ----------')
  print(total_fallen)
  return total_fallen

get_total_fallen_bricks()
