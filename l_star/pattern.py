from l_star.dfa import DeterministicFiniteAutomaton
from l_star import alphabet

def strip_parenthesis(s: str) -> str:
    if s.startswith("(") and s.endswith(")"):
        return s[1:-1]
    return s

class Pattern:
    def __init__(self, pattern: str):
        if len(pattern) > 1:
            self.pattern = f"({pattern})"
        else:
            self.pattern = pattern

    def __str__(self):
        return self.pattern

    def __eq__(self, other):
        return isinstance(other, Pattern) and self.pattern == other.pattern

    def __or__(self, other: 'Pattern') -> 'Pattern':
        # Union: if one side is the empty set, return the other.
        if self.pattern == "∅":
            return other
        if other.pattern == "∅":
            return self
        if self.pattern == other.pattern:
            return self
        # check if this pattern is somehow an or of all characters in the alphabet
        print(set(strip_parenthesis(self.pattern).split("|")))
        if set(strip_parenthesis(self.pattern).split("|")) == alphabet:
            return Pattern.dot()

        return Pattern(f"{self.pattern}|{other.pattern}")

    def __add__(self, other: 'Pattern') -> 'Pattern':
        # Concatenation: if either is ∅, then the result is ∅.
        if self.pattern == "∅" or other.pattern == "∅":
            return Pattern("∅")
        # ε acts as the identity for concatenation.
        if self.pattern == "ε":
            return other
        if other.pattern == "ε":
            return self
        return Pattern(f"{self.pattern}{other.pattern}")

    def star(self) -> 'Pattern':
        # The Kleene star of ∅ or ε is ε.
        if self.pattern in ["∅", "ε"]:
            return Pattern("ε")
        if self.pattern.endswith("*"):
            return self
        if len(self.pattern) == 1:
            return Pattern(f"{self.pattern}*")

        return Pattern(f"({strip_parenthesis(self.pattern)})*")

    @staticmethod
    def empty_lang() -> 'Pattern':
        return Pattern("∅")

    @staticmethod
    def empty_str() -> 'Pattern':
        return Pattern("ε")

    @staticmethod
    def dot() -> 'Pattern':
        return Pattern(".")

def generate_regex(dfa: DeterministicFiniteAutomaton) -> Pattern:
    # Create new start and accept states.
    new_start = "new_start"
    new_accept = "new_accept"

    # Combine original states with the new ones.
    states = set(dfa.states)
    states.add(new_start)
    states.add(new_accept)

    # Initialize a dictionary of dictionaries holding Regex objects.
    R = {state: {state2: Pattern.empty_lang() for state2 in states} for state in states}

    # Set labels for each transition in the DFA.
    for src in dfa.transitions:
        for symbol, dst in dfa.transitions[src].items():
            R[src][dst] = R[src][dst] | Pattern(symbol)

    # Add an ε-transition from the new start to the original start.
    R[new_start][dfa.start_state] = R[new_start][dfa.start_state] | Pattern.empty_str()

    # For every accepting state, add an ε-transition to the new accept state.
    for a_state in dfa.accepting_states:
        R[a_state][new_accept] = R[a_state][new_accept] | Pattern.empty_str()

    # Eliminate states one by one, except new_start and new_accept.
    elimination_states = states - {new_start, new_accept}
    for r in list(elimination_states):
        for i in states:
            for j in states:
                # Update rule: R[i][j] = R[i][j] ∪ (R[i][r] · (R[r][r])^* · R[r][j])
                new_expr = R[i][r] + (R[r][r].star() + R[r][j])
                # Note: Because our operators are overloaded, the above expression concatenates as intended.
                R[i][j] = R[i][j] | new_expr
        # "Remove" state r by nullifying its transitions.
        for i in states:
            R[i][r] = Pattern.empty_lang()
        for j in states:
            R[r][j] = Pattern.empty_lang()
        states.remove(r)

    # The regular expression for the language is the one from new_start to new_accept.
    return R[new_start][new_accept]



# # Define a sample DFA.
# dfa = DeterministicFiniteAutomaton(starting_state="q0")
# dfa.states = {"q0", "q1", "q2"}
# dfa.accepting_states = {"q2"}
# dfa.transitions = {
#     "q0": {"a": "q1", "b": "q0"},
#     "q1": {"a": "q2", "b": "q0"},
#     "q2": {"a": "q2", "b": "q2"}
# }
#
# # Convert the DFA to a regular expression.
# regex = dfa_to_regex_state_elimination(dfa)
# print("Regular expression for the DFA:", regex)
