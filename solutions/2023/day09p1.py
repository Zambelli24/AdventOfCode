from aocd import get_data

def calculate_differences(history):
  differences = []
  for i in range(1, len(history)):
    differences.append(history[i] - history[i - 1])
  return differences

def get_history():
  history = []
  raw_data = get_data(day=9, year=2023).split('\n')

  for row in raw_data:
    original = list(map(int, row.split(' ')))
    
    differences = []
    curr_differences = calculate_differences(original)
    differences.append(curr_differences)
    
    while len(set(curr_differences)) > 1:
      curr_differences = calculate_differences(curr_differences)
      differences.append(curr_differences)
    
    differences.reverse()
    history.append({
      'history': original,
      'differences': differences,
    })

  print('---------- HISTORY ----------')
  print(history)
  return history

def get_next_value(hist):
  history = hist['history']
  differences = hist['differences']

  next = 0
  for diff in differences:
    next += diff[-1]
  next += history[-1]

  return next

def get_next_values():
  history = get_history()
  next_values = []

  for hist in history:
    next_value = get_next_value(hist)
    next_values.append(next_value)

  print('---------- NEXT VALUES ----------')
  print(next_values)
  print('---------- SUM ----------')
  print(sum(next_values))
  return sum(next_values)


get_next_values()
  