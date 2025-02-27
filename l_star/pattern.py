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

    def __or__(self, other):
        if self.symbol == '∅':
            return other
        if other.symbol == '∅':
            return self

        if self.symbol == 'ε' and other.symbol == 'ε':
            return Symbol.empty_string()

        # if the members consists of the entire alphabet, return any symbol
        if (isinstance(self, Symbol) and self.symbol == '.') or (isinstance(other, Symbol) and other.symbol == '.'):
            return Symbol.any_symbol()

        union = Union(self, other)

        # check if member of this union consists of the entire alphabet
        if all(isinstance(member, Symbol) for member in union.members) and \
            set(member.symbol for member in union.members) == alphabet:
            return Symbol.any_symbol()

        return union

    def __add__(self, other):
        if self.symbol == '∅' or other.symbol == '∅':
            return Symbol.empty_lang()

        if isinstance(self, Star) and isinstance(other, Symbol):
            if self.members[0].symbol == other.symbol:
                return self
        if isinstance(other, Star) and isinstance(self, Symbol):
            if other.members[0].symbol == self.symbol:
                return other

        return Concatenation(self, other)

    def star(self):
        if self.symbol == '∅':
            return Symbol.empty_lang()
        return Star(self)

class Union(Pattern):
    def __init__(self, first: Pattern, second: Pattern):
        if isinstance(first, Union):
            members = first.members
        else:
            members = [first]

        if isinstance(second, Union):
            members.extend(second.members)
        else:
            members.append(second)

        # members should be unique
        members = list(set(members))
        super().__init__(members=members)

    def __str__(self):
        # I am trying to make quesiton mark if one of them is epsilon
        if len(self.members) == 2:
            if self.members[0].symbol == 'ε':
                if isinstance(self.members[1], Symbol):
                    return f"{self.members[1]}?"
                return f"({self.members[1]})?"
            if self.members[1].symbol == 'ε':
                if isinstance(self.members[0], Symbol):
                    return f"{self.members[0]}?"
                return f"({self.members[0]})?"
        return f"({'|'.join(str(member) for member in self.members)})"

class Concatenation(Pattern):
    def __init__(self, first: Pattern, second: Pattern):
        if isinstance(first, Concatenation):
            first = first.members
        else:
            first = [first]

        if isinstance(second, Concatenation):
            second = second.members
        else:
            second = [second]

        super().__init__(members=first + second)

    def __str__(self):
        # keep all non-ε
        self.members = [member for member in self.members if member.symbol != 'ε']

        return ''.join(str(member) for member in self.members)

class Star(Pattern):
    def __init__(self, first: Pattern):
        super().__init__(members=[first])

    def __str__(self):
        if isinstance(self.members[0], Symbol) or str(self.members[0])[-1] == ')':
            return f"{self.members[0]}*"
        return f"({self.members[0]})*"

class Symbol(Pattern):
    def __init__(self, symbol: str):
        super().__init__(symbol=symbol)

    def __str__(self):
        return self.symbol

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