from main import *

def test_list_equality():
    # different rows on the table can be directly compared
    assert [True, True, False] == [True, True, False]
    assert [True, True, False] != [True, True, True]
    assert [True, False] != [True, True, True]

def test_prefix_concat_alphabet():
    assert prefix_concat_alphabet(['a', 'b']) == ['aa', 'ab', 'ba', 'bb']
    assert prefix_concat_alphabet(['aa', 'ab', 'ba', 'bb']) == ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

def test_all_prefixes_of_str():
    assert all_prefixes_of_str('abc') == ['', 'a', 'ab', 'abc']
    assert all_prefixes_of_str('abcd') == ['', 'a', 'ab', 'abc', 'abcd']

