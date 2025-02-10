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

# are the list comprehensions making the correct lists?

def test_duplicate_rows():
    O = {"": [True, False, True], "a": [True, True, False], "b": [True, True, False]}
    S = ["", "a", "b"]
    assert find_duplicate_rows(O, S) == [['a', 'b']]
    O = {"": [True, False, True], "a": [True, True, False], "b": [True, True, False], "aa": [True, True, False]}
    S = ["", "a", "b", "aa"]
    assert find_duplicate_rows(O, S) == [['a', 'b', 'aa']]
    O = {"": [True, False, True], "a": [True, True, False], "b": [True, True, False], "aa": [True, False, False], "ab": [True, False, True]}
    S = ["", "a", "b", "aa", "ab"]
    assert find_duplicate_rows(O, S) == [['', 'ab'], ['a', 'b']]

if __name__ == '__main__':
    test_list_equality()
    test_prefix_concat_alphabet()
    test_all_prefixes_of_str()
    test_duplicate_rows()
    print('All tests passed!')
