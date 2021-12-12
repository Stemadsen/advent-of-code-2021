from fileinput import FileInput
from enum import Enum

Direction = Enum('Direction', {
    'forward': 'forward',
    'down': 'down',
    'up': 'up'
})

def add_move(direction: Direction, amount: int, current_horizontal: int, current_depth: int):
    horizontal = current_horizontal
    depth = current_depth

    if direction == Direction.forward:
        horizontal += amount
    elif direction == Direction.down:
        depth += amount
    elif direction == Direction.up:
        depth -= amount
    return horizontal, depth


horizontal = 0
depth = 0

file_input = FileInput('../input.txt')
while True:
    line = file_input.readline()
    if not line:
        break
    direction, amount = line.split(' ')
    horizontal, depth = add_move(Direction[direction], int(amount), horizontal, depth)

print(horizontal * depth)
