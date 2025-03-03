from l_star.pattern import generate_regex
from l_star import alphabet

class Teacher:

    def __init__(self):
        self.memory = {}

    def is_member(self, q):
        if q in self.memory:
            return self.memory[q]
        human = True
        if human:
            a = input(f'Is "{q}" in the language?')
            is_member = True if 'y' in a else False
        else:
            is_member = self.correctness_agent(q)
        self.memory[q] = is_member
        return is_member

    @staticmethod
    def is_equivalent(dfa):
        dfa.view()
        regex = generate_regex(dfa)
        a = input(f'Is this regex {regex} correct?')
        if 'y' in a:
            return True, None

        while True:
            counter_example = input('What is a counter example?')
            if all(c in alphabet for c in counter_example):
                break
            print('Counter example must be in the alphabet')

        return False, counter_example

    @staticmethod
    def correctness_agent(q):
        # if len(q) >= 2 and q[1] == 'a':
        #     return True
        if 'a' in q and 'b' in q:
            return True
        return False