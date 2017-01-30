from heapq import *
import operator
import re
from collections import namedtuple
import itertools
import time

def is_checkpoint(nodes, position):
  el = nodes[position]

  return el != "." and el != "#" and el != "0"

def read_input(file_name):
  rows = open(file_name).read().strip().split("\n")[1:-1]
  rows = list(map(lambda r: r[1:-1], rows))

  nodes = {}
  initial_position = ()
  total_checkpoints = 0

  for i, row in enumerate(rows):
    for j, el in enumerate(row):
      nodes[(i, j)] = "." if el == "0" else el

      if el == "0":
        initial_position = (i, j)

      if is_checkpoint(nodes, (i, j)):
        total_checkpoints += 1

  return (nodes, initial_position, total_checkpoints)

def is_closed_space(nodes, node):
  return nodes[node] == "#"

def dist(x, y):
  return abs(x[0] - y[0]) + abs(x[1] - y[1])

assert dist((1, 2), (6, 7)) == 10

def heuristic(visited_points, total_checkpoints):
  return total_checkpoints - len(visited_points)

def reconstruct_path(current, came_from):
  shortest_path = []

  while current in came_from:
    shortest_path.append(current)
    current = came_from[current]

  return shortest_path

def astar(nodes, initial_position, total_checkpoints):
  start_time = time.time()
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  counter = itertools.count()

  came_from = {}
  visited_check_points = ""
  g_scores = { (initial_position, visited_check_points): 0 }
  open_set = []

  heappush(open_set, (heuristic(visited_check_points, total_checkpoints), next(counter), initial_position, visited_check_points))

  total_checkpoints_counter = 0

  while open_set:
    _, _, position, visited_check_points = heappop(open_set)

    if total_checkpoints_counter == len(visited_check_points):
      print(str(total_checkpoints_counter) + ": " + str(visited_check_points) + " " + str(time.time() - start_time))
      start_time = time.time()
      total_checkpoints_counter += 1

    if len(visited_check_points) == total_checkpoints:
      shortest_path = reconstruct_path((position, visited_check_points), came_from)
      return len(shortest_path)

    for next_step in neighbors:
      next_position = tuple(map(operator.add, position, next_step))

      if next_position not in nodes:
        continue

      if is_closed_space(nodes, next_position):
        continue

      next_visited_check_points = str(visited_check_points)
      if is_checkpoint(nodes, next_position) and not nodes[next_position] in visited_check_points:
        next_visited_check_points = "".join(sorted(visited_check_points + nodes[next_position]))

      current_state = (position, visited_check_points)
      next_state = (next_position, next_visited_check_points)

      tentative_g_score = g_scores[current_state] + 1

      if not next_state in g_scores or \
        tentative_g_score < g_scores[next_state]:

        came_from[next_state] = current_state
        g_scores[next_state] = tentative_g_score

        f_score = tentative_g_score + heuristic(next_visited_check_points, total_checkpoints)
        heappush(open_set, (f_score, next(counter), next_position, next_visited_check_points))

  return False

test_params = read_input("test_input.dat")
assert astar(*test_params) == 14

params = read_input("input.dat")
print(astar(*params))
