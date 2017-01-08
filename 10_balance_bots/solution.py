import bisect
from collections import defaultdict

def process_instructions(instructions):
  values = defaultdict(list)
  bots_comparisons = defaultdict(list)
  compare_queue = []

  for instruction in instructions:
    instruction_parts = instruction.split(" ")
    first_command = instruction_parts.pop(0)

    if first_command == "value":
      value = int(instruction_parts.pop(0))
      bot_id = int(instruction_parts.pop(-1))

      bisect.insort(values[bot_id], value)

      if len(values[bot_id]) == 2:
        compare_queue.append(bot_id)

    elif first_command == "bot":
      bot_id = int(instruction_parts[0])

      if instruction_parts[4] == "bot":
        bots_comparisons[bot_id].insert(0, int(instruction_parts[5]))
      else:
        bots_comparisons[bot_id].insert(0, -1)

      if instruction_parts[9] == "bot":
        bots_comparisons[bot_id].append(int(instruction_parts[10]))
      else:
        bots_comparisons[bot_id].insert(-1, -1)

  while len(compare_queue) > 0:
    bot_id = compare_queue.pop(0)

    low_bot_id, high_bot_id = bots_comparisons[bot_id]

    if low_bot_id > -1:
      bisect.insort(values[low_bot_id], values[bot_id][0])
      if len(values[low_bot_id]) == 2:
        compare_queue.append(low_bot_id)

    if high_bot_id > -1:
      bisect.insort(values[high_bot_id], values[bot_id][1])
      if len(values[high_bot_id]) == 2:
        compare_queue.append(high_bot_id)

  return dict([(":".join(map(str, v)), k) for k, v in values.iteritems()])

assert process_instructions(["value 5 goes to bot 2",
                             "bot 2 gives low to bot 1 and high to bot 0",
                             "value 3 goes to bot 1",
                             "bot 1 gives low to output 1 and high to bot 0",
                             "bot 0 gives low to output 2 and high to output 0",
                             "value 2 goes to bot 2"])["2:5"] == 2

instructions = open("input.dat").read().strip().split("\n")
print process_instructions(instructions)["17:61"]
