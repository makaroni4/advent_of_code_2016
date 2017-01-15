def find_lowest_ip(ranges):
  ranges = list(map(lambda r: list(map(int, r.split("-"))), ranges))
  ranges = sorted(ranges, key=lambda r: r[0])

  if ranges[0][0] > 0:
    return 0

  while len(ranges) > 1:
    range1 = ranges.pop(0)
    range2 = ranges.pop(0)

    if range2[0] > range1[1] + 1:
      return range1[1] + 1
    elif range2[1] > range1[1]:
      new_range = [range1[0], range2[1]]
      ranges.insert(0, new_range)
    else:
      ranges.insert(0, range1)

  return ranges[0][1] + 1

assert find_lowest_ip(["5-8", "1-2", "4-7"]) == 0
assert find_lowest_ip(["5-8", "0-2", "4-7"]) == 3
assert find_lowest_ip(["5-8", "0-6", "4-7"]) == 9
assert find_lowest_ip(["0-1", "2-3", "4-5"]) == 6

ranges = open("input.dat").read().strip().split("\n")
print(find_lowest_ip(ranges))
