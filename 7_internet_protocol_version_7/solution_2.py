import re

def contains_aba_triplet(string):
  if len(string) < 3:
    return False

  i = 0
  while i + 2 < len(string):
    if string[i] == string[i + 2]:
      return True

    i += 1

  return False

assert contains_aba_triplet("aba") == True
assert contains_aba_triplet("asojdabavaodsu") == True
assert contains_aba_triplet("abaasojdabavaodsu") == True
assert contains_aba_triplet("asodvaodsuaba") == True
assert contains_aba_triplet("asodugn") == False
