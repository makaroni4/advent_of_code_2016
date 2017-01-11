import numpy
from heapq import *

def is_closed_space(fav_number, x, y):
  val = x*x + 3*x + 2*x*y + y + y*y + fav_number

  return bin(val)[2:].count("1") % 2 == 1

def heuristic(a, b):
    return (b[0] - a[0]) + (b[1] - a[1])

def reconstruct_path(current, came_from):
  shortest_path = []

  while current in came_from:
    shortest_path.append(current)
    current = came_from[current]

  return shortest_path

def astar(fav_number, start, goal):
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  closed_set = set()
  came_from = {}
  g_scores = { start: 0 }
  open_set = []

  heappush(open_set, (heuristic(start, goal), start))

  while open_set:
    current = heappop(open_set)[1]

    if current == goal:
      return reconstruct_path(current, came_from)

    closed_set.add(current)

    for i, j in neighbors:
      neighbor = current[0] + i, current[1] + j

      if neighbor in closed_set:
        continue

      if neighbor[0] < 0 or neighbor[1] < 0:
        continue

      if is_closed_space(fav_number, neighbor[0], neighbor[1]):
        continue

      tentative_g_score = g_scores[current] + heuristic(current, neighbor)

      if neighbor not in [i[1] for i in open_set] or \
         tentative_g_score < g_scores.get(neighbor, 0):

        came_from[neighbor] = current
        g_scores[neighbor] = tentative_g_score

        f_score = tentative_g_score + heuristic(neighbor, goal)
        heappush(open_set, (f_score, neighbor))

  return False

assert len(astar(10, (1, 1), (7, 4))) == 11

print(len(astar(1358, (1, 1), (31, 39))))
