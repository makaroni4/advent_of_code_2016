import re
import hashlib
from collections import defaultdict

THREE_CHAR_PATTERN = re.compile(r"(\w)\1{2}")
FIVE_CHAR_PATTERN = re.compile(r"(\w)\1{4}")

def md5_digest(salt, index):
  code = salt + str(index)
  digest = hashlib.md5()
  digest.update(code.encode())
  return digest.hexdigest()

def cache_index(hashes, five_letter_char_indices, five_letter_index_chars, salt, index):
  hash_str = md5_digest(salt, index)
  five_chars = set(FIVE_CHAR_PATTERN.findall(hash_str))

  for char in five_chars:
    five_letter_char_indices[char].add(index)
    five_letter_index_chars[index].add(char)

  hashes.append(hash_str)

def uncache_index(five_letter_char_indices, five_letter_index_chars, index):
  if index in five_letter_index_chars:
    for char in five_letter_index_chars.pop(index):
      five_letter_char_indices[char].discard(index)

def generate_keys(salt):
  hashes = []
  five_letter_char_indices = defaultdict(set)
  five_letter_index_chars = defaultdict(set)
  found_keys = 0

  for i in range(0, 1001):
    cache_index(hashes, five_letter_char_indices, five_letter_index_chars, salt, i)

  i = 0
  while found_keys < 64:
    triplet_char = THREE_CHAR_PATTERN.search(hashes.pop(0))

    uncache_index(five_letter_char_indices, five_letter_index_chars, i)

    if triplet_char:
      triplet_char = triplet_char.group(1)

      if len(five_letter_char_indices[triplet_char]) > 0:
        found_keys += 1

    i += 1

    cache_index(hashes, five_letter_char_indices, five_letter_index_chars, salt, 1000 + i)

  return i - 1

assert generate_keys("abc") == 22728

print(generate_keys("ngcjuoqr"))
