from l_star.pattern import generate_regex
from l_star.dfa import DeterministicFiniteAutomaton

def test_generate_regex():
    dfa = DeterministicFiniteAutomaton('q0')
    dfa.add_state('q0')
    dfa.add_state('q1')
    dfa.add_state('q2', accepting=True)
    dfa.add_state('q3')
    dfa.add_transition('q0', 'a', 'q1')
    dfa.add_transition('q0', 'b', 'q1')
    dfa.add_transition('q1', 'a', 'q2')
    dfa.add_transition('q1', 'b', 'q3')
    dfa.add_transition('q2', 'a', 'q2')
    dfa.add_transition('q2', 'b', 'q2')
    dfa.add_transition('q3', 'a', 'q3')
    dfa.add_transition('q3', 'b', 'q3')

    regex = generate_regex(dfa)
    assert str(regex) == '.a.*'