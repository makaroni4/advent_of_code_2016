import numpy as np

def decode(instructions):
  code = []
  current_index = [1, 1]
  KEYPAD = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  for instruction in instructions:
    for command in instruction:
      if command == "R" and current_index[0] < 2:
        current_index[0] += 1
      elif command == "L" and current_index[0] > 0:
        current_index[0] -= 1
      elif command == "U" and current_index[1] > 0:
        current_index[1] -= 1
      elif command == "D" and current_index[1] < 2:
        current_index[1] += 1

    code.append(KEYPAD[current_index[1]][current_index[0]])

  print "".join(map(str, code))

# decode(["ULL", "RRDDD", "LURDL", "UUUUD"])

steps = open("input.dat").read().strip().split("\n")
decode(steps)
