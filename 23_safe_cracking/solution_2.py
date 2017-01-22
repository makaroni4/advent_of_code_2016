import re

NUM_PATTERN = re.compile("-?\d+")

def extract_register_value(registers, id):
  if NUM_PATTERN.match(id):
    return int(id)
  else:
    return registers[id]

def process(registers, instructions):
  i = 0
  while i < len(instructions):
    instruction = instructions[i]
    instruction_parts = instruction.split(" ")
    command = instruction_parts.pop(0)

    if command == "cpy":
      value = extract_register_value(registers, instruction_parts[0])
      register = instruction_parts[1]

      registers[register] = value
    elif command == "inc":
      register = instruction_parts[0]

      registers[register] += 1
    elif command == "dec":
      register = instruction_parts[0]

      registers[register] -= 1
    elif command == "jnz":
      value = extract_register_value(registers, instruction_parts[0])
      shift = extract_register_value(registers, instruction_parts[1])

      # optimization using multiplication
      if instruction_parts[0] == "d" and \
         shift == -5 and \
         instructions[i - 1] == "dec d" and \
         instructions[i - 2] == "jnz c -2" and \
         instructions[i - 3] == "dec c" and \
         instructions[i - 4] == "inc a" and \
         instructions[i - 5] == "cpy b c":

        registers["a"] += registers["b"] * registers["d"]
        registers["c"] = 0
      elif value != 0:
        i += (shift - 1)
    elif command == "tgl":
      tgl_i = i + extract_register_value(registers, instruction_parts[0])

      if 0 <= tgl_i < len(instructions):
        tgl_instructions = instructions[tgl_i].split(" ")

        if len(tgl_instructions) == 2:
          if tgl_instructions[0] == "inc":
            tgl_instructions[0] = "dec"
          else:
            tgl_instructions[0] = "inc"

          instructions[tgl_i] = " ".join(tgl_instructions)
        elif len(tgl_instructions) == 3:
          if tgl_instructions[0] == "jnz":
            tgl_instructions[0] = "cpy"
          else:
            tgl_instructions[0] = "jnz"

          instructions[tgl_i] = " ".join(tgl_instructions)

    i += 1

  return registers

test_instructions = open("test_input.dat").read().strip().split("\n")
assert process(
    {"a": 0, "b": 0, "c": 0, "d": 0},
    test_instructions
  )["a"] == 3

instructions = open("input.dat").read().strip().split("\n")
print(process({"a": 12, "b": 0, "c": 0, "d": 0}, instructions)["a"])
