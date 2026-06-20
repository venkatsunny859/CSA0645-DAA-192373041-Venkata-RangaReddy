# EXP54.py - Longest Palindromic Substring

def longest_palindrome(s):
    """Find longest palindromic substring using DP"""
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

print("=" * 60)
print("Test Case 1:")
s1 = "babad"
result1 = longest_palindrome(s1)
print(f"Input: s = \"{s1}\"")
print(f"Output: \"{result1}\"")
print()

print("Test Case 2:")
s2 = "cbbd"
result2 = longest_palindrome(s2)
print(f"Input: s = \"{s2}\"")
print(f"Output: \"{result2}\"")
print("=" * 60)
