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

def reverse(str, x, y):
  return str[0:x] + str[x:y + 1][::-1] + str[y + 1:]

assert reverse("abcde", 0, 4) == "edcba"
assert reverse("abcde", 1, 3) == "adcbe"



