def is_member(q):
    print(q)
    a = input(f'Is {q} in the language?')
    return 1 if a == 'y' else 0

def is_equivalent(self, grammar):
    print(grammar)
    a = input('Is the grammar correct?')
    return a == 'y', []

def s_concat_alphabet(S, alphabet):
    output = []
    for s in S:
        for a in alphabet:
            if s + a not in S:
                output.append(s + a)
    return output

def main():
    # we have an observation table O
    O: dict = {}
    alphabet = list('ab')
    S: list = ['']
    E: list = ['']
    # is it closed?
    print(s_concat_alphabet(S, alphabet))
    # for s in s_concat_alphabet(S, alphabet):

    # is it consistent?

    # present to the teacher

    # exit

if __name__ == '__main__':
    main()