from aocd import get_data

CARD_VALUE = {
  'A': 13,
  'K': 12,
  'Q': 11,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2,
  'J': 1,
}

HAND_STRENGTH = {
  '5kind': 7,
  '4kind': 6,
  'fullhouse': 5,
  '3kind': 4,
  '2pair': 3,
  'pair': 2,
  'highcard': 1,
}

def determine_hand_type(cards):
  card_map = {}
  for char in cards:
    if char in card_map.keys():
      card_map[char] += 1
    else:
      card_map[char] = 1

  counts = card_map.values()
  if 'J' in card_map.keys() and len(counts) > 1:
    jokers = card_map['J']
    del card_map['J']
    counts = sorted(card_map.values())
    adjusted = counts[-1] + jokers
    counts.pop()
    counts.append(adjusted)

  if len(counts) == 1:
    return '5kind'
  elif len(counts) == 5:
    return 'highcard'
  elif 4 in counts:
    return '4kind'
  elif 3 in counts and 2 in counts:
    return 'fullhouse'
  elif 3 in counts:
    return '3kind'
  elif 2 in counts and len(counts) == 3:
    return '2pair'
  else:
    return 'pair'

def get_all_hands():
  hands = []
  raw_data = get_data(day=7, year=2023).split('\n')
  
  for line in raw_data:
    line = line.split(' ')
    hand = {
      'bid': int(line[1]),
      'cards': line[0],
      'card1': CARD_VALUE[line[0][0]],
      'card2': CARD_VALUE[line[0][1]],
      'card3': CARD_VALUE[line[0][2]],
      'card4': CARD_VALUE[line[0][3]],
      'card5': CARD_VALUE[line[0][4]],
      'type': determine_hand_type(line[0]),
    }
    hands.append(hand)
  
  print('---------- HANDS ----------')
  print(hands)
  return hands

def sort_hands():
  all_hands = get_all_hands()
  sorted_hands = sorted(all_hands, key=lambda hand: (HAND_STRENGTH[hand['type']], hand['card1'], hand['card2'], hand['card3'], hand['card4'], hand['card5']))
  print('---------- SORTED HANDS ----------')
  print(sorted_hands)
  return sorted_hands

def get_total_winnings():
  sorted_hands = sort_hands()
  total_winnings = 0
  for i, hand in enumerate(sorted_hands):
    total_winnings += hand['bid'] * (i + 1)

  print('---------- TOTAL WINNINGS ----------')
  print(total_winnings)
  return total_winnings

get_total_winnings()