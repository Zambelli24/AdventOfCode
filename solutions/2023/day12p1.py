# s/o https://github.com/hyper-neutrino for the help

from aocd import get_data

def get_spring_groups():
  raw_data = get_data(day=12, year=2023)
  
  springs = []
  for row in raw_data.split('\n'):
    spr, damage_record = row.split(' ')
    springs.append({
      'damage_record': tuple(map(int, damage_record.split(','))),
      'springs': spr,
    })

  print('---------- SPRINGS ----------')
  print(springs)
  return springs

def get_arrangements_for_spring(springs, damage_record):
  if springs == '':
    return 1 if damage_record == () else 0
  
  if damage_record == ():
    return 0 if '#' in springs else 1
  
  count = 0

  if springs[0] in '.?':
    count += get_arrangements_for_spring(springs[1:], damage_record)

  if springs[0] in '#?':
    if damage_record[0] <= len(springs) and '.' not in springs[:damage_record[0]] and (damage_record[0] == len(springs) or springs[damage_record[0]] != '#'):
      count += get_arrangements_for_spring(springs[damage_record[0] + 1:], damage_record[1:])
    else:
      count += 0
  
  return count

def get_all_possible_arrangements():
  spring_groups = get_spring_groups()
  all_possible_arrangements = 0

  for group in spring_groups:
    all_possible_arrangements += get_arrangements_for_spring(group['springs'], group['damage_record'])

  print('---------- ALL POSSIBLE ARRANGEMENTS ----------')
  print(all_possible_arrangements)
  return all_possible_arrangements

get_all_possible_arrangements()