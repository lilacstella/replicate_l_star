from l_star import alphabet, S, E, teacher
from l_star.util import all_prefixes_of_str, prefix_concat_alphabet, find_duplicate_rows
from l_star.observation_table import ObservationTable

def l_star():
    observation_table = ObservationTable() # <- TODO can we not regenerate the whole table every time

    done = False
    while not done:
        observation_table.construct_table()

        # is it closed?
        is_closed, new_prefix = closed(observation_table, S)
        if not is_closed:
            S.append(new_prefix)
            continue

        # is it consistent?
        is_consistent, new_extension = consistent(observation_table, S)
        if not is_consistent:
            E.append(new_extension)
            continue

        print(observation_table)
        # present to the teacher
        dfa = observation_table.create_dfa()
        done, counter_example = teacher.is_equivalent(dfa)
        if done:
            break

        # add counter example to the table
        new_prefixes = [i for i in all_prefixes_of_str(counter_example) if i not in S]
        for i in new_prefixes:
            if i not in S:
                S.append(i)

def closed(O, S):
    for i in prefix_concat_alphabet(alphabet, S):
        # is there a row in the S section that is equivalent to curr in S•Σ?
        if not any(O[i] == O[s] for s in S):
            # no matches -> add the current i to S
            return False, i
    return True, None

def consistent(O, S):
    # for every type or row value in S section of O
    # do they go to the same row type if the next character is
    # every character in the alphabet?
    # TODO can these things be generators?
    for matching_row_s in find_duplicate_rows(O, S):
        # do all s in matching_row_s go to the same place?
        # len(matching_row_s) >= 2
        # matching_row_s looks like ['a', 'b'], keys s in S that have the same row values
        # as of rn, they are completely matching,
        # we're going to check if that continues to be the case with concat + a in alphabet
        x = matching_row_s[0]
        for y in matching_row_s[1:]:
            for a in alphabet:
                if O[x + a] == O[y + a]:
                    continue
                # need to figure out what to add to E
                for i, boolean_pair in enumerate(zip(O[x + a], O[y + a])):
                    if boolean_pair[0] != boolean_pair[1]:
                        return False, a + E[i]
                raise ValueError(f"States {x} and {y} reached here with {a}")
    return True, None

if __name__ == '__main__':
    l_star()
