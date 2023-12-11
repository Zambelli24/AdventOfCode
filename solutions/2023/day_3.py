from aocd import get_data

def get_all_lines():
  return get_data(day=3, year=2023).split('\n')

def is_dot(digit):
  return digit == '.'

def is_star(digit):
  return digit == '*'

def is_digit(digit):
  return digit.isnumeric()

def check_valid_part(engine, i, j):
  above_left = False
  above = False
  above_right = False
  below_left = False
  below = False
  below_right = False
  left = False
  right = False
  
  if i > 0:
    above = not is_dot(engine[i - 1][j])

    if j > 0:
      above_left = not is_dot(engine[i - 1][j - 1])
      left = not is_dot(engine[i][j - 1]) and not is_digit(engine[i][j - 1])
    
    if j < len(engine[i]) - 1:
      above_right = not is_dot(engine[i - 1][j + 1])
      right = not is_dot(engine[i][j + 1]) and not is_digit(engine[i][j + 1])

  if i < len(engine) - 1:
    below = not is_dot(engine[i + 1][j])
    
    if j > 0:
      below_left = not is_dot(engine[i + 1][j - 1])
      left = not is_dot(engine[i][j - 1]) and not is_digit(engine[i][j - 1])
    
    if j < len(engine[i]) - 1:
      below_right = not is_dot(engine[i + 1][j + 1])
      right = not is_dot(engine[i][j + 1]) and not is_digit(engine[i][j + 1])

  return above_left or above or above_right or below_left or below or below_right or left or right

def build_number(engine, i, j):
  number = engine[i][j]
  if j > 0:
    if is_digit(engine[i][j - 1]):
      number = engine[i][j - 1] + number
    
      if j - 1 > 0 and is_digit(engine[i][j - 2]):
        number = engine[i][j - 2] + number
    

  if j < len(engine[i]) - 1:
    if is_digit(engine[i][j + 1]):
      number = number + engine[i][j + 1]
    
      if j + 1 < len(engine[i]) and is_digit(engine[i][j + 2]):
        number = number + engine[i][j + 2]
  
  return number

def get_gear_parts(engine, i, j):
  parts = []
  
  if i > 0:
    if is_digit(engine[i - 1][j]):
      parts.append(build_number(engine, i - 1, j))

    if j > 0:
      if is_digit(engine[i - 1][j - 1]):
        parts.append(build_number(engine, i - 1, j - 1))
      if is_digit(engine[i][j - 1]):
        parts.append(build_number(engine, i, j - 1))
    
    if j < len(engine[i]) - 1:
      if is_digit(engine[i - 1][j + 1]):
        parts.append(build_number(engine, i - 1, j + 1))
      if is_digit(engine[i][j + 1]):
        parts.append(build_number(engine, i, j + 1))

  if i < len(engine) - 1:
    if is_digit(engine[i + 1][j]):
      parts.append(build_number(engine, i + 1, j))
    
    if j > 0:
      if is_digit(engine[i + 1][j - 1]):
        parts.append(build_number(engine, i + 1, j - 1))
      if is_digit(engine[i][j - 1]):
        parts.append(build_number(engine, i, j - 1))
    
    if j < len(engine[i]) - 1:
      if is_digit(engine[i + 1][j + 1]):
        parts.append(build_number(engine, i + 1, j + 1))
      if is_digit(engine[i][j + 1]):
        parts.append(build_number(engine, i, j + 1))

  return list(set(parts))


def sum_valid_parts():
  all_lines = get_all_lines()
  all_chars = []
  for line in all_lines:
    all_chars.append([char for char in line])
  

  sum = 0
  keep_number = False
  number = ''
  for i, char in enumerate(all_chars):
    for j, subchar in enumerate(all_chars[i]):
      if all_chars[i][j].isnumeric():
          number += all_chars[i][j]
          if check_valid_part(all_chars, i, j):
            keep_number = True
      else:
        if keep_number and number != '':
          print('---------- VALID PART ----------')
          print(number)
          sum += int(number)

        keep_number = False
        number = ''

    if keep_number and number != '':
        print('---------- VALID PART ----------')
        print(number)
        sum+=int(number)

    keep_number = False
    number = ''
  
  print('---------- SUM OF ALL VALID PARTS FOR PART ----------')
  print(sum)
  return sum

def sum_gear_parts():
  all_lines = get_all_lines()
  all_chars = []
  for line in all_lines:
    all_chars.append([char for char in line])
  
  sum = 0
  for i, char in enumerate(all_chars):
    for j, subchar in enumerate(all_chars[i]):
      if is_star(all_chars[i][j]):
          parts = get_gear_parts(all_chars, i, j)
          if len(parts) == 2:
            print('---------- GEAR PARTS ----------')
            print(parts)
            sum += int(parts[0]) * int(parts[1])
  
  print('---------- SUM OF ALL GEAR PARTS FOR PART ----------')
  print(sum)
  return sum

sum_valid_parts()
sum_gear_parts()