import numpy as np

def to_key(array):
  return ";".join(map(str, array))

def calculate_distance(steps):
  # FYI: https://en.wikipedia.org/wiki/Rotation_matrix
  RIGHT_TURN_MATRIX = np.array([[0, 1], [-1, 0]])
  LEFT_TURN_MATRIX = np.array([[0, -1], [1, 0]])

  coordinates = np.array([0, 0])
  direction = np.array([0, 1])
  visited_locations = set(coordinates)
  visited_twice = False

  for step in steps:
    distance = int(step[1:])

    direction = RIGHT_TURN_MATRIX.dot(direction) if step[0] == "R" else LEFT_TURN_MATRIX.dot(direction)

    for i in range(0, distance):
      coordinates = coordinates + direction

      if not visited_twice and to_key(coordinates) in visited_locations:
        visited_twice = True
        print "First location visited twice is %d blocks away" % np.absolute(coordinates).sum()
      else:
        visited_locations.add(to_key(coordinates))

  print "Bunny HQ is %d blocks away" % np.absolute(coordinates).sum()

# calculate_distance(["R2"])
# calculate_distance(["L2"])
# calculate_distance(["R2", "R3"])
# calculate_distance(["R2", "R2", "R2"])
# calculate_distance(["R5", "L5", "R5", "R3"])
# calculate_distance(["R2", "R2", "R2", "R2"])
# calculate_distance(["R8", "R4", "R4", "R8"])

steps = open("input.dat").read().strip().split(", ")
calculate_distance(steps)
