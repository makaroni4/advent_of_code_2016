import re

NUM_PATTERN = re.compile("\d+")

def extract_register_value(registers, id):
  if NUM_PATTERN.match(id):
    return int(id)
  else:
    return registers[id]

def process(instructions):
  registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
  }

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
      shift = int(instruction_parts[1])

      if value != 0:
        i += (shift - 1)

    i += 1

  return registers

assert process(["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"])["a"] == 42

instructions = open("input.dat").read().strip().split("\n")
print(process(instructions)["a"])
