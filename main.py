from teacher import Teacher

alphabet = list('ab')

def prefix_concat_alphabet(S): # S•Σ
    return [s + a for s in S for a in alphabet if s + a not in S]

def all_prefixes_of_str(str):
    return [str[:i] for i in range(len(str) + 1)]

def find_duplicate_rows(O, S):
    seen = {}
    duplicates = []

    for s in S:
        row = tuple(O[s])
        if row in seen:
            seen[row].append(s)
        else:
            seen[row] = [s]

    for rows in seen.values():
        if len(rows) > 1:
            duplicates.append(rows)

    return duplicates

def main():
    # we have an observation table O
    # it has a rows and columns
    # going to represent each row as an array
    # with indices corresponding to E
    O: dict = {}
    alphabet = list('ab')
    S: list = ['']
    E: list = ['']

    # populate table
    O[''] = [is_member('')]
    for a in alphabet:
        O[a] = [is_member(a)]

    print(s_concat_alphabet(S, alphabet))
    # is it closed?
    for i in s_concat_alphabet(S, alphabet):
        O[i] = [is_member(i)]
    # is it consistent?

    # present to the teacher

    # exit

if __name__ == '__main__':
    main()