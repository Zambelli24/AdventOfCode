from aocd import get_data

def get_patterns():
  raw_data = get_data(day=13, year=2023)
  patterns = []
  
  for pattern in raw_data.split('\n\n'):
    pattern = pattern.split('\n')
    
    curr_pattern = []
    for row in pattern:
      curr_pattern.append(row)

    print(curr_pattern)
    patterns.append(curr_pattern)

  print('---------- PATTERNS ----------')
  print(patterns)
  return patterns

def get_reflection_point(pattern):
  reflection_type = ''
  reflection_index = None

  for i, row in enumerate(pattern):
    if i < len(pattern) - 1 and row == pattern[i+1]:
      reflection_type = 'row'
      reflection_index = i

      above = i-1
      below = i+2
      while above >= 0 and below < len(pattern):
        if pattern[above] != pattern[below]:
          reflection_type = ''
          reflection_index = None

        above -= 1
        below += 1

    if reflection_type != '':
      break
    
  for i in range(len(pattern[0])):
    col = [row[i] for row in pattern]
    if i < len(pattern[0]) - 1 and col == [row[i+1] for row in pattern]:
      reflection_type = 'col'
      reflection_index = i

      left = i-1
      right = i+2
      while left >= 0 and right < len(pattern[0]):
        if [row[left] for row in pattern] != [row[right] for row in pattern]:
          reflection_type = ''
          reflection_index = None

        left -= 1
        right += 1
    
    if reflection_type != '':
      break
    
  print('---------- REFLECTION POINT ----------')
  print(reflection_type, reflection_index)
  return reflection_type, reflection_index

def get_pattern_summary():
  summary = 0
  for pattern in get_patterns():
    type, index = get_reflection_point(pattern)
    if type == 'row':
      summary += (index+1)*100
    elif type == 'col':
      summary += index+1

  print('---------- SUMMARY ----------')
  print(summary)
  return summary

get_pattern_summary()
