class WordFilter:

    def __init__(self, words):
        self.lookup = {}

        for i, word in enumerate(words):
            for p in range(len(word) + 1):
                prefix = word[:p]

                for s in range(len(word) + 1):
                    suffix = word[len(word)-s:]
                    self.lookup[(prefix, suffix)] = i

    def f(self, pref, suff):
        return self.lookup.get((pref, suff), -1)


wf = WordFilter(["apple"])

print(wf.f("a", "e"))