def is_room_real(name):
  return True

assert is_room_real("aaaaa-bbb-z-y-x-123[abxyz]") == True
assert is_room_real("a-b-c-d-e-f-g-h-987[abcde]") == True
assert is_room_real("not-a-real-room-404[oarel]") == True
assert is_room_real("totally-real-room-200[decoy]") == False
