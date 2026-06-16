def str_str(haystack, needle):

    for i in range(len(haystack) - len(needle) + 1):

        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


# Test Cases
print(str_str("sadbutsad", "sad"))
print(str_str("leetcode", "leeto"))