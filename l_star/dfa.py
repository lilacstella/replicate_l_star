from l_star import alphabet
from automathon import DFA as DFA_VISUALIZATION

class DeterministicFiniteAutomaton:
    def __init__(self, starting_state):
        self.states: set = set()
        self.transitions: dict[str: dict[str: str]] = {}
        self.start_state: str = starting_state
        self.accepting_states: set = set()
        self.regex = None

    def add_state(self, state: str, accepting=False):
        self.states.add(state)
        if accepting:
            self.accepting_states.add(state)

    def add_transition(self, src, symbol, dest):
        if src not in self.transitions:
            self.transitions[src] = {}
        self.transitions[src][symbol] = dest

    def view(self):
        automata = DFA_VISUALIZATION(self.states, alphabet, self.transitions, self.start_state, self.accepting_states)
        automata.view("DFA")
