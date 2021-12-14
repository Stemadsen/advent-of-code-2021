input_template = 'FNFPPNKPPHSOKFFHOFOC'
input_rules = {
    'VS': 'B',
    'SV': 'C',
    'PP': 'N',
    'NS': 'N',
    'BC': 'N',
    'PB': 'F',
    'BK': 'P',
    'NV': 'V',
    'KF': 'C',
    'KS': 'C',
    'PV': 'N',
    'NF': 'S',
    'PK': 'F',
    'SC': 'F',
    'KN': 'K',
    'PN': 'K',
    'OH': 'F',
    'PS': 'P',
    'FN': 'O',
    'OP': 'B',
    'FO': 'C',
    'HS': 'F',
    'VO': 'C',
    'OS': 'B',
    'PF': 'V',
    'SB': 'V',
    'KO': 'O',
    'SK': 'N',
    'KB': 'F',
    'KH': 'C',
    'CC': 'B',
    'CS': 'C',
    'OF': 'C',
    'FS': 'B',
    'FP': 'H',
    'VN': 'O',
    'NB': 'N',
    'BS': 'H',
    'PC': 'H',
    'OO': 'F',
    'BF': 'O',
    'HC': 'P',
    'BH': 'S',
    'NP': 'P',
    'FB': 'C',
    'CB': 'H',
    'BO': 'C',
    'NN': 'V',
    'SF': 'N',
    'FC': 'F',
    'KK': 'C',
    'CN': 'N',
    'BV': 'F',
    'FK': 'C',
    'CF': 'F',
    'VV': 'B',
    'VF': 'S',
    'CK': 'C',
    'OV': 'P',
    'NC': 'N',
    'SS': 'F',
    'NK': 'V',
    'HN': 'O',
    'ON': 'P',
    'FH': 'O',
    'OB': 'H',
    'SH': 'H',
    'NH': 'V',
    'FF': 'B',
    'HP': 'B',
    'PO': 'P',
    'HB': 'H',
    'CH': 'N',
    'SN': 'P',
    'HK': 'P',
    'FV': 'H',
    'SO': 'O',
    'VH': 'V',
    'BP': 'V',
    'CV': 'P',
    'KP': 'K',
    'VB': 'N',
    'HV': 'K',
    'SP': 'N',
    'HO': 'P',
    'CP': 'H',
    'VC': 'N',
    'CO': 'S',
    'BN': 'H',
    'NO': 'B',
    'HF': 'O',
    'VP': 'K',
    'KV': 'H',
    'KC': 'F',
    'HH': 'C',
    'BB': 'K',
    'VK': 'P',
    'OK': 'C',
    'OC': 'C',
    'PH': 'H',
}

# An attempt to improve performance by mapping strings to ints (probably won't work ...)

num_to_string_map: dict[int, str] = {}

def map_string_to_nums(string: str, map: dict[int, str]):
    return [map_char_to_num(char, map) for char in string]

def map_nums_to_string(nums: list[int], map: dict[int, str]):
    return ''.join([map_num_to_char(num, map) for num in nums])

def map_dictionary_items_to_nums(dictionary: dict[str, str], map: dict[int, str]):
    result: dict[int, int] = {}
    for key, value in dictionary.items():
        result[combine_nums(map_string_to_nums(key, map))] = map_char_to_num(value, map)
    return result

def map_dictionary_items_to_strings(dictionary: dict[int, int], map: dict[int, str]):
    result: dict[str, str] = {}
    for key, value in dictionary.items():
        result[map_nums_to_string(split_num(key), map)] = map_num_to_char(value, map)
    return result

def map_char_to_num(char: str, map: dict[int, str]):
    if char in map.values():
        i = list(map.keys())[list(map.values()).index(char)]
    else:
        i = len(map.keys()) + 1
        map[i] = char
    return i

def map_num_to_char(num: int, map: dict[int, str]):
    return map[num]

def combine_nums(nums: list[int]):
    return int(''.join([str(num) for num in nums]))

def split_num(num: int):
    num_str = str(num)
    # TODO

##################
# Testing:

template_mapped = map_string_to_nums(input_template, num_to_string_map)
print(template_mapped)
print(map_nums_to_string(template_mapped, num_to_string_map))
rules_mapped = map_dictionary_items_to_nums(input_rules, num_to_string_map)
print(rules_mapped)
print(map_dictionary_items_to_strings(rules_mapped, num_to_string_map))

##################

def apply_rules(string: str):
    length = len(string)
    print('string length:', length)
    for i in range(1, length):
        pair_start = length - 1 - i # work backwards through the string
        pair = string[pair_start:pair_start + 2]
        insertion = input_rules[pair]
        if insertion:
            string = string[0:pair_start + 1] + insertion + string[pair_start + 1:]
    return string


string = input_template
for i in range(0, 40):
    print('iteration', i + 1)
    string = apply_rules(string)

histogram = {}
for i in range(0, len(string)):
    char = string[i]
    if not histogram.get(char):
        histogram[char] = 0
    histogram[char] += 1

print(max(histogram.values()) - min(histogram.values()))
