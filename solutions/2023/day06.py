from aocd import get_data
import regex

def get_race_records():
  race_records = []
  raw_data = get_data(day=6, year=2023).split('\n')

  times = regex.findall(r'\d+', raw_data[0].split(':')[1])
  records = regex.findall(r'\d+', raw_data[1].split(':')[1])
  
  for i, time in enumerate(times):
    race_records.append((int(time), int(records[i])))
  
  print('---------- RACE RECORDS ----------')
  print(race_records)
  return race_records

def get_number_of_ways_to_win(time, record):
  ways_to_win = 0
  hold = 0
  while hold < time:
    dist = hold * (time - hold)
    if dist > record:
      ways_to_win += 1
    hold += 1

  print('---------- WAYS TO WIN ----------')
  print(ways_to_win)
  return ways_to_win

def get_ways_to_win_part_one():
  records = get_race_records()

  permutations = 1
  for record in records:
    num_ways_to_win = get_number_of_ways_to_win(record[0], record[1])
    permutations *= num_ways_to_win

  print('---------- WAYS TO WIN PART 1 ----------')
  print(permutations)
  return permutations

def get_ways_to_win_part_two():
  records = get_race_records()

  race_time = ''
  race_dist = ''
  for records in records:
    race_time += str(records[0])
    race_dist += str(records[1])

  num_ways_to_win = get_number_of_ways_to_win(int(race_time), int(race_dist))

  print('---------- WAYS TO WIN PART 2 ----------')
  print(num_ways_to_win)
  return num_ways_to_win

get_ways_to_win_part_one()
get_ways_to_win_part_two()
