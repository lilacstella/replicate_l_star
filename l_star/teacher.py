from l_star.pattern import generate_regex
from l_star import alphabet

class Teacher:

    def __init__(self):
        self.memory = {}

    def is_member(self, q):
        if q in self.memory:
            return self.memory[q]
        a = input(f'Is "{q}" in the language?')
        is_member = True if 'y' in a else False

        self.memory[q] = is_member
        return is_member

    @staticmethod
    def is_equivalent(dfa):
        regex = generate_regex(dfa)
        dfa.view()
        a = input(f'Is this regex {regex} correct?')
        if 'y' in a:
            return True, None

        while True:
            counter_example = input('What is a counter example?')
            if all(c in alphabet for c in counter_example):
                break
            print('Counter example must be in the alphabet')

        return False, counter_example
