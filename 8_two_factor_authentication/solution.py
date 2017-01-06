def flatten(l):
  return [item for sublist in l for item in sublist]

def rect(display, width, height):
  for y in range(0, height):
    display[y][0:width] = ["*"] * width

  return display

assert rect([['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.']], 3, 2) == [['*', '*', '*', '.', '.', '.', '.'],
                                                             ['*', '*', '*', '.', '.', '.', '.'],
                                                             ['.', '.', '.', '.', '.', '.', '.']]

def rotate_array(array, shift):
  shift = shift % len(array)

  return array[-shift:] + array[0:-shift]

assert rotate_array(['#', '.', '#', '.', '.', '.', '.'], 1) == ['.', '#', '.', '#', '.', '.', '.']
assert rotate_array(['#', '.', '#', '.', '.', '.', '.'], 4) == ['.', '.', '.', '.', '#', '.', '#']

def rotate_row(display, index, shift):
  display[index] = rotate_array(display[index], shift)

  return display

assert rotate_row([['#', '.', '#', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.', '.', '.']], 0, 4) == [['.', '.', '.', '.', '#', '.', '#'],
                                                                   ['.', '.', '.', '.', '.', '.', '.'],
                                                                   ['.', '.', '.', '.', '.', '.', '.']]

def rotate_column(display, column, shift):
  return map(list, zip(*rotate_row(zip(*display), column, shift)))

assert rotate_column([['*', '*', '*', '.', '.', '.', '.'],
                      ['*', '*', '*', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']], 1, 1) == [['*', '.', '*', '.', '.', '.', '.'],
                                                                      ['*', '*', '*', '.', '.', '.', '.'],
                                                                      ['.', '*', '.', '.', '.', '.', '.']]

def rotate_display(display, direction, coordinate, shift):
  method = eval("rotate_" + direction)
  return method(display, coordinate, shift)

display = [["."] * 50] * 6

commands = open("input.dat").read().strip().split("\n")

for command in commands:
  command_parts = command.split(" ")

  command_name = command_parts.pop(0)

  if command_name == "rect":
    x, y = map(int, command_parts.pop(0).split("x"))

    display = rect(display, x, y)
  elif command_name == "rotate":
    direction, coordinate, by, value = command_parts
    coordinate = int(coordinate.split("=")[-1])

    display = rotate_display(display, direction, coordinate, int(value))
  else:
    raise ValueError("Unknown command " + command)

print sum([1 for pixel in flatten(display) if pixel == "*"])

for row in display:
  print "".join(row)











