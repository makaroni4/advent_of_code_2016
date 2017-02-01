import re

def flatten(l):
  return [item for sublist in l for item in sublist]

assert flatten([["a"], ["b"]]) == ["a", "b"]

def inverse_triplet(string):
  return string[1] + string[0] + string[1]

assert inverse_triplet("aba") == "bab"
assert inverse_triplet("bab") == "aba"


def find_aba_tripltes(string):
  if len(string) < 3:
    return [  ]

  triplets = []
  i = 0

  while i + 2 < len(string):
    if string[i] == string[i + 2]:
      triplets.append(string[i:i+3])

    i += 1

  return triplets

assert find_aba_tripltes("aba") == ["aba"]
assert find_aba_tripltes("asojdabavaodsu") == ["aba", "ava"]
assert find_aba_tripltes("abaasojdabavaodsu") == ["aba", "aba", "ava"]
assert find_aba_tripltes("asodvaodsuaba") == ["aba"]
assert find_aba_tripltes("asodugn") == []


def is_valid_ip_address(ip_address):
  address_parts = []
  brackets_parts = []

  parts = re.split(r"([\[\]])", ip_address)
  i = 0

  while i < len(parts):
    if parts[i] == "[":
      brackets_parts.append(parts[i + 1])
      i += 3
    else:
      address_parts.append(parts[i])
      i += 1

  address_triplets = flatten(map(find_aba_tripltes, address_parts))
  bracket_triplets = flatten(map(find_aba_tripltes, brackets_parts))
  bracket_inverted_triplets = map(inverse_triplet, bracket_triplets)

  return bool(set(address_triplets) & set(bracket_inverted_triplets))

assert is_valid_ip_address("aba[bab]xyz") == True
assert is_valid_ip_address("aaa[kek]eke") == True
assert is_valid_ip_address("zazbz[bzb]cdb") == True
assert is_valid_ip_address("xyx[xyx]xyx") == False

ip_addresses = open("input.dat").read().strip().split("\n")
print(sum(map(is_valid_ip_address, ip_addresses)))
