# s/o https://github.com/hyper-neutrino for the help with part 2

from aocd import get_data

def get_part_one_min_location():
  raw_data = get_data(day=5, year=2023).split('\n\n')
  values = list(map(int, raw_data[0].split(':')[1].split()))
  raw_mappings = raw_data[1:]

  for mapping in raw_mappings:
    ranges = []
    for line in mapping.splitlines()[1:]:
      ranges.append(list(map(int, line.split())))

    new = []
    for value in values:
      for dest, source, rng in ranges:
        if source <= value <= source + rng:
          new.append(value - source + dest)
          break
      else:
        new.append(value)
    
    values = new

  print('---------- LOCATIONS PART 1 ----------')
  print(values)

  print('---------- MIN LOCATION PART 1 ----------')
  print(min(values))

  return min(values)

def get_part_two_min_location():
  raw_data = get_data(day=5, year=2023).split('\n\n')
  input_values = list(map(int, raw_data[0].split(':')[1].split()))

  processed_values = []
  raw_mappings = raw_data[1:]

  for i in range(0, len(input_values), 2):
    processed_values.append((input_values[i], input_values[i] + input_values[i + 1]))

  for mapping in raw_mappings:
    ranges = []
    for line in mapping.splitlines()[1:]:
      ranges.append(list(map(int, line.split())))

    new = []
    while len(processed_values) > 0:
      start, end = processed_values.pop()
      for dest, source, rng in ranges:
        overlap_start = max(start, source)
        overlap_end = min(end, source + rng)
        if overlap_start < overlap_end:
          new.append((overlap_start - source + dest, overlap_end - source + dest))
          if overlap_start > start:
            processed_values.append((start, overlap_start))
          if end > overlap_end:
            processed_values.append((overlap_end, end))
          break
      else:
        new.append((start, end))

    processed_values = new

  print('---------- LOCATIONS PART 2 ----------')
  print(processed_values)

  print('---------- MIN LOCATION PART 2 ----------')
  print(min(processed_values)[0])
  return min(processed_values)[0]

get_part_one_min_location()
get_part_two_min_location()