import re

NUM_PATTERN = re.compile("-?\d+")

def extract_register_value(registers, id):
  if NUM_PATTERN.match(id):
    return int(id)
  else:
    return registers[id]

def process(registers, instructions):
  clock_signal = None
  clock_i = 0
  i = 0

  while i < len(instructions) and clock_i < 100:
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
    elif command == "out":
      value = extract_register_value(registers, instruction_parts[0])

      if value in [0, 1]:
        clock_i += 1
      else:
        print("False")
        return False

      if value == clock_signal:
        return False
      else:
        clock_signal = value
    elif command == "dec":
      register = instruction_parts[0]

      registers[register] -= 1
    elif command == "jnz":
      value = extract_register_value(registers, instruction_parts[0])
      shift = extract_register_value(registers, instruction_parts[1])

      if value != 0:
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

  return True

instructions = open("input.dat").read().strip().split("\n")

a = 0
while not process({"a": a, "b": 0, "c": 0, "d": 0}, instructions):
  a += 1

print(a)
