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

def shift_row(display, index, shift):
  display[index] = rotate_array(display[index], shift)

  return display

assert shift_row([['#', '.', '#', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.']], 0, 4) == [['.', '.', '.', '.', '#', '.', '#'],
                                                                  ['.', '.', '.', '.', '.', '.', '.'],
                                                                  ['.', '.', '.', '.', '.', '.', '.']]

def rotate_column(display, column, shift):
  return map(list, zip(*shift_row(zip(*display), column, shift)))

assert rotate_column([['*', '*', '*', '.', '.', '.', '.'],
                      ['*', '*', '*', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']], 1, 1) == [['*', '.', '*', '.', '.', '.', '.'],
                                                                      ['*', '*', '*', '.', '.', '.', '.'],
                                                                      ['.', '*', '.', '.', '.', '.', '.']]
