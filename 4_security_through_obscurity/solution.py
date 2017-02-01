from collections import defaultdict
import string
import functools

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

  chars = sorted(chars.items(), key=functools.cmp_to_key(chars_dict_compare))

  for index, char in enumerate(check_sum):
    if chars[index][0] != char:
      return -1

  return int(sector_id)

assert check_room("aaaaa-bbb-z-y-x-123[abxyz]") == 123
assert check_room("a-b-c-d-e-f-g-h-987[abcde]") == 987
assert check_room("not-a-real-room-404[oarel]") == 404
assert check_room("totally-real-room-200[decoy]") == -1

def count_sector_ids_sum(names):
  ids_sum = 0
  for name in names:
    sector_id = check_room(name)
    if sector_id > 0:
      ids_sum += sector_id

  return ids_sum

names = open("input.dat").read().strip().split("\n")
print(count_sector_ids_sum(names))

ALPHABET = list(string.ascii_lowercase)
ALPHABET_INDICES = dict(zip(ALPHABET, range(0, 26)))
ALPHABET_SIZE = 26

def rotate_letter(letter, times):
  letter_index = ALPHABET_INDICES[letter]

  return ALPHABET[(letter_index + times) % 26]

assert rotate_letter("a", 2) == "c"
assert rotate_letter("a", 28) == "c"

def decipher_name(name):
  encrypted_name, sector_id = name[0:-7].rsplit("-", 1)
  sector_id = int(sector_id)
  deciphered_name = ""

  for letter in encrypted_name:
    if letter == "-":
      deciphered_name += " "
    else:
      deciphered_name += rotate_letter(letter, sector_id)

  return deciphered_name

assert decipher_name("qzmt-zixmtkozy-ivhz-343[abcde]") == "very encrypted name"

for name in names:
  if decipher_name(name) == "northpole object storage":
    print(name)

