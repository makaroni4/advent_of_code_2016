import re

def contains_reverse_pair(string):
  if len(string) < 4:
    return False

  i = 0
  while i + 4 <= len(string):
    if string[i:i+2] != string[i+2:i+4] and string[i:i+2] == string[i+2:i+4][::-1]:
      return True

    i += 1

  return False

assert contains_reverse_pair("abba") == True
assert contains_reverse_pair("oxxoij") == True
assert contains_reverse_pair("ioxxoj") == True
assert contains_reverse_pair("ijoxxo") == True
assert contains_reverse_pair("kggkghamrhzvzkmkvzvf") == True
assert contains_reverse_pair("kghamrhzvzkmkvzvffv") == True
assert contains_reverse_pair("abc") == False
assert contains_reverse_pair("mnop") == False
assert contains_reverse_pair("aaaa") == False
assert contains_reverse_pair("zxcvbn") == False
assert contains_reverse_pair("kghamrhzvzkmkvzvf") == False

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

  return any(contains_reverse_pair(part) for part in address_parts) and not any(contains_reverse_pair(part) for part in brackets_parts)

assert is_valid_ip_address("abba[mnop]qrst") == True
assert is_valid_ip_address("ioxxoj[asdfgh]zxcvbn") == True
assert is_valid_ip_address("zxcvbn[asdfgh]ioxxoj") == True
assert is_valid_ip_address("zxcvbn[asdfgh]ioxxoj[oqiq]sandvo") == True
assert is_valid_ip_address("dinkcecgpjkucufxmmx[kghamrhzvzkmkvzvf]fsijghkzvcnruuch") == True
assert is_valid_ip_address("fsijghkzvcnruuch[kghamrhzvzkmkvzvf]dinkcecgpjkucufxmmx") == True
assert is_valid_ip_address("abcd[bddb]xyyx") == False
assert is_valid_ip_address("aaaa[qwer]tyui") == False
assert is_valid_ip_address("zxcvbn[asdfgh]ioxxoj[abba]sandvo") == False

ip_addresses = open("input.dat").read().strip().split("\n")
print(sum(map(is_valid_ip_address, ip_addresses)))
