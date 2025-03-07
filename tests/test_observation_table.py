from l_star.observation_table import ObservationTable
from l_star.dfa import DeterministicFiniteAutomaton
from l_star import S, E, alphabet
from l_star.util import prefix_concat_alphabet, represent_state_in_bin

def test_construct_table(mocker):
    mock_is_member = mocker.patch('l_star.teacher.Teacher.is_member')
    mock_is_member.side_effect = lambda x: x in ['a', 'b', 'c']
    table = ObservationTable()
    table.construct_table()
    for s in S:
        assert s in table.O
        assert len(table.O[s]) == len(E)
    for i in prefix_concat_alphabet(alphabet, S):
        assert i in table.O
        assert len(table.O[i]) == len(E)

def test_getitem(mocker):
    mock_is_member = mocker.patch('l_star.teacher.Teacher.is_member')
    mock_is_member.side_effect = lambda x: x in ['a', 'b', 'c']
    table = ObservationTable()
    key = 'some_key'
    result = table[key]
    assert key in table.O
    assert result == table.O[key]

def test_create_dfa(mocker):
    mock_is_member = mocker.patch('l_star.teacher.Teacher.is_member')
    mock_is_member.side_effect = lambda x: x in ['a', 'b', 'c']
    table = ObservationTable()
    table.construct_table()
    dfa = table.create_dfa()
    assert isinstance(dfa, DeterministicFiniteAutomaton)
    assert dfa.start_state == represent_state_in_bin(table.O[''])
    for s in S:
        state_bin = represent_state_in_bin(table.O[s])
        assert state_bin in dfa.states
        for a in alphabet:
            transition_state = represent_state_in_bin(table.O[s + a])
            assert dfa.transitions[state_bin][a] == transition_state

def test_str(mocker):
    mock_is_member = mocker.patch('l_star.teacher.Teacher.is_member')
    mock_is_member.side_effect = lambda x: x in ['a', 'b', 'c']
    table = ObservationTable()
    table.construct_table()
    table_str = str(table)
    assert isinstance(table_str, str)
    assert table_str == str(table.O)