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

def get_prev_value(hist):
  history = hist['history']
  differences = hist['differences']

  prev = 0
  for diff in differences:
    prev = diff[0] - prev
  prev = history[0] - prev

  return prev

def get_prev_values():
  history = get_history()
  prev_values = []

  for hist in history:
    prev_value = get_prev_value(hist)
    prev_values.append(prev_value)

  print('---------- PREVIOUS VALUES ----------')
  print(prev_values)
  print('---------- SUM ----------')
  print(sum(prev_values))
  return sum(prev_values)

get_prev_values()
  