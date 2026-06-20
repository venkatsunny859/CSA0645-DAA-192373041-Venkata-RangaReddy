# EXP59.py - WordFilter: Prefix and Suffix Search

class WordFilter:
    def __init__(self, words):
        self.words = words
    
    def f(self, pref, suff):
        """Find index of word with prefix and suffix, return largest index"""
        for i in range(len(self.words) - 1, -1, -1):
            word = self.words[i]
            if word.startswith(pref) and word.endswith(suff):
                return i
        return -1

print("=" * 60)
print("WordFilter - Prefix and Suffix Search")
print()

print("Test Case 1:")
words1 = ["apple"]
wf1 = WordFilter(words1)
result1 = wf1.f("a", "e")
print(f"Input: WordFilter([{words1}])")
print(f"Query: f(\"a\", \"e\")")
print(f"Output: {result1}")
print(f"Explanation: Word at index {result1} has prefix \"a\" and suffix \"e\"")
print()

print("Test Case 2:")
words2 = ["apple", "app", "apricot"]
wf2 = WordFilter(words2)
result2a = wf2.f("ap", "le")
result2b = wf2.f("a", "e")
print(f"Input: WordFilter({words2})")
print(f"Query 1: f(\"ap\", \"le\") = {result2a}")
print(f"Query 2: f(\"a\", \"e\") = {result2b}")
print("=" * 60)
