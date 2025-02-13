def prefix_concat_alphabet(alphabet: list, S: list): # S•Σ
    return [s + a for s in S for a in alphabet if s + a not in S]

def all_prefixes_of_str(counter_example: str):
    return [counter_example[:i] for i in range(len(counter_example) + 1)]

def find_duplicate_rows(O: 'ObservationTable', S: list):
    seen = {}
    duplicates = []

    for s in S:
        row = tuple(O[s]) # make hashable
        if row in seen:
            seen[row].append(s)
        else:
            seen[row] = [s]

    for rows in seen.values():
        if len(rows) > 1:
            duplicates.append(rows)

    return duplicates

def represent_state_in_bin(state: list):
    return ''.join(['1' if i else '0' for i in state])