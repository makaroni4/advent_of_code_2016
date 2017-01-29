from collections import deque
from collections import defaultdict
from itertools import combinations
import copy

def flatten(l):
  return [item for sublist in l for item in sublist]

def print_state(state):
  elevator_position = int(state[0])

  floors = defaultdict(list)
  i = 0
  state = state[1:]
  while i < len(state):
    s = state[i:i+3]
    floors[int(s[-1])].append(s[0:-1])
    i += 3

  total_elements = len(flatten(floors.values()))
  output = [x[:] for x in [[".  "] * (total_elements + 2)] * 4]

  output[3 - elevator_position][1] = "E  "

  for i in range(0, 4):
    output[i][0] = "F" + str(4 - i) + " "

  inverted_floors = {}
  for floor, devices in floors.items():
    for device in devices:
      inverted_floors[device] = floor

  for ix, device in enumerate(sorted(inverted_floors.keys())):
    output[3 - inverted_floors[device]][2 + ix] = device + " "

  for row in output:
    print(" ".join(row))
  print("\n")

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

def find_min_steps(floors):
  total_elements = len(flatten(floors.values()))
  init_state = state_key(0, floors)
  seen_states = set([init_state])

  min_steps = -1
  # min_history = []
  # queue = deque([[0, 0, floors, [init_state]]])
  queue = deque([[0, 0, floors]])

  while len(queue) > 0:
    # steps, elevator_position, floors, history = queue.popleft()
    steps, elevator_position, floors = queue.popleft()

    if min_steps > -1 and steps > min_steps:
      continue

    if elevator_position == 3 and len(floors[elevator_position]) == total_elements:
      if min_steps == -1 or min_steps > steps:
        min_steps = steps
        # min_history = history

      continue

    possible_elevator_passengers = list(map(list, combinations(floors[elevator_position], 2))) + [[d] for d in floors[elevator_position]]

    for passengers in possible_elevator_passengers:
      if len(passengers) == 2:
        pass_1, pass_2 = passengers
        if pass_1[1] != pass_2[1] and pass_1[0] != pass_2[0]:
          continue

      # check move up
      if elevator_position < 3:
        if is_valid_floor_state(passengers + floors[elevator_position + 1]) and is_valid_floor_state(list(set(floors[elevator_position]) - set(passengers))):
          next_floors = copy.deepcopy(floors)
          for p in passengers:
            next_floors[elevator_position].remove(p)
          next_floors[elevator_position + 1] += passengers
          next_state_key = state_key(elevator_position + 1, next_floors)

          if not next_state_key in seen_states and (min_steps == -1 or (steps + 1) < min_steps):
            seen_states.add(next_state_key)
            # next_history = list(history)
            # next_history.append(next_state_key)
            # queue.append([steps + 1, elevator_position + 1, next_floors, next_history])
            queue.append([steps + 1, elevator_position + 1, next_floors])

      # check move down
      if elevator_position > 0:
        if is_valid_floor_state(passengers + floors[elevator_position - 1]) and is_valid_floor_state(list(set(floors[elevator_position]) - set(passengers))):
          next_floors = copy.deepcopy(floors)
          for p in passengers:
            next_floors[elevator_position].remove(p)
          next_floors[elevator_position - 1] += passengers
          next_state_key = state_key(elevator_position - 1, next_floors)

          if not next_state_key in seen_states and (min_steps == -1 or (steps + 1) < min_steps):
            seen_states.add(next_state_key)
            # next_history = list(history)
            # next_history.append(next_state_key)
            # queue.append([steps + 1, elevator_position - 1, next_floors, next_history])
            queue.append([steps + 1, elevator_position - 1, next_floors])

  # print(min_steps)
  # print(min_history)
  # for state in min_history:
  #   print_state(state)

  return min_steps

assert find_min_steps({0: ["HM", "LM"], 1: ["HG"], 2: ["LG"], 3: []}) == 9

print(find_min_steps({0: ["PG", "TG", "TM", "OG", "RG", "RM", "CG", "CM"], 1: ["PM", "OM"], 2: [], 3: []}))
