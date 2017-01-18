import collections
import hashlib
import operator

OPEN_MOVE_CODES = set(["b", "c", "d", "e", "f"])
NEXT_MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
NEXT_MOVES_CODES = ["U", "D", "L", "R"]

def available_moves(passcode, path, current_position):
  str = passcode + path
  move_codes = hashlib.md5(str.encode()).hexdigest()[0:4]
  available_moves = []

  for i, move_code in enumerate(move_codes):
    if move_code in OPEN_MOVE_CODES:
      new_position = tuple(map(operator.add, current_position, NEXT_MOVES[i]))
      if 0 <= new_position[0] < 4 and 0 <= new_position[1] < 4:
        available_moves.append([path + NEXT_MOVES_CODES[i], new_position])

  return available_moves

assert available_moves("hijkl", "", (0, 0)) == [["D", (0, 1)]]
assert available_moves("hijkl", "D", (0, 1)) == [["DU", (0, 0), ], ["DR", (1, 1)]]

def brute_force_search(passcode):
  current_max_path = ""
  queue = collections.deque([["", (0, 0)]])

  while len(queue) > 0:
    current_path, current_position = queue.popleft()

    for move in available_moves(passcode, current_path, current_position):
      current_path, current_position = move

      if current_position == (3, 3):
        if len(current_max_path) == 0 or len(current_max_path) < len(current_path):
          current_max_path = current_path
      else:
        queue.append([current_path, current_position])

  return len(current_max_path)

assert brute_force_search("hijkl") == 0
assert brute_force_search("ihgpwlah") == 370
assert brute_force_search("kglvqrro") == 492
assert brute_force_search("ulqzkmiv") == 830

print(brute_force_search("pslxynzg"))
