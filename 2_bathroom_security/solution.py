import numpy as np

def decode(instructions):
  code = []

  # current_index = [1, 1]
  # KEYPAD = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  current_index = [0, 2]
  KEYPAD = np.array([
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
  ])

  for instruction in instructions:
    for command in instruction:
      if command == "R" and len(KEYPAD[current_index[1]]) > current_index[0] + 1 and KEYPAD[current_index[1]][current_index[0] + 1]:
        current_index[0] += 1
      elif command == "L" and current_index[0] > 0 and KEYPAD[current_index[1]][current_index[0] - 1]:
        current_index[0] -= 1
      elif command == "U" and current_index[1] > 0 and KEYPAD[current_index[1] - 1][current_index[0]]:
        current_index[1] -= 1
      elif command == "D" and len(KEYPAD) > current_index[1] + 1 and KEYPAD[current_index[1] + 1][current_index[0]]:
        current_index[1] += 1

    code.append(KEYPAD[current_index[1]][current_index[0]])

  return "".join(map(str, code))

# assert decode(["ULL", "RRDDD", "LURDL", "UUUUD"]) == "1985"
assert decode(["ULL", "RRDDD", "LURDL", "UUUUD"]) == "5DB3"

steps = open("input.dat").read().strip().split("\n")
print(decode(steps))
