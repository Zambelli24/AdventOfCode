from aocd import get_data

BOXES = {}

def get_init_sequence():
  raw_data = get_data(day=15, year=2023)
  init_sequence = raw_data.split(',')

  print('---------- INIT SEQUENCE ----------')
  print(init_sequence)
  return init_sequence

def get_hash_value(string):
  value = 0
  for char in string:
    value += ord(char)
    value *= 17
    value %= 256
  
  print('---------- VALUE FOR ' + string + ' ----------')
  print(value)
  return value

def organize_lenses():
  init_sequence = get_init_sequence()

  for lense in init_sequence:
    is_add = '=' in lense
    if is_add:
      label, length = lense.split('=')
    else:
      label, length = lense.split('-')
    
    hash_value = get_hash_value(label)
    if hash_value not in BOXES.keys():
      if is_add:
        BOXES[hash_value] = [(label, length)]
    else:
      if is_add:
        curr_lenses = BOXES[hash_value]
        curr_lense = list(i for i, curr in enumerate(curr_lenses) if curr[0] == label)
        if len(curr_lense) > 0:
          BOXES[hash_value][curr_lense[0]] = (label, length)
        else:
          BOXES[hash_value].append((label, length))
      else:
        curr_lenses = BOXES[hash_value]
        curr_lense = list(curr for curr in curr_lenses if curr[0] == label)
        if len(curr_lense) > 0:
          BOXES[hash_value].remove(curr_lense[0])

  print('---------- ORGANIZED BOXES WITH LENSES ----------')
  print(BOXES)

def get_focus_power():
  organize_lenses()
  focus_power = 0
  for box_num in BOXES.keys():
    for i, lense in enumerate(BOXES[box_num]):
      focus_power += (box_num+1) * (i+1) * int(lense[1])

  print('---------- FOCUS POWER ----------')
  print(focus_power)
  return focus_power

get_focus_power()