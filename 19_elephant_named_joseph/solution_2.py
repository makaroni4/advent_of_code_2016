import collections

def dummy_find_lucky_elf(elves):
  queue = list(range(1, elves + 1))

  while len(queue) > 1:
    queue.pop(len(queue) // 2)

    current_elve = queue.pop(0)
    queue.append(current_elve)

  return queue[0]

assert dummy_find_lucky_elf(4) == 1
assert dummy_find_lucky_elf(5) == 2
assert dummy_find_lucky_elf(6) == 3
assert dummy_find_lucky_elf(10) == 1
assert dummy_find_lucky_elf(177) == 111

def fast_find_lucky_elf(elves):
  queue1 = collections.deque(range(1, 1 + elves // 2))
  queue2 = collections.deque(range(1 + elves // 2, elves + 1))

  while queue1:
    current = queue1.popleft()

    queue2.popleft()
    queue2.append(current)

    if len(queue2) > len(queue1) + 1:
      queue1.append(queue2.popleft())

  return queue2[0]

assert fast_find_lucky_elf(4) == 1
assert fast_find_lucky_elf(5) == 2
assert fast_find_lucky_elf(6) == 3
assert fast_find_lucky_elf(10) == 1
assert fast_find_lucky_elf(177) == 111

print(fast_find_lucky_elf(3014603))
