def swap_x_and_y(str, x, y):
  chars = list(str)
  chars[y], chars[x] = chars[x], chars[y]

  return "".join(chars)

assert swap_x_and_y("abcde", 0, 4) == "ebcda"

def swap_letter_x_and_y(str, x, y):
  x_pos = str.find(x)
  y_pos = str.find(y)

  return swap_x_and_y(str, x_pos, y_pos)

assert swap_letter_x_and_y("abcde", "a", "e") == "ebcda"
