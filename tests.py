from l_star import alphabet
from l_star.observation_table import ObservationTable
from l_star.util import prefix_concat_alphabet, all_prefixes_of_str, find_duplicate_rows


def test_list_equality():
    # different rows on the table can be directly compared
    assert [True, True, False] == [True, True, False]
    assert [True, True, False] != [True, True, True]
    assert [True, False] != [True, True, True]

def test_prefix_concat_alphabet():
    assert prefix_concat_alphabet(alphabet, ['a', 'b']) == ['aa', 'ab', 'ba', 'bb']
    assert prefix_concat_alphabet(alphabet, ['aa', 'ab', 'ba', 'bb']) == ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

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

def test_zip():
    O = ObservationTable()
    O.O = {"": [True, False, True], "a": [True, True, False], "b": [True, True, False], "aa": [True, True, False]}
    global S
    S = ["", "a", "b", "aa"]
    global E
    E = ['', 'a', 'b']
    from l_star import teacher
    global teacher
    teacher.memory = {"ba": True, "aaa": False, "ab": False, "bb": False, "aab": False}
    matching_row_s = find_duplicate_rows(O, S)[0]
    print(matching_row_s)
    for a in ['a', 'b']:
        for s in matching_row_s[1:]:
            print(a)
            print(s)
            print(O[matching_row_s[0] + a])
            print(O[s + a])
            # some weird things are happening out here outside of the package itself...
            # definitely using these in ways that they were not meant to
            # made it difficult for myself to write unit tests
            for one, two in zip(O[matching_row_s[0] + a], O[s + a]):
                print(one, two)

def run_tests():
    test_list_equality()
    test_prefix_concat_alphabet()
    test_all_prefixes_of_str()
    test_duplicate_rows()
    test_zip()
    print('All tests passed!')

if __name__ == '__main__':
    run_tests()