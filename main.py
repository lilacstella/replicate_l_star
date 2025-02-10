def is_member(q):
    print(q)
    a = input(f'Is "{q}" in the language?')
    return True if a == 'y' else False

def is_equivalent(grammar):
    print(grammar)
    a = input('Is the grammar correct?')
    return a == 'y', []

def s_concat_alphabet(S, alphabet):
    return [s + a for s in S for a in alphabet if s + a not in S]

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