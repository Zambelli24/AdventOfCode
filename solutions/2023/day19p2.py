# s/o https://github.com/hyper-neutrino for the help - solution for part 1 not efficent enough for part 2

from aocd import get_data


def get_workflows():  
  raw_worflows, _ = get_data(day=19, year=2023).split("\n\n")

  workflows = {}

  for line in raw_worflows.splitlines():
      name, rest = line[:-1].split("{")
      rules = rest.split(",")
      workflows[name] = ([], rules.pop())
      for rule in rules:
          comparison, target = rule.split(":")
          key = comparison[0]
          cmp = comparison[1]
          value = int(comparison[2:])
          workflows[name][0].append((key, cmp, value, target))
  
  return workflows

def get_num_accepted_parts(workflows, ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            pass_range = (lo, min(n - 1, hi))
            fail_range = (max(n, lo), hi)
        else:
            pass_range = (max(n + 1, lo), hi)
            fail_range = (lo, min(n, hi))
        if pass_range[0] <= pass_range[1]:
            copy = dict(ranges)
            copy[key] = pass_range
            total += get_num_accepted_parts(workflows, copy, target)
        if fail_range[0] <= fail_range[1]:
            ranges = dict(ranges)
            ranges[key] = fail_range
        else:
            break
    else:
        total += get_num_accepted_parts(workflows, ranges, fallback)
            
    return total

def get_all_accepted_parts():
  workflows = get_workflows()
  accepted_parts = get_num_accepted_parts(workflows, {key: (1, 4000) for key in "xmas"})

  print('---------- NUM ACCEPTED PARTS ----------')
  print(accepted_parts)
  return accepted_parts

get_all_accepted_parts()