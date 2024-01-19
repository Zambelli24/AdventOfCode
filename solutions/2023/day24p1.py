from aocd import get_data


def get_hailstones():
  raw_data = get_data(year=2023, day=24).splitlines()

  hailstones = []
  for row in raw_data:
    pos, velocity = row.split(' @ ')
    x, y, _ = pos.split(', ')
    vx, vy, _ = velocity.split(', ')
    hailstones.append((int(x), int(y), int(vx), int(vy)))

  print('---------- HAILSTONES ----------')
  print(hailstones)
  return hailstones

def line(p1, p2):
  A = (p1[1] - p2[1])
  B = (p2[0] - p1[0])
  C = (p1[0]*p2[1] - p2[0]*p1[1])
  return A, B, -C

def get_intersection_point(line1, line2):
  D = line1[0] * line2[1] - line1[1] * line2[0]
  Dx = line1[2] * line2[1] - line1[1] * line2[2]
  Dy = line1[0] * line2[2] - line1[2] * line2[0]
  if D != 0:
    x = Dx / D
    y = Dy / D
    return x, y
  else:
    return False


def get_num_intersectioning_hailstones(): 
  hailstones = get_hailstones()
  min_position = 200000000000000
  max_position = 400000000000000

  num_intersecting_hailstones = 0
  for i, hailstone in enumerate(hailstones):
    hx, hy, hvx, hvy = hailstone
    hailstone_line = line((hx, hy), (hx + hvx, hy + hvy))
    for comp_stone in hailstones[:i]:
      cx, cy, cvx, cvy = comp_stone
      comp_line = line((cx, cy), (cx + cvx, cy + cvy))
      intersection = get_intersection_point(hailstone_line, comp_line)
      if intersection:
        x, y = intersection
        hs_in_future = ((hvx > 0 and x > hx) or (hvx < 0 and x < hx)) and ((hvy > 0 and y > hy) or (hvy < 0 and y < hy))
        cs_in_future = ((cvx > 0 and x > cx) or (cvx < 0 and x < cx)) and ((cvy > 0 and y > cy) or (cvy < 0 and y < cy))
        if min_position <= x <= max_position and min_position <= y <= max_position and hs_in_future and cs_in_future:
          num_intersecting_hailstones += 1

  print('---------- NUM INTERSECTNG HAILSTONES ----------')
  print(num_intersecting_hailstones)
  return num_intersecting_hailstones

get_num_intersectioning_hailstones()

    