# EXP55.py - Longest Substring Without Repeating Characters

def longest_substring_without_repeating(s):
    """Find longest substring without repeating characters"""
    char_index = {}
    max_len = 0
    start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_len = max(max_len, i - start + 1)
    
    return max_len

print("=" * 60)
print("Longest Substring Without Repeating Characters")
print()

print("Test Case 1:")
s1 = "abcabcbb"
result1 = longest_substring_without_repeating(s1)
print(f"Input: s = \"{s1}\"")
print(f"Output: {result1}")
print(f"Explanation: The answer is \"abc\", with length {result1}")
print()

print("Test Case 2:")
s2 = "bbbbb"
result2 = longest_substring_without_repeating(s2)
print(f"Input: s = \"{s2}\"")
print(f"Output: {result2}")
print(f"Explanation: The answer is \"b\", with length {result2}")
print()

print("Test Case 3:")
s3 = "pwwkew"
result3 = longest_substring_without_repeating(s3)
print(f"Input: s = \"{s3}\"")
print(f"Output: {result3}")
print(f"Explanation: The answer is \"wke\", with length {result3}")
print("=" * 60)
