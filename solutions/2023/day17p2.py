from aocd import get_data
from heapq import heappush, heappop

def get_blocks():
  raw_data = get_data(day=17).split('\n')
  blocks = []
  for line in raw_data:
    blocks.append([int(block) for block in line])

  print('---------- BLOCKS ----------')
  print(blocks)
  return blocks

def get_turn_heat_loss(blocks, row, next_row, col, next_col):
  turn_heat_loss = 0
  if next_row == row:
    diff = next_col - col
    while diff != 0:
      turn_heat_loss += blocks[row][col + diff]
      if diff > 0:
        diff -= 1
      else:
        diff += 1

  if next_col == col:
    diff = next_row - row
    while diff != 0:
      turn_heat_loss += blocks[row + diff][col]
      if diff > 0:
        diff -= 1
      else:
        diff += 1

  print('---------- TURN HEAT LOSS ----------')
  print(turn_heat_loss)
  return turn_heat_loss


def get_minimum_heat_loss():  
  blocks = get_blocks()
  visited = set()
  priority_queue = [(0, 0, 0, 0, 0, 0)]

  min_heat_loss = 10000000000
  while priority_queue:
    heat_loss, row, col, dir_row, dir_col, num_steps = heappop(priority_queue)

    if row == len(blocks) - 1 and col == len(blocks[0]) - 1:
      min_heat_loss = heat_loss
      break

    if (row, col, dir_row, dir_col, num_steps) in visited:
      continue

    visited.add((row, col, dir_row, dir_col, num_steps))

    if num_steps < 10 and (dir_row, dir_col) != (0, 0):
      next_row = row + dir_row
      next_col = col + dir_col
      if 0 <= next_row < len(blocks) and 0 <= next_col < len(blocks[0]):
        heappush(priority_queue, (heat_loss + blocks[next_row][next_col], next_row, next_col, dir_row, dir_col, num_steps + 1))

    for next_dir_row, next_dir_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      if (next_dir_row, next_dir_col) != (-dir_row, -dir_col) and (next_dir_row, next_dir_col) != (dir_row, dir_col):
        next_row = row + (next_dir_row * 4)
        next_col = col + (next_dir_col * 4)
        if 0 <= next_row < len(blocks) and 0 <= next_col < len(blocks[0]):
          turn_heat_loss = get_turn_heat_loss(blocks, row, next_row, col, next_col)
          heappush(priority_queue, (heat_loss + turn_heat_loss, next_row, next_col, next_dir_row, next_dir_col, 4))

  print('---------- MINIMUM HEAT LOSS ----------')
  print(min_heat_loss)
  return min_heat_loss

get_minimum_heat_loss()