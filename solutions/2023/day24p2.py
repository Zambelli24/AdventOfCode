# s/o https://github.com/hyper-neutrino for the elegant solution and intro to sympy
from aocd import get_data
import sympy

def get_hailstones():
  raw_data = get_data(year=2023, day=24).splitlines()

  hailstones = []
  for row in raw_data:
    pos, velocity = row.split(' @ ')
    x, y, z = pos.split(', ')
    vx, vy, vz = velocity.split(', ')
    hailstones.append((int(x), int(y), int(z), int(vx), int(vy), int(vz)))

  print('---------- HAILSTONES ----------')
  print(hailstones)
  return hailstones

def get_sum_rock_coords():
  xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

  hailstones = get_hailstones()
  equations = []

  for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
      continue
    solutions = [soln for soln in sympy.solve(equations)]
    if len(solutions) == 1:
      break
      
  rock = solutions[0]

  print('---------- SUM ROCK COORDINATES ----------')
  print(rock[xr] + rock[yr] + rock[zr])
  return rock[xr] + rock[yr] + rock[zr]

get_sum_rock_coords()