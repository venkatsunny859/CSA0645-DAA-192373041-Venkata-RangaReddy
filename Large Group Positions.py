def large_group_positions(s):

    result = []
    start = 0

    for i in range(len(s)):

        if i == len(s)-1 or s[i] != s[i+1]:

            if i - start + 1 >= 3:
                result.append([start, i])

            start = i + 1

    return result

print(large_group_positions("abbxxxxzzy"))
# [[3,6]]

print(large_group_positions("abc"))
# []