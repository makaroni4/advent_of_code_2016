import re

def extract_first_num(str):
  numbers = re.findall("\d+", str)
  if numbers:
    return int(numbers[0])
  else:
    return None

assert extract_first_num("abc") == None
assert extract_first_num("1abc") == 1

def read_input(file_name):
  lines = open(file_name).read().strip().split("\n")[2:]
  output = []

  for line in lines:
    parts = re.split("\s+", line)
    output.append([parts[0], extract_first_num(parts[2]), extract_first_num(parts[3])])

  return output

def find_viable_pairs(nodes):
  viable_pairs = 0

  for a_node in nodes:
    for b_node in nodes:
      if b_node[0] == a_node[0]:
        continue

      if a_node[1] > 0 and a_node[1] <= b_node[2]:
        viable_pairs += 1

  return viable_pairs

nodes = read_input("input.dat")
print(find_viable_pairs(nodes))
