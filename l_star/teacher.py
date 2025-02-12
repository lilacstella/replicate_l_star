class Teacher:

    def __init__(self):
        self.memory = {}

    def is_member(self, q):
        if q in self.memory:
            return self.memory[q]
        a = input(f'Is "{q}" in the language?')
        is_member = True if a == 'y' else False

        self.memory[q] = is_member
        return is_member

    def is_equivalent(self, grammar):
        print(grammar)
        a = input('Is the grammar correct?')
        if a == 'y':
            return True, None
        return False, input('What is a counter example? ')
