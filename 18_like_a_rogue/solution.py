TRAP_ABC_TILES = ["^^.", ".^^", "^..", "..^"]

def make_rows(first_row, rows_count):
  rows = [first_row]

  while len(rows) < rows_count:
    next_row = ""
    previous_row = "." + rows[-1] + "."
    i = 0

    while i < len(previous_row) - 2:
      abc_tiles = previous_row[i:i+3]

      if abc_tiles in TRAP_ABC_TILES:
        next_row += "^"
      else:
        next_row += "."

      i += 1

    rows.append(next_row)

  return rows

assert make_rows("..^^.", 3) == ["..^^.", ".^^^^", "^^..^"]

def count_safe_tiles(rows):
  count = 0

  for row in rows:
    count += row.count(".")

  return count

assert count_safe_tiles(["..^^.", ".^^^^", "^^..^"]) == 6

first_row = open("input.dat").read().strip()
rows = make_rows(first_row, 40)
print(count_safe_tiles(rows))

rows = make_rows(first_row, 400000)
print(count_safe_tiles(rows))
