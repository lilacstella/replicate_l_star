from teacher import Teacher

alphabet = list('ab')

def prefix_concat_alphabet(S): # S•Σ
    return [s + a for s in S for a in alphabet if s + a not in S]

def all_prefixes_of_str(str):
    return [str[:i] for i in range(len(str) + 1)]

def find_duplicate_rows(O, S):
    seen = {}
    duplicates = []

    for s in S:
        row = tuple(O[s])
        if row in seen:
            seen[row].append(s)
        else:
            seen[row] = [s]

    for rows in seen.values():
        if len(rows) > 1:
            duplicates.append(rows)

    return duplicates

def main():
    # we have an observation table O
    # it has a rows and columns
    # going to represent each row as an array
    # with indices corresponding to E
    O: dict = {}  # observation table
    S: list = ['']  # prefixes (rows)
    E: list = ['']  # postfixes (columns)
    teacher = Teacher()

    done = False
    while not done:
        # reset table every loop
        for s in S:
            O[s] = [teacher.is_member(s + e) for e in E]

        # is it closed?
        is_closed, new_prefix = closed(O, S)
        if not is_closed:
            # closed no longer has side effects
            S.append(new_prefix)
            # it will make S•Σ larger too...
            # how do I know which ones are new and need to be updated?
            # check for not filled in entries in the table at the start
            # just simply completely make the new entries of the O
            continue

        # is it consistent?
        is_consistent, new_extension = consistent(O, S, E)
        if not is_consistent:
            E.append(new_extension)
            continue

        # present to the teacher
        done, counter_example = teacher.is_equivalent(O)
        if done:
            break

        # add counter example to the table
        new_prefixes = [i for i in all_prefixes_of_str(counter_example) if i not in S]
        for i in new_prefixes:
            if i not in S:
                S.append(i)

def closed(O, S):
    for i in prefix_concat_alphabet(S):
        # is there a row in the S section that is equivalent to curr in S•Σ?
        if not any(O[i] == O[s] for s in S):
            # no matches -> add the current i to S
            S.append(i)
            return False
    return True

def consistent(O, S):
    # for every type or row value in S section of O
    # do they go to the same row type if the next character is
    # every character in the alphabet?
    for matching_row_s in find_duplicate_rows(O, S):
        # do all s in matching_row_s go to the same place?
        # len(matching_row_s) >= 2
        # matching_row_s looks like ['a', 'b'], keys s in S that have the same row values
        for a in alphabet:
            for s in matching_row_s[1:]:
                # can we make the assumption that this is already filled?
                if O[matching_row_s[0] + a] != O[s + a]:
                    # need to figure out what to add to E
                    return False


if __name__ == '__main__':
    main()