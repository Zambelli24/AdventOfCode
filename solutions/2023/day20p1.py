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

def send_pulse(config):
  next = [('', '-', 'broadcaster')]

  num_low_pulses = 0
  num_high_pulses = 0

  while len(next) > 0:
    sender, pulse, receiver = next.pop(0)
    if pulse == '-':
      num_low_pulses += 1
    else:
      num_high_pulses += 1

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
    
  print('---------- NUM LOW PULSES ----------')
  print(num_low_pulses)
  print('---------- NUM HIGH PULSES ----------')
  print(num_high_pulses)
  return num_low_pulses, num_high_pulses

def send_all_pulses():
  config = get_configuration()
  
  total_low_pulses = 0
  total_high_pulses = 0

  for _ in range(1000):
    low_pulses, high_pulses = send_pulse(config)
    total_low_pulses += low_pulses
    total_high_pulses += high_pulses

  print('---------- TOTAL LOW PULSES ----------')
  print(total_low_pulses)
  print('---------- TOTAL HIGH PULSES ----------')
  print(total_high_pulses)
  print('---------- PRODUCT OF PULSES ----------')
  print(total_low_pulses * total_high_pulses)
  return total_low_pulses * total_high_pulses

send_all_pulses()
    