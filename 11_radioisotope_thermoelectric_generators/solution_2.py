from itertools import combinations
from collections import defaultdict
from heapq import *
import operator
import copy
import itertools

def flatten(l):
  return [item for sublist in l for item in sublist]

def is_valid_floor_state(devices):
  floor_devices = defaultdict(list)

  for device in devices:
    element, device_type = list(device)
    floor_devices[device_type].append(element)

  if len(floor_devices) == 1:
    return True

  microchips = set(floor_devices["M"])
  generators = set(floor_devices["G"])

  if len(microchips - generators) > 0 and len(generators - microchips) > 0:
    return False

  return True

assert is_valid_floor_state(["HM", "LM"]) == True
assert is_valid_floor_state(["HG", "HM"]) == True
assert is_valid_floor_state(["HG", "HM", "LG"]) == True
assert is_valid_floor_state(["HG", "LM", "LG"]) == True
assert is_valid_floor_state(["HG", "LM", "LG", "HM"]) == True
assert is_valid_floor_state(["HG", "LM"]) == False

def state_key(elevator_position, floors):
  key = str(elevator_position)
  elements_positions = {}

  for floor, devices in floors.items():
    for device in devices:
      elements_positions[device] = floor

  for k, v in sorted(elements_positions.items()):
    key += k + str(v)

  return key

assert state_key(0, {1: ["a"], 2: ["b"], 3: ["c", "d"]}) == "0a1b2c3d3"

def heuristic(floors):
  return -len(floors[3]) * 10

def reconstruct_path(current_state_key, came_from):
  shortest_path = []

  while current_state_key in came_from:
    shortest_path.append(current_state_key)
    current_state_key = came_from[current_state_key]

  return shortest_path

def find_min_steps(floors):
  total_elements = len(flatten(floors.values()))
  came_from = {}
  g_scores = { state_key(0, floors): 0 }
  closed_set = set()
  open_set = []

  # http://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts
  counter = itertools.count()

  for key in floors.keys():
    floors[key] = sorted(floors[key])

  heappush(open_set, (0, next(counter), (0, floors)))

  while len(open_set) > 0:
    elevator_position, floors = heappop(open_set)[2]
    current_state_key = state_key(elevator_position, floors)

    if elevator_position == 3 and len(floors[elevator_position]) == total_elements:
      shortest_path = reconstruct_path(current_state_key, came_from)
      return len(shortest_path)

    closed_set.add(current_state_key)

    possible_elevator_passengers = list(map(list, combinations(floors[elevator_position], 2))) + [[d] for d in floors[elevator_position]]

    moves = []
    if elevator_position < 3:
      moves.append(1)

    if elevator_position > 0:
      moves.append(-1)

    for passengers in possible_elevator_passengers:
      for move in moves:
        next_elevator_position = elevator_position + move

        if is_valid_floor_state(passengers + floors[next_elevator_position]) and \
          is_valid_floor_state(list(set(floors[elevator_position]) - set(passengers))):

          next_floors = copy.deepcopy(floors)
          for p in passengers:
            next_floors[elevator_position].remove(p)

          next_floors[next_elevator_position] += passengers
          next_floors[next_elevator_position] = sorted(next_floors[next_elevator_position])

          next_state_key = state_key(next_elevator_position, next_floors)

          tentative_g_score = g_scores[current_state_key] + 1

          if not next_state_key in closed_set or tentative_g_score < g_scores[next_state_key]:
            came_from[next_state_key] = current_state_key
            g_scores[next_state_key] = tentative_g_score

            f_score = tentative_g_score + heuristic(next_floors)
            heappush(open_set, (f_score, next(counter), (next_elevator_position, next_floors)))

  return False

assert find_min_steps({0: ["HM", "LM"], 1: ["HG"], 2: ["LG"], 3: []}) == 9

print(find_min_steps({0: ["PG", "TG", "TM", "OG", "RG", "RM", "CG", "CM", "EG", "EM", "DG", "DM"], 1: ["PM", "OM"], 2: [], 3: []}))
