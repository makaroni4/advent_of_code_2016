def decompress(text):
  output = ""

  i = 0
  while i < len(text):
    if text[i] == "(":
      open_bracket_i = i

      while text[i] != ")":
        i += 1

      close_bracket_i = i

      sub_chars, times = map(int, text[open_bracket_i + 1:close_bracket_i].split("x"))

      output += text[close_bracket_i + 1:close_bracket_i + sub_chars + 1] * times

      i += sub_chars + 1
    else:
      output += text[i]

      i += 1

  return output

assert decompress("ADVENT") == "ADVENT"
assert decompress("A(1x5)BC") == "ABBBBBC"
assert decompress("(3x3)XYZ") == "XYZXYZXYZ"
assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
assert decompress("(6x1)(1x3)A") == "(1x3)A"
assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"


text = open("input.dat").read().strip()
print len(decompress(text))
