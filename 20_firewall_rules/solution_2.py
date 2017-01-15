def find_lowest_ip(ranges):
  ranges = list(map(lambda r: list(map(int, r.split("-"))), ranges))
  ranges = sorted(ranges, key=lambda r: r[0])

  valid_ranges = []

  if ranges[0][0] > 0:
    return 0

  while len(ranges) > 1:
    range1 = ranges.pop(0)
    range2 = ranges.pop(0)

    if range2[0] > range1[1] + 1:
      valid_ranges.append([range1[1] + 1, range2[0] - 1])
      new_range = [range1[0], range2[1]]
      ranges.insert(0, new_range)
    elif range2[1] > range1[1]:
      new_range = [range1[0], range2[1]]
      ranges.insert(0, new_range)
    else:
      ranges.insert(0, range1)

  if ranges[0][1] < 4294967295:
    valid_ranges.append([ranges[0][1] + 1, 4294967295])

  valid_ips = 0
  for r in valid_ranges:
    valid_ips += r[1] - r[0] + 1

  return valid_ips

assert find_lowest_ip(["0-1", "2-3", "4-5"]) == 4294967290

ranges = open("input.dat").read().strip().split("\n")
print(find_lowest_ip(ranges))
