import math

def brute_force_find_lucky_elf(queue):
  while len(queue) > 1:
    queue.pop(int(len(queue) / 2))

    current_elve = queue.pop(0)
    queue.append(current_elve)

  return queue[0]

assert brute_force_find_lucky_elf(list(range(1, 6))) == 2
assert brute_force_find_lucky_elf(list(range(1, 5))) == 1

