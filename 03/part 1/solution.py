def get_lines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.read().split('\n')
    lines.remove('')
    return lines


input_lines = get_lines('../input.txt')

gamma_rate = ''
epsilon_rate = ''

for col in range(0, len(input_lines[0])):
    result = 0
    for num in input_lines:
        result += 1 if num[col] == '1' else -1
    gamma_rate += '1' if result > 0 else '0'
    epsilon_rate += '0' if result > 0 else '1'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
