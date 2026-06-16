def word_break(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                break

    return dp[n]

dictionary = {
    "i", "like", "sam", "sung", "samsung",
    "mobile", "ice", "cream", "icecream",
    "man", "go", "mango"
}

print("ilike :", "Yes" if word_break("ilike", dictionary) else "No")
print("ilikesamsung :", "Yes" if word_break("ilikesamsung", dictionary) else "No")