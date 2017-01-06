def rect(display, width, height):
  for y in range(0, height):
    display[y][0:width] = ["*"] * width

  return display

assert rect([['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.']], 3, 2) == [['*', '*', '*', '.', '.', '.', '.'],
                                                             ['*', '*', '*', '.', '.', '.', '.'],
                                                             ['.', '.', '.', '.', '.', '.', '.']]
