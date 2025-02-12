from l_star import alphabet, teacher, S, E
from l_star.util import prefix_concat_alphabet

class ObservationTable:
    def __init__(self):
        self.O: dict = {}  # observation table

    def construct_table(self):
        # the S section
        for s in S:
            self.O[s] = [teacher.is_member(s + e) for e in E]
        # we should also generate all of S•Σ
        for i in prefix_concat_alphabet(alphabet, S):
            self.O[i] = [teacher.is_member(i + e) for e in E]

    def __getitem__(self, key):
        if key not in self.O:
            self.O[key] = [teacher.is_member(key + e) for e in E]
        return self.O[key]

    # def convert_to_dfa(self):
    #     states_names = {chr(ord('A') + i): state for i, state in enumerate({self.O[s] for s in S})}
    #     print(states_names)
    #     starting_state = self.O['']
    #     # accept states that have a 1 to start in their row value

    def convert_to_dfa(self):
        # https://rahul.gopinath.org/post/2024/01/04/lstar-learning-regular-languages/#convert-table-to-grammar
        # Step 1: identify all distinguished states.
        prefix_to_state = {}  # Mapping from row string to state ID
        states = {}
        grammar = {}
        for s in S:
            state_name = f'{self.O[s]}'
            if state_name not in states: states[state_name] = []
            states[state_name].append(s)
            prefix_to_state[s] = state_name

        for state_name in states: grammar[state_name] = []

        # Step 2: Identify the start state, which corresponds to epsilon row
        start_nt = prefix_to_state['']

        # Step 3: Identify the accepting states
        accepting = [prefix_to_state[s] for s in S if self.O[s][0] == 1]
        if not accepting: return {'<start>': []}, '<start>'
        for s in accepting: grammar[s] = [['<_>']]
        grammar['<_>'] = [[]]

        # Step 4: Create the transition function
        for sid1 in states:
            first_such_row = states[sid1][0]
            for a in alphabet:
                sid2 = f'{self.O[first_such_row + a]}'
                grammar[sid1].append([a, sid2])

        return grammar, start_nt


    def __str__(self):
        return str(self.O)
