from l_star import alphabet
from automathon import DFA as DFA_VISUALIZATION
from graphviz import ExecutableNotFound

class DeterministicFiniteAutomaton:
    def __init__(self, starting_state: str):
        self.states: set = set()
        self.transitions: dict[str: dict[str: str]] = {}
        self.start_state: str = starting_state
        self.accepting_states: set = set()
        self.regex = None

    def add_state(self, state: str, accepting=False) -> None:
        self.states.add(state)
        if accepting:
            self.accepting_states.add(state)

    def add_transition(self, src, symbol, dest) -> None:
        if src not in self.transitions:
            self.transitions[src] = {}
        self.transitions[src][symbol] = dest

    def view(self) -> None:
        automata = DFA_VISUALIZATION(self.states, alphabet, self.transitions, self.start_state, self.accepting_states)
        try:
            automata.view("DFA")
        except ExecutableNotFound:
            print("Please install graphviz and add it to your PATH to visualize the DFA")
