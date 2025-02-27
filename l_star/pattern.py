from l_star import alphabet
from l_star.dfa import DeterministicFiniteAutomaton


class Pattern:
    def __init__(self, symbol: str = None, members: list['Pattern'] = None):
        if symbol and members:
            raise ValueError("Pattern must be either a symbol or a list of members")
        self.symbol = symbol
        self.members = members

    def __str__(self):
        raise NotImplementedError("Should be implemented by child")

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
    def empty_string():
        return Symbol('ε')

    @staticmethod
    def empty_lang():
        return Symbol('∅')

    @staticmethod
    def any_symbol():
        return Symbol('.')

def generate_regex(dfa: DeterministicFiniteAutomaton) -> Pattern:
    # Create new start and accept states.
    new_start = "new_start"
    new_accept = "new_accept"

    # Combine original states with the new ones.
    states = set(dfa.states)
    states.add(new_start)
    states.add(new_accept)

    # Initialize a dictionary of dictionaries holding Regex objects.
    adj_m = {from_state: {to_state: Symbol.empty_lang() for to_state in states} for from_state in states}

    # Set labels for each transition in the DFA.
    for src in dfa.transitions:
        for symbol, dst in dfa.transitions[src].items():
            adj_m[src][dst] |= Symbol(symbol)

    # Add an ε-transition from the new start to the original start.
    adj_m[new_start][dfa.start_state] = Symbol.empty_string()

    # For every accepting state, add an ε-transition to the new accept state.
    for a_state in dfa.accepting_states:
        adj_m[a_state][new_accept] = Symbol.empty_string()


    # Eliminate states one by one, except new_start and new_accept.
    # the states to consider/update are new_start + new_accept + all non_eliminated states
    for r in dfa.states:
        states.remove(r)
        for i in states: # for every state going to r
            # what are all the ways that I can go to r?
            # adj_m[i][r] already took care of that expression
            for j in states: # for every state leaving r
                # Update rule: adj_m[i][j] = adj_m[i][j] ∪ (adj_m[i][r] · (adj_m[r][r])^* · adj_m[r][j])
                # the deletion of r will lead to more paths from i to j
                print(f"Considering {i} -> {r} -> {j}: {adj_m[i][j]}")
                new_expr = adj_m[i][r]

                if adj_m[r][r].symbol != '∅':
                    new_expr += adj_m[r][r].star()
                new_expr += adj_m[r][j]

                adj_m[i][j] |= new_expr
                print(f"{adj_m[i][r]} + ({adj_m[r][r].star()} + {adj_m[r][j]}) = {new_expr}")
                print(f"Updating {i} -> {j} to {adj_m[i][j]}")
        print_adj_m(adj_m, states)
    # The regular expression for the language is the one from new_start to new_accept.
    return adj_m[new_start][new_accept]

# make a print adj matrix function
def print_adj_m(adj_m, states):
    print("----------------------------------------")
    for src in states:
        print(f"From {src}:")
        for dest in adj_m[src]:
            print(f"    -> {dest}: {adj_m[src][dest]}")