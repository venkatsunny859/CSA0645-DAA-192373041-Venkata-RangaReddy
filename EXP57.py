# EXP57.py - Word Segmentation using Dictionary

def word_segmentation(s, word_dict):
    """Check if string can be segmented into dictionary words"""
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return "Yes" if dp[n] else "No"

print("=" * 60)
print("Word Segmentation Problem")
print()
print("Dictionary: {i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}")
dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
print()

print("Test Case 1:")
s1 = "ilike"
result1 = word_segmentation(s1, dictionary)
print(f"Input: {s1}")
print(f"Output: {result1}")
print(f"Explanation: Can be segmented as \"i like\"")
print()

print("Test Case 2:")
s2 = "ilikesamsung"
result2 = word_segmentation(s2, dictionary)
print(f"Input: {s2}")
print(f"Output: {result2}")
print(f"Explanation: Can be segmented as \"i like samsung\" or \"i like sam sung\"")
print("=" * 60)
