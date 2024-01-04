# s/o https://github.com/hyper-neutrino for a great explanation of part 2

import math
from aocd import get_data

def get_configuration():
  data = get_data(year=2023, day=20).splitlines()
  config = {}
  for module in data:
    source, dest = module.split(' -> ')
      
    mod = {}
    if source.startswith('%'):
        mod['type'] = source[0]
        source = source[1:]
        mod['state'] = 0
    elif source.startswith('&'):
        mod['type'] = source[0]
        source = source[1:]
        mod['sources'] = {}
    else:
        mod['type'] = 'S'

    dests = dest.split(', ')
    mod['dests'] = dests
    
    config[source] = mod

  for key in config.keys():
    dests = config[key]['dests']
    for d in dests:
       if d in config.keys():
        dest_config = config[d]
        if dest_config['type'] == '&':
            dest_config['sources'][key] = '-'
           

  print('---------- CONFIGURATION ----------')
  print(config)
  return config

def send_pulse(config, cycle_lengths, seen, feed, num_button_presses):
  next = [('', '-', 'broadcaster')]

  num_low_pulses = 0
  num_high_pulses = 0

  while len(next) > 0:
    sender, pulse, receiver = next.pop(0)

    if receiver == feed and pulse == '+':
      seen[sender] += 1

      if sender not in cycle_lengths:
          cycle_lengths[sender] = num_button_presses
      else:
          assert num_button_presses == seen[sender] * cycle_lengths[sender]
          
      if all(seen.values()):
          x = 1
          for cycle_length in cycle_lengths.values():
              x = x * cycle_length // math.gcd(x, cycle_length)
          return x

    if receiver in config.keys():
      add_dests = True
      curr = config[receiver]
      
      if curr['type'] == '%':
        if pulse == '-':
          if curr['state'] == 0:
              curr['state'] = 1
              pulse = '+'
          else:
              curr['state'] = 0
        else:
          add_dests = False
      elif curr['type'] == '&':
        sources = curr['sources']
        sources[sender] = pulse
        latest_pulses = set(sources.values())
        pulse = '-' if len(latest_pulses) == 1 and '+' in latest_pulses else '+'

            
      if add_dests:
        for dest in curr['dests']:
          next.append((receiver, pulse, dest))
    else:
      if pulse == '-':
        num_low_pulses += 1
      else:
        num_high_pulses += 1

  return False
  

def send_all_pulses():
  config = get_configuration()

  (feed,) = [name for name, module in config.items() if 'rx' in module['dests']]
  
  cycle_lengths = {}
  seen = {name: 0 for name, module in config.items() if feed in module['dests']}

  num_button_presses = 0
  is_complete = False
  while not is_complete:
    num_button_presses += 1
    is_complete = send_pulse(config, cycle_lengths, seen, feed, num_button_presses)

  num_button_presses = is_complete

  print('---------- NUM BUTTON PRESSES ----------')
  print(num_button_presses)
  return num_button_presses

send_all_pulses()
    