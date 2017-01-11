def is_open_space(fav_number, x, y):
  val = x*x + 3*x + 2*x*y + y + y*y + fav_number

  return bin(val)[2:].count("1") % 2 == 0

def find_all_locations(fav_number, max_steps, start):
  visited_locations = set()
  queue = { start: 0 }
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  while queue:
    current, current_distance = queue.popitem()

    if current_distance == max_steps:
      continue

    for i, j in neighbors:
      neighbor = current[0] + i, current[1] + j

      if neighbor in visited_locations:
        continue

      if (neighbor, current_distance + 1) in queue:
        continue

      if neighbor[0] < 0 or neighbor[1] < 0:
        continue

      if is_open_space(fav_number, neighbor[0], neighbor[1]):
        visited_locations.add(neighbor)
        queue[neighbor] = current_distance + 1

  return len(visited_locations)

assert find_all_locations(1358, 2, (1, 1)) == 5

print find_all_locations(1358, 50, (1, 1))
