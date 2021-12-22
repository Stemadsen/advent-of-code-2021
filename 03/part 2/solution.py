def get_lines(filename: str) -> list[str]:
    with open(filename) as file:
        lines = file.read().split('\n')
    lines.remove('')
    return lines


input_lines = get_lines('../input.txt')
number_of_lines = len(input_lines)
number_of_columns = len(input_lines[0])
line_range = range(0, number_of_lines)
colum_range = range(0, number_of_columns)
column_bit_indices: list[dict[str, list[int]]] = []

for column in colum_range:
    bit_indices = {'0': [], '1': []}
    for i in line_range:
        bit_indices.get(input_lines[i][column]).append(i)
    column_bit_indices.append(bit_indices)

oxygen_generator_indices = list(line_range)
co2_scrubber_indices = list(line_range)

for column in colum_range:
    if len(oxygen_generator_indices) > 1:
        oxygen_generator_indices_of_1s = [i for i in column_bit_indices[column]['1'] if i in oxygen_generator_indices]
        oxygen_generator_indices = oxygen_generator_indices_of_1s \
            if len(oxygen_generator_indices_of_1s) * 2 >= len(oxygen_generator_indices) \
            else [i for i in column_bit_indices[column]['0'] if i in oxygen_generator_indices]
    if len(co2_scrubber_indices) > 1:
        co2_scrubber_indices_of_0s = [i for i in column_bit_indices[column]['0'] if i in co2_scrubber_indices]
        co2_scrubber_indices = co2_scrubber_indices_of_0s \
            if len(co2_scrubber_indices_of_0s) * 2 <= len(co2_scrubber_indices) \
            else [i for i in column_bit_indices[column]['1'] if i in co2_scrubber_indices]


print(int(input_lines[oxygen_generator_indices[0]], 2) * int(input_lines[co2_scrubber_indices[0]], 2))
