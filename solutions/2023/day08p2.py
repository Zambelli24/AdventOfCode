from aocd import get_data
import math
from functools import reduce

def get_desert_map():
  raw_data = get_data(day=8, year=2023).split('\n')
  steps = raw_data[0]
  desert_map = {}
  for mapping in raw_data[1:]:
    if mapping != '':
      mapping = mapping.split(' = ')
      left_right = mapping[1][1:-1].split(', ')
      desert_map[mapping[0]] = (left_right[0], left_right[1])

  print('---------- DESERT MAP ----------')
  print(desert_map)
  print('---------- STEPS ----------')
  print(steps)
  
  return desert_map, steps

def get_starting_nodes():
  desert_map, steps = get_desert_map()
  starting_nodes = []

  for mapping in desert_map.keys():
    if mapping[-1] == 'A':
      starting_nodes.append(mapping)
  
  print('---------- STARTING NODES ----------')
  print(starting_nodes)
  return starting_nodes

def get_steps_for_starting_node(starting_node, desert_map, steps):
  current = starting_node
  
  curr_step = 0
  step_count = 0
  while current[-1] != 'Z':
    step_count += 1
    direction = steps[curr_step]
    if direction == 'L':
      current = desert_map[current][0]
    else:
      current = desert_map[current][1]
    
    curr_step += 1
    if curr_step == len(steps):
      curr_step = 0

  print('---------- NUMBER OF STEPS FOR ' + starting_node + ' ----------')
  print(step_count)
  return step_count

def lcm(arr):
    l = reduce(lambda x,y:(x*y) // math.gcd(x,y), arr)
    return l

def find_least_steps():
  desert_map, steps = get_desert_map()
  starting_nodes = get_starting_nodes()

  step_count = 0
  node_steps = []

  for node in starting_nodes:
    min_steps = get_steps_for_starting_node(node, desert_map, steps)
    node_steps.append(min_steps)

  step_count = lcm(node_steps)

  print('---------- NUMBER OF STEPS ----------')
  print(step_count)
  return step_count

find_least_steps()