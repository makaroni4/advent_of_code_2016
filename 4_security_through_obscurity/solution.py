from collections import defaultdict

def chars_dict_compare(i1, i2):
  if i2[1] > i1[1]:
    return 1
  elif i2[1] < i1[1]:
    return -1
  elif i2[1] == i1[1]:
    if i2[0] > i1[0]:
      return -1
    elif i2[0] < i1[0]:
      return 1
    else:
      return 0

def check_room(name):
  check_sum = name[-6:-1]
  encrypted_name, sector_id = name[0:-7].rsplit("-", 1)
  encrypted_name = encrypted_name.replace("-", "")

  chars = defaultdict(int)
  for char in encrypted_name:
    chars[char] += 1

  chars = sorted(chars.items(), cmp=chars_dict_compare)

  for index, char in enumerate(check_sum):
    if chars[index][0] != char:
      return -1

  return int(sector_id)

assert check_room("aaaaa-bbb-z-y-x-123[abxyz]") == 123
assert check_room("a-b-c-d-e-f-g-h-987[abcde]") == 987
assert check_room("not-a-real-room-404[oarel]") == 404
assert check_room("totally-real-room-200[decoy]") == -1

names = open("input.dat").read().strip().split("\n")

ids_sum = 0
for name in names:
  sector_id = check_room(name)
  if sector_id > 0:
    ids_sum += sector_id

print ids_sum
