import md5

def find_password(door_id):
  password = ""
  index = 0

  while len(password) < 8:
    digest = md5.new()
    digest.update(door_id + str(index))
    hexdigest = digest.hexdigest()

    if hexdigest[0:5] == "00000":
      password += hexdigest[5]

    index += 1

  return password

assert find_password("abc") == "18f47a30"

door_id = open("input.dat").read().strip()
print find_password(door_id)
