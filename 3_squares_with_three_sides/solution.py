import itertools
import re

def is_valid_triangle(sides):
  if len(sides) != 3:
    raise ValueError("Triangle should have 3 sides")

  return sides[0] < sides[1] + sides[2] and \
         sides[1] < sides[0] + sides[2] and \
         sides[2] < sides[0] + sides[1]

def count_valid_triangles(triangles):
  return sum(map(is_valid_triangle, triangles))

assert is_valid_triangle([3, 4, 5]) == True
assert is_valid_triangle([5, 10, 25]) == False
assert count_valid_triangles([[3, 4, 5], [5, 10, 25]]) == 1


triangles = open("input.dat").read().strip().split("\n")
triangles = [map(int, re.split(r"\s+", triangle.strip())) for triangle in triangles]
print count_valid_triangles(triangles)

