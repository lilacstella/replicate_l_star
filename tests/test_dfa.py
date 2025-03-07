import pytest
from l_star.dfa import DeterministicFiniteAutomaton

def test_add_state():
    dfa = DeterministicFiniteAutomaton(starting_state='q0')
    dfa.add_state('q1')
    assert 'q1' in dfa.states

def test_add_accepting_state():
    dfa = DeterministicFiniteAutomaton(starting_state='q0')
    dfa.add_state('q1', accepting=True)
    assert 'q1' in dfa.accepting_states

def test_add_transition():
    dfa = DeterministicFiniteAutomaton(starting_state='q0')
    dfa.add_state('q1')
    dfa.add_transition('q0', 'a', 'q1')
    assert dfa.transitions['q0']['a'] == 'q1'

def test_starting_state():
    dfa = DeterministicFiniteAutomaton(starting_state='q0')
    assert dfa.start_state == 'q0'

def test_view():
    dfa = DeterministicFiniteAutomaton(starting_state='q0')
    dfa.add_state('q1', accepting=True)
    dfa.add_transition('q0', 'a', 'q1')
    dfa.view()  # This should generate a visualization file without errors