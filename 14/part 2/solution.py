input_template = 'FNFPPNKPPHSOKFFHOFOC'
input_rules: dict[str, str] = {
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


def fill_counts_dict(strings, counts: dict):
    for string in strings:
        increase_count(string, counts, 1)


def increase_count(string: str, counts: dict, amount: int):
    if string in counts.keys():
        counts[string] += amount
    else:
        counts[string] = amount


def decrease_count(string: str, counts: dict, amount: int):
    if string in counts.keys():
        counts[string] -= amount


def apply_rules(letter_counts: dict[str, int], pair_counts: dict[str, int]):
    letter_counts_copy = letter_counts.copy()
    pair_counts_copy = pair_counts.copy()
    for pair, pair_count in pair_counts.items():
        insertion_letter = input_rules[pair]
        if insertion_letter:
            increase_count(insertion_letter, letter_counts_copy, pair_count)
            increase_count(pair[0] + insertion_letter, pair_counts_copy, pair_count)
            increase_count(insertion_letter + pair[1], pair_counts_copy, pair_count)
            decrease_count(pair, pair_counts_copy, pair_count)
    return letter_counts_copy, pair_counts_copy


def solve():
    letter_counts: dict[str, int] = {}
    pair_counts: dict[str, int] = {}

    fill_counts_dict(input_template, letter_counts)
    fill_counts_dict([input_template[i:i + 2] for i in range(0, len(input_template) - 1)], pair_counts)

    for i in range(0, 40):
        letter_counts, pair_counts = apply_rules(letter_counts, pair_counts)

    return max(letter_counts.values()) - min(letter_counts.values())


print(solve())
