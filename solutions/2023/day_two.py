from aocd import get_data

CUBE_LIMITS = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def get_all_lines():
  return get_data(day=2, year=2023).split('\n')

def get_game_details(line, part):
  game = {}
  line = line.split(': ')

  game['id'] = int(line[0].split(' ')[1])
  game['rounds'] = []

  rounds = line[1].split(';')
  for round in rounds:
    cube_counts = round.split(',')
    round_result = {}

    for count in cube_counts:
      count, color = count.strip().split(' ')
      round_result[color] = int(count)

      if part == 1 and int(count) > CUBE_LIMITS[color]:
        round_result['impossible'] = True

      game['rounds'].append(round_result)

  if part == 1:
    impossible = False
    for round in game['rounds']:
      if 'impossible' in round.keys():
        impossible = True
    game['impossible'] = impossible
  else:
    min_set = {
      'red': 1,
      'green': 1,
      'blue': 1,
    }
    for round in game['rounds']:
      for color in round.keys():
        count = round[color]
        if count > min_set[color]:
          min_set[color] = count
    game['min_set'] = min_set

  return game

def get_all_games(part):
  all_lines = get_all_lines()
  games = []
  
  for line in all_lines:
    games.append(get_game_details(line, part))

  print('---------- ALL GAMES ----------')
  print(games)
  return games

def get_sum_of_possible_games():
  games = get_all_games(1)
  possible_games = []

  for game in games:
    if game['impossible'] == False:
      possible_games.append(game['id'])

  print('---------- POSSIBLE GAMES ----------')
  print(possible_games)

  print('---------- SUM OF POSSIBLE GAMES ----------')
  print(sum(possible_games))

  return sum(possible_games)

def get_sum_of_min_cube_sets():
  games = get_all_games(2)
  game_powers = []

  for game in games:
    game_power = 1
    for color in game['min_set'].keys():
      game_power *= game['min_set'][color]
    game_powers.append(game_power)

  print('---------- GAME POWERS ----------')
  print(game_powers)
  print('---------- SUM OF ALL GAME POWERS ----------')
  print(sum(game_powers))

  return sum(game_powers)


get_sum_of_possible_games()
get_sum_of_min_cube_sets()