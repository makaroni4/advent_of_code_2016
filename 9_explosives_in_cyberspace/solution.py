def decompress(text):
  output = ""

  return output

assert decompress("ADVENT") == "ADVENT"
assert decompress("A(1x5)BC") == "ABBBBBC"
assert decompress("(3x3)XYZ") == "XYZXYZXYZ"
assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
assert decompress("(6x1)(1x3)A") == "(1x3)A"
assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"
