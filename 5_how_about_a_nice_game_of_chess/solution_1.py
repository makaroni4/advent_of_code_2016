import hashlib

def find_password(door_id):
  password = ""
  index = 0

  while len(password) < 8:
    digest = hashlib.md5()
    key = door_id + str(index)
    digest.update(key.encode())
    hexdigest = digest.hexdigest()

    if hexdigest[0:5] == "00000":
      password += hexdigest[5]

    index += 1

  return password

assert find_password("abc") == "18f47a30"

door_id = open("input.dat").read().strip()
print(find_password(door_id))
