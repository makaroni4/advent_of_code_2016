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

def move_x_to_y(str, x, y):
  chars = list(str)
  char = chars.pop(x)
  chars.insert(y, char)

  return "".join(chars)

assert move_x_to_y("bcdea", 1, 4) == "bdeac"

def rotate(str, direction, steps):
  steps = steps % len(str)

  n = -1 * direction * steps

  return str[n:] + str[:n]

assert rotate("abcd", 1, 1) == "dabc"
assert rotate("abcd", -1, 1) == "bcda"

def rotate_pos(str, letter):
  letter_pos = str.find(letter)
  steps = 1 + letter_pos

  if letter_pos >= 4:
    steps += 1

  return rotate(str, 1, steps)

assert rotate_pos("ecabd", "d") == "decab"

def process_command(str, command):
  command_words = command.split(" ")

  if command_words[0] == "swap":
    if command_words[1] == "position":
      return swap_x_and_y(str, int(command_words[2]), int(command_words[5]))
    elif command_words[1] == "letter":
      return swap_letter_x_and_y(str, command_words[2], command_words[5])
    else:
      raise ValueError("Wrong command " + command)
  elif command_words[0] == "rotate":
    if command_words[1] == "based":
      return rotate_pos(str, command_words[6])
    elif command_words[1] == "left":
      return rotate(str, -1, int(command_words[2]))
    elif command_words[1] == "right":
      return rotate(str, 1, int(command_words[2]))
    else:
      raise ValueError("Wrong command " + command)
  elif command_words[0] == "reverse":
    return reverse(str, int(command_words[2]), int(command_words[4]))
  elif command_words[0] == "move":
    return move_x_to_y(str, int(command_words[2]), int(command_words[5]))
  else:
    raise ValueError("Wrong command " + command)

def scramble(str, commands_file):
  commands = open(commands_file).read().strip().split("\n")

  for command in commands:
    str = process_command(str, command)

  return str

assert scramble("abcde", "test_input.dat") == "decab"

print scramble("abcdefgh", "input.dat")
