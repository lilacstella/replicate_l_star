from l_star import alphabet, S, E, teacher
from l_star.util import all_prefixes_of_str, prefix_concat_alphabet, find_duplicate_rows
from l_star.observation_table import ObservationTable

def l_star():
    observation_table = ObservationTable()

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

        # present to the teacher
        done, counter_example = teacher.is_equivalent(observation_table)
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


if __name__ == '__main__':
    l_star()
