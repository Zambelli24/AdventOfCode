from aocd import get_data


def get_workflow_and_parts():
  workflows, parts = get_data(day=19, year=2023).split("\n\n")

  workflow_map = {}
  for workflow in workflows.split("\n"):
      name, conditions = workflow[:-1].split("{")
      conditions = conditions.split(",")
      default = conditions.pop(-1)

      mapped_conditions = []
      for condition in conditions:
          cond, outcome = condition.split(":")
          if '>' in cond:
            cond = cond.split(">")
            mapped_conditions.append((cond[0], '>', int(cond[1]), outcome))
          elif '<' in cond:
            cond = cond.split("<")
            mapped_conditions.append((cond[0], '<', int(cond[1]), outcome))

      workflow_map[name] = { 'default': default, 'conditions': mapped_conditions }

  parts_to_process = []
  for part in parts.split("\n"):
      pieces = part[1:-1].split(",")

      obj = {'x': 0, 'm': 0, 'a': 0, 's': 0}
      for piece in pieces:
        category, value = piece.split("=")
        obj[category] = int(value)
      
      parts_to_process.append(obj)

  print('---------- WORKFLOW MAP ----------')
  print(workflow_map)
  print('---------- PARTS TO PROCESS ----------')
  print(parts_to_process)
  return workflow_map, parts_to_process

def get_sum_all_accepted_parts():
  workflows, parts = get_workflow_and_parts()
  sum_accepted_parts = 0

  for part in parts:
    curr_wf = 'in'

    while curr_wf not in 'AR':
      no_match = True
      wf = workflows[curr_wf]
      for condition in wf['conditions']:
        match = False
        if condition[1] == '>':
          match = part[condition[0]] > condition[2]
        elif condition[1] == '<':
          match = part[condition[0]] <= condition[2]
        
        if match:
          curr_wf = condition[3]
          no_match = False
          break

      if no_match:
        curr_wf = wf['default']

    if curr_wf == 'A':
      sum_accepted_parts += part['x'] + part['m'] + part['a'] + part['s']

  print('---------- SUM OF ACCEPTED PARTS ----------')
  print(sum_accepted_parts)
  return sum_accepted_parts

get_sum_all_accepted_parts()