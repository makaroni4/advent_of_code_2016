def generate_dragon_sequence(initial_state):
  output = initial_state + "0"
  for char in initial_state[::-1]:
    if char == "0":
      output += "1"
    else:
      output += "0"

  return output

assert generate_dragon_sequence("1") == "100"
assert generate_dragon_sequence("0") == "001"
assert generate_dragon_sequence("11111") == "11111000000"
assert generate_dragon_sequence("111100001010") == "1111000010100101011110000"

def fill_dragon(initial_state, max_size):
  while len(initial_state) <= max_size:
    initial_state = generate_dragon_sequence(initial_state)

  return initial_state

assert fill_dragon("10000", 20) == "10000011110010000111110"

def checksum(disk):
  output = ""

  for i in range(0, len(disk), 2):
    pair = disk[i:i + 2]

    if pair[0] == pair[1]:
      output += "1"
    else:
      output += "0"

  while len(output) % 2 == 0:
    output = checksum(output)

  return output

assert checksum("10000011110010000111") == "01100"

def hack_checksum(initial_state, disk_size):
  initial_state = fill_dragon(initial_state, disk_size)[0:disk_size]

  return checksum(initial_state)

assert hack_checksum("10000", 20) == "01100"

print(hack_checksum("11110010111001001", 35651584))
