import md5

def find_password(door_id):
  password = [None] * 8
  found_characters = 0
  index = 0

  while found_characters < 8:
    digest = md5.new()
    digest.update(door_id + str(index))
    hexdigest = digest.hexdigest()

    if hexdigest[0:5] == "00000":
      position = int(hexdigest[5], 16)

      if position < 8 and not password[position]:
        password[position] = hexdigest[6]
        found_characters += 1

    index += 1

  return "".join(password)

assert find_password("abc") == "05ace8e3"

door_id = open("input.dat").read().strip()
print find_password(door_id)
