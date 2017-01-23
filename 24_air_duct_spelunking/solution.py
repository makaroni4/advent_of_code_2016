import collections
import re
import operator

NUM_PATTERN = re.compile("\d+")
NEXT_MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
NEXT_MOVES_CODES = ["U", "D", "L", "R"]

def brute_force_search(map_file):
  rows = open(map_file).read().strip().split("\n")[1:-1]
  rows = list(map(lambda r: r[1:-1], rows))
  row_size = len(rows[0])

  initial_position = ()
  for j, row in enumerate(rows):
    i = row.find("0")
    if i > -1:
      initial_position = (i, j)
      break

  total_checkpoints = 0
  for row in rows:
    for c in row:
      if NUM_PATTERN.match(c):
        total_checkpoints += 1

  shortest_path = ""
  queue = collections.deque([["", set(["0"]), initial_position, (0, 0)]])

  while len(queue) > 0:
    queue_item = queue.popleft()
    back_move = tuple(map(lambda r: r * -1, queue_item.pop()))
    current_position = queue_item.pop()
    current_path, current_visited_checkpoints = queue_item

    for move_i, move in enumerate(NEXT_MOVES):
      if back_move == move:
        continue

      next_position = tuple(map(operator.add, current_position, move))
      next_current_path = current_path + NEXT_MOVES_CODES[move_i]
      curr_x, curr_y = next_position

      if curr_y >= len(rows) or curr_y < 0 or curr_x >= row_size or curr_x < 0:
        continue
      elif rows[curr_y][curr_x] == "#":
        continue
      elif rows[curr_y][curr_x] == ".":
        if shortest_path == "" or len(shortest_path) > len(next_current_path):
          queue.append([next_current_path, current_visited_checkpoints, next_position, move])
      elif NUM_PATTERN.match(rows[curr_y][curr_x]):
        if rows[curr_y][curr_x] in current_visited_checkpoints:
          if shortest_path == "" or len(shortest_path) > len(next_current_path):
            queue.append([next_current_path, current_visited_checkpoints, next_position, move])
        else:
          new_current_visited_checkpoints = set(current_visited_checkpoints)
          new_current_visited_checkpoints.add(rows[curr_y][curr_x])

          if len(new_current_visited_checkpoints) == total_checkpoints:
            if shortest_path == "" or len(shortest_path) > len(next_current_path):
              shortest_path = next_current_path
          else:
            queue.append([next_current_path, new_current_visited_checkpoints, next_position, (0, 0)])


  return len(shortest_path)

assert brute_force_search("test_input.dat") == 14

print(brute_force_search("input.dat"))
