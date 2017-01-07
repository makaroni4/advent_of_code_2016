def decompress_len(text):
  output = 0

  i = 0

  while i < len(text):
    if text[i] == "(":
      open_bracket_i = i

      while text[i] != ")":
        i += 1

      close_bracket_i = i

      sub_chars, times = map(int, text[open_bracket_i + 1:close_bracket_i].split("x"))

      decompressed_piece = text[close_bracket_i + 1:close_bracket_i + sub_chars + 1]

      if "(" in decompressed_piece:
        decompressed_piece_len = decompress_len(decompressed_piece) * times
      else:
        decompressed_piece_len = len(decompressed_piece) * times

      output += decompressed_piece_len

      i += sub_chars + 1
    else:
      output += 1

      i += 1

  return output

assert decompress_len("ADVENT") == len("ADVENT")
assert decompress_len("A(1x5)BC") == len("ABBBBBC")
assert decompress_len("(3x3)XYZ") == len("XYZXYZXYZ")
assert decompress_len("X(8x2)(3x3)ABCY") == len("XABCABCABCABCABCABCY")
assert decompress_len("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
assert decompress_len("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445

text = open("input.dat").read().strip()
print decompress_len(text)
