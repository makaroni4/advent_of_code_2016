import re

def extract_first_num(str):
  numbers = re.findall("\d+", str)
  if numbers:
    return int(numbers[0])
  else:
    return None

def read_init_positions(file_name):
  lines = open(file_name).read().strip().split("\n")

  positions = []
  for line in lines:
    parts = line.split(" ")
    positions.append([int(parts[3]), extract_first_num(parts[11])])

  return positions

def find_waiting_time(disks):
  t = 0
  can_pass_through = False

  while not can_pass_through:
    for i, disk in enumerate(disks):
      can_pass_through = (disk[1] + t + i + 1) % disk[0] == 0

      if not can_pass_through:
        break

    t += 1

  return t - 1

assert find_waiting_time([[5, 4], [2, 1]]) == 5

init_positions = read_init_positions("input.dat")
print(find_waiting_time(init_positions))

init_positions.append([11, 0])
print(find_waiting_time(init_positions))
