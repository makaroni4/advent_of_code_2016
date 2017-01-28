from collections import deque
from collections import defaultdict
from itertools import combinations

def state_key(elevator_position, microchip_positions, generator_positions):
  key = str(elevator_position)
  for k, v in sorted(microchip_positions.items()):
    key += k + str(v)

  for k, v in sorted(generator_positions.items()):
    key += k + str(v)

  return key

assert state_key(0, {"a": 1, "b": 2}, {"c": 3, "d": 4}) == "0a1b2c3d4"

def floors_positions(microchip_positions, generator_positions):
  floors = defaultdict(list)

  for k, v in microchip_positions.items():
    floors[v].append(k)

  for k, v in generator_positions.items():
    floors[v].append(k)

  return floors

assert floors_positions({"a": 1, "b": 2}, {"c": 1, "d": 2}) == {1: ["a", "c"], 2: ["b", "d"]}

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
assert is_valid_floor_state(["HG", "LM"]) == False

def find_min_steps(microchip_positions, generator_positions):
  seen_states = set([state_key(0, microchip_positions, generator_positions)])

  min_steps = -1
  queue = deque([[0, 0, microchip_positions, generator_positions]])

  while len(queue) > 0:
    steps, elevator_position, microchip_positions, generator_positions = queue.popleft()
    floors = floors_positions(microchip_positions, generator_positions)

    if min_steps > -1 and steps > min_steps:
      continue

    possible_elevator_passengers = list(combinations(floors[elevator_position], 2)) + floors[elevator_position]

    for passengers in possible_elevator_passengers:
      if isinstance(passengers, tuple):
        pass_1, pass_2 = passengers
        if pass_1[1] != pass_2[1] and pass_1[0] != pass_2[0]:
          continue

        print(passengers)
        # check move up
        # check move down
      else:
        print(passengers)
        # check move up
        # check move down



  return min_steps

assert find_min_steps({"HM": 0, "LM": 0}, {"HG": 1, "LG": 2}) == 11
