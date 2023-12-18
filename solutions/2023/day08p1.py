from aocd import get_data

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

def get_number_of_steps():
  desert_map, steps = get_desert_map()

  current = 'AAA'
  end = 'ZZZ'
  curr_step = 0
  step_count = 0
  while current != end:
    step_count += 1
    direction = steps[curr_step]
    if direction == 'L':
      current = desert_map[current][0]
    else:
      current = desert_map[current][1]
    
    curr_step += 1
    if curr_step == len(steps):
      curr_step = 0

  print('---------- NUMBER OF STEPS ----------')
  print(step_count)
  return step_count


get_number_of_steps()