def find_lucky_elf(queue):
  if len(queue) == 1:
    return queue[0] + 1

  i = 0
  new_queue = []

  while i < len(queue):
    new_queue.append(queue[i])
    i += 2

  if len(queue) % 2 == 1:
    last_elve = new_queue.pop()
    new_queue.insert(0, last_elve)

  return find_lucky_elf(new_queue)

assert find_lucky_elf(range(0, 4)) == 1
assert find_lucky_elf(range(0, 5)) == 3

print(find_lucky_elf(range(0, 3014603)))

