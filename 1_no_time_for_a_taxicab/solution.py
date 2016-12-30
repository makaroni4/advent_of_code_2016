import numpy as np

def calculate_distance(steps):
  # FYI: https://en.wikipedia.org/wiki/Rotation_matrix
  RIGHT_TURN_MATRIX = np.array([[0, 1], [-1, 0]])
  LEFT_TURN_MATRIX = np.array([[0, -1], [1, 0]])

  coordinates = np.array([0, 0])
  direction = np.array([0, 1])

  for step in steps:
    distance = int(step[1:])

    direction = RIGHT_TURN_MATRIX.dot(direction) if step[0] == "R" else LEFT_TURN_MATRIX.dot(direction)
    coordinates = coordinates + direction.dot(distance)

  print np.absolute(coordinates).sum()

# calculate_distance(["R2"])
# calculate_distance(["L2"])
# calculate_distance(["R2", "R3"])
# calculate_distance(["R2", "R2", "R2"])
# calculate_distance(["R5", "L5", "R5", "R3"])
# calculate_distance(["R2", "R2", "R2", "R2"])

steps = open("input.dat").read().strip().split(", ")
calculate_distance(steps)
