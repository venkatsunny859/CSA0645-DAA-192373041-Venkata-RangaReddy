# EXP56.py - Word Break Problem using DP

def word_break(s, word_dict):
    """Check if string can be segmented into dictionary words"""
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

print("=" * 60)
print("Word Break Problem")
print()

print("Test Case 1:")
s1 = "leetcode"
word_dict1 = ["leet", "code"]
result1 = word_break(s1, word_dict1)
print(f"Input: s = \"{s1}\", wordDict = {word_dict1}")
print(f"Output: {result1}")
print(f"Explanation: Return {result1} because \"{s1}\" can be segmented as \"leet code\"")
print()

print("Test Case 2:")
s2 = "applepenapple"
word_dict2 = ["apple", "pen"]
result2 = word_break(s2, word_dict2)
print(f"Input: s = \"{s2}\", wordDict = {word_dict2}")
print(f"Output: {result2}")
print(f"Explanation: Return {result2} because \"{s2}\" can be segmented as \"apple pen apple\"")
print()

print("Test Case 3:")
s3 = "catsandog"
word_dict3 = ["cats", "dog", "sand", "and", "cat"]
result3 = word_break(s3, word_dict3)
print(f"Input: s = \"{s3}\", wordDict = {word_dict3}")
print(f"Output: {result3}")
print("=" * 60)
