from aocd import get_data

def get_init_sequence():
  raw_data = get_data(day=15, year=2023)
  init_sequence = raw_data.split(',')

  print('---------- INIT SEQUENCE ----------')
  print(init_sequence)
  return init_sequence

def get_value(string):
  value = 0
  for char in string:
    value += ord(char)
    value *= 17
    value %= 256
  
  print('---------- VALUE FOR ' + string + ' ----------')
  print(value)
  return value

def get_sum():
  init_sequence = get_init_sequence()

  sum = 0
  for string in init_sequence:
    sum += get_value(string)

  print('---------- SUM ----------')
  print(sum)
  return sum

get_sum()