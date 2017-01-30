from heapq import *
import operator
import re
from collections import namedtuple
import itertools
import time

def extract_first_num(str):
  numbers = re.findall("\d+", str)
  if numbers:
    return int(numbers[0])
  else:
    return None

assert extract_first_num("abc") == None
assert extract_first_num("1abc") == 1

Node = namedtuple('Node', ['size', 'used', 'avail'])

def read_input(file_name):
  lines = open(file_name).read().strip().split("\n")[2:]
  output = {}

  for line in lines:
    parts = re.split("\s+", line)
    x, y = parts[0].split("-")[-2:]
    x = int(re.findall('\d+', x)[0])
    y = int(re.findall('\d+', y)[0])

    output[(x, y)] = Node(extract_first_num(parts[1]), extract_first_num(parts[2]), extract_first_num(parts[3]))

  return output

def is_closed_space(nodes, coord, target_coord):
  node = nodes[coord]
  target_node = nodes[target_coord]

  return node.size < target_node.used

def dist(x, y):
  return abs(x[0] - y[0]) + abs(x[1] - y[1])

assert dist((1, 2), (6, 7)) == 10

def heuristic(data_node, empty_node):
  return dist(data_node, (0, 0))

def reconstruct_path(current, came_from):
  shortest_path = []

  while current in came_from:
    shortest_path.append(current)
    current = came_from[current]

  return shortest_path

def astar(nodes):
  start_time = time.time()
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  counter = itertools.count()

  max_x = max(map(lambda c: c[0], nodes.keys()))
  empty_node = next(start for start in nodes.keys() if nodes[start].used == 0)
  data_node = (max_x, 0)
  goal = (0, 0)

  came_from = {}
  g_scores = { (data_node, empty_node): 0 }
  open_set = []

  heappush(open_set, (max_x, next(counter), data_node, empty_node))

  max_coord_counter = 33

  while open_set:
    _, _, data_node, empty_node = heappop(open_set)

    if max_coord_counter == data_node[0]:
      print(str(max_coord_counter) + ": " + str(data_node) + " " + str(time.time() - start_time))
      start_time = time.time()
      max_coord_counter -= 1

    if heuristic(data_node, empty_node) == 0:
      shortest_path = reconstruct_path((data_node, empty_node), came_from)
      return len(shortest_path)

    for next_step in neighbors:
      next_empty_node = tuple(map(operator.add, empty_node, next_step))
      next_data_node = empty_node if next_empty_node == data_node else data_node

      if next_empty_node not in nodes:
        continue

      if is_closed_space(nodes, empty_node, next_empty_node):
        continue

      tentative_g_score = g_scores[(data_node, empty_node)] + 1

      if not (next_data_node, next_empty_node) in g_scores or \
        tentative_g_score < g_scores[(next_data_node, next_empty_node)]:

        came_from[(next_data_node, next_empty_node)] = (data_node, empty_node)
        g_scores[(next_data_node, next_empty_node)] = tentative_g_score

        f_score = tentative_g_score + heuristic(next_data_node, next_empty_node)
        heappush(open_set, (f_score, next(counter), next_data_node, next_empty_node))

  return False

test_nodes = read_input("test_input.dat")
assert astar(test_nodes) == 7

nodes = read_input("input.dat")
print(astar(nodes))
