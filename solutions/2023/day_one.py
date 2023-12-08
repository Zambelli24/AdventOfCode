from aocd import get_data
import regex

DIGIT_MAP = {
  'zero': '0',
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def get_all_lines():
  return get_data(day=1, year=2023).split('\n')

def get_line_values_part_one(lines):
  line_values = []
  for line in lines:
    line_digits = regex.findall(r'[0-9]', line)
    first_digit = line_digits[0]
    last_digit = line_digits[-1]

    value = first_digit + last_digit
    line_values.append(int(value))

  print('---------- ALL LINE VALUES FOR PART 1 ----------')
  print(line_values)

  return line_values

def convert_to_digit(num_word):
  return DIGIT_MAP[num_word]

def get_line_values_part_two(lines):
  line_values = []
  for line in lines:
    line_digits = regex.findall(r'([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)
    first_digit = line_digits[0]
    last_digit = line_digits[-1]

    if first_digit in DIGIT_MAP.keys():
      first_digit = convert_to_digit(first_digit)

    if last_digit in DIGIT_MAP.keys():
      last_digit = convert_to_digit(last_digit)

    value = first_digit + last_digit
    line_values.append(int(value))

  print('---------- ALL LINE VALUES FOR PART 2 ----------')
  print(line_values)

  return line_values
  
def get_sum_of_values(part):
  if part == 1:
    line_values = get_line_values_part_one(get_all_lines())
  else:
    line_values = get_line_values_part_two(get_all_lines())
  
  sum_of_values = sum(line_values)

  print('---------- SUM OF VALUES PART ' + str(part) + '----------')
  print(sum_of_values)

  return sum_of_values

get_sum_of_values(1)
get_sum_of_values(2)