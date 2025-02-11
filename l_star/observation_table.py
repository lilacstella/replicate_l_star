from l_star import alphabet, teacher, S, E
from l_star.util import prefix_concat_alphabet

class ObservationTable:
    def __init__(self):
        self.O: dict = {}  # observation table

    def construct_table(self):
        # the S section
        for s in S:
            self.O[s] = [teacher.is_member(s + e) for e in E]
        # we should also generate all of S•Σ
        for i in prefix_concat_alphabet(alphabet, S):
            self.O[i] = [teacher.is_member(i + e) for e in E]

    def __getitem__(self, key):
        if key not in self.O:
            self.O[key] = [teacher.is_member(key + e) for e in E]
        return self.O[key]

