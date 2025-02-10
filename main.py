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
    # populate table with first column
    O[''] = [teacher.is_member('')]
    for a in alphabet:
        O[a] = [teacher.is_member(a)]

    done = False
    while not done:
        # is it closed?
        if not closed(O, S):
            # adding things to S has side effects
            # it will make S•Σ larger too..
            # how do I know which ones are new and need to be updated?
            continue

        # is it consistent?
        if not consistent():
            continue
        # present to the teacher
        done, counter_example = teacher.is_equivalent(O)
        if done:
            break
        # add counter example to the table
        new_prefices = [i for i in all_prefixes_of_str(counter_example) if i not in S]
        for i in new_prefices:
            # how do I stop asking the same question?
            O[i] = [teacher.is_member(i + e) for e in E]

def closed(O, S):
    for i in prefix_concat_alphabet(S):
        # is there a row in the S section that is equivalent to curr in S•Σ?
        if not any(O[i] == O[s] for s in S):
            # no matches -> add the current i to S
            S.append(i)
            return False
    return True

    # present to the teacher

    # exit

if __name__ == '__main__':
    main()