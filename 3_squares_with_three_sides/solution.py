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

# https://docs.python.org/3.1/library/itertools.html#recipes
def grouper(n, iterable, fillvalue=None):
  args = [iter(iterable)] * n
  return itertools.izip_longest(*args, fillvalue=fillvalue)

def count_valid_vertical_triangles(triangles):
  valid_triangles = 0

  for triangles_group in grouper(3, triangles):
    for triangle in map(list, zip(*triangles_group)):
      if is_valid_triangle(triangle):
        valid_triangles += 1

  return valid_triangles

assert count_valid_vertical_triangles([[3, 10, 5], [4, 25, 3], [5, 5, 4]]) == 2

print count_valid_vertical_triangles(triangles)
