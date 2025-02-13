from l_star import alphabet
from automathon import DFA as DFA_VISUALIZATION

class DeterministicFiniteAutomaton:
    def __init__(self, starting_state):
        self.states = set()
        self.transitions = {}
        self.start_state = starting_state
        self.accepting_states = set()

    def add_state(self, state: str, accepting=False):
        self.states.add(state)
        if accepting:
            self.accepting_states.add(state)

    def add_transition(self, state, symbol, next_state):
        if state not in self.transitions:
            self.transitions[state] = {}
        self.transitions[state][symbol] = next_state

    def view(self):
        automata = DFA_VISUALIZATION(self.states, alphabet, self.transitions, self.start_state, self.accepting_states)
        automata.view("dfa")