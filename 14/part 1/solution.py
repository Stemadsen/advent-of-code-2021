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

def apply_rules(string: str):
    length = len(string)
    for i in range(1, length):
        pair_start = length - 1 - i # work backwards through the string
        pair = string[pair_start:pair_start + 2]
        # print('pair:', pair)
        insertion = input_rules[pair]
        if insertion:
            # print('inserting', insertion)
            new_pair = pair[0] + insertion + pair[1]
            # print('new pair:', new_pair)
            string = string[0:pair_start + 1] + insertion + string[pair_start + 1:]
            # print('new string:', string)
    return string


string = input_template
for i in range(0, 10):
    string = apply_rules(string)

histogram = {}
for i in range(0, len(string)):
    char = string[i]
    if not histogram.get(char):
        histogram[char] = 0
    histogram[char] += 1

print(histogram)

most_occurrences = 0
fewest_occurrences = 0
for occurrences in histogram.values():
    if occurrences > most_occurrences:
        most_occurrences = occurrences
    if occurrences < fewest_occurrences or not fewest_occurrences:
        fewest_occurrences = occurrences

print(most_occurrences - fewest_occurrences)
