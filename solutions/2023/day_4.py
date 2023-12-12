from aocd import get_data

def get_all_cards():
  all_cards = []
  lines = get_data(day=4, year=2023).split('\n')
  for line in lines:
    card = {}
    line, numbers = line.split(':')
    print(line)
    id = line.split(' ')[-1]
    card['id'] = id

    processed_winners = []
    processed_numbers = []
    winning_numbers, my_numbers = numbers.split(' | ')
    winning_numbers = winning_numbers.strip().split(' ')
    for number in winning_numbers:
      if number != '':
        processed_winners.append(number)
    
    my_numbers = my_numbers.strip().split(' ')
    for number in my_numbers:
      if number != '':
        processed_numbers.append(number)

    card['winning_numbers'] = processed_winners
    card['my_numbers'] = processed_numbers
    card['winners'] = 0
    card['duplicates'] = 0

    all_cards.append(card)

  print('---------- ALL CARDS ----------')
  print(all_cards)
  return all_cards

def get_card_point_value(card):
  winning_numbers = card['winning_numbers']
  my_numbers = card['my_numbers']
  point_value = 0

  for number in my_numbers:
    if number in winning_numbers:
      if point_value == 0:
        point_value = 1
      else:
        point_value *= 2

  print('---------- POINT VALUE FOR CARD ' +  card['id'] + ' ----------')
  print(point_value)
  return point_value

def get_number_of_winners(card):
  winning_numbers = card['winning_numbers']
  my_numbers = card['my_numbers']
  winners = 0

  for number in my_numbers:
    if number in winning_numbers:
      winners += 1

  print('---------- NUMBER OF MATCHES ON CARD ' +  card['id'] + ' ----------')
  print(winners)
  return winners

def get_all_point_values():
  all_cards = get_all_cards()
  all_point_values = []

  for card in all_cards:
    point_value = get_card_point_value(card)
    all_point_values.append(point_value)

  print('---------- ALL POINT VALUES ----------')
  print(sum(all_point_values))
  return sum(all_point_values)

def get_total_scratchcards():
  all_cards = get_all_cards()
  
  for i, card in enumerate(all_cards):
    winners = get_number_of_winners(card)
    card['winners'] = winners
    
    j = 0
    while j < card['duplicates'] + 1:
      index = i + 1
      last_winner = i + winners
      while index <= last_winner:
        all_cards[index]['duplicates'] += 1
        index += 1
      j += 1

  total_cards = 0
  for card in all_cards:
    total_cards += card['duplicates'] + 1
  
  print('---------- TOTAL SCRATCHCARDS ----------')
  print(total_cards)
  return total_cards

get_all_point_values()
get_total_scratchcards()