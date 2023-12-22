from aocd import get_data

cache = {}

def get_spring_groups():
  raw_data = get_data(day=12, year=2023)
  
  springs = []
  for row in raw_data.split('\n'):
    spr, damage_record = row.split(' ')

    unfolded_spring = spr
    unfolded_damage = damage_record
    for i in range(4):
      unfolded_spring += '?' + spr
      unfolded_damage += ',' + damage_record

    springs.append({
      'damage_record': tuple(map(int, unfolded_damage.split(','))),
      'springs': unfolded_spring,
    })

  print('---------- SPRINGS ----------')
  print(springs)
  return springs

def get_arrangements_for_spring(springs, damage_record):
  if springs == '':
    return 1 if damage_record == () else 0
  
  if damage_record == ():
    return 0 if '#' in springs else 1

  key = (springs, damage_record)
  if key in cache:
    return cache[key]
  
  count = 0

  if springs[0] in '.?':
    count += get_arrangements_for_spring(springs[1:], damage_record)

  if springs[0] in '#?':
    if damage_record[0] <= len(springs) and '.' not in springs[:damage_record[0]] and (damage_record[0] == len(springs) or springs[damage_record[0]] != '#'):
      count += get_arrangements_for_spring(springs[damage_record[0] + 1:], damage_record[1:])
    else:
      count += 0
  
  cache[key] = count
  print('---------- COUNT FOR SPRING ----------')
  print(count)
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