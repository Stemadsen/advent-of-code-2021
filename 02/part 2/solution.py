from fileinput import FileInput
from enum import Enum

Direction = Enum('Direction', {
    'forward': 'forward',
    'down': 'down',
    'up': 'up'
})

def add_move(direction: Direction, amount: int, current_horizontal: int, current_depth: int, current_aim: int):
    horizontal = current_horizontal
    depth = current_depth
    aim = current_aim

    if direction == Direction.down:
        aim += amount
    elif direction == Direction.up:
        aim -= amount
    elif direction == Direction.forward:
        horizontal += amount
        depth += aim * amount
    return horizontal, depth, aim


horizontal = 0
depth = 0
aim = 0

file_input = FileInput('../input.txt')
while True:
    line = file_input.readline()
    if not line:
        break
    direction, amount = line.split(' ')
    horizontal, depth, aim = add_move(Direction[direction], int(amount), horizontal, depth, aim)

print(horizontal * depth)
