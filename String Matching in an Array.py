def string_matching(words):

    result = []

    for i in range(len(words)):
        for j in range(len(words)):

            if i != j and words[i] in words[j]:
                result.append(words[i])
                break

    return result


# Test Cases
print(string_matching(["mass", "as", "hero", "superhero"]))
print(string_matching(["leetcode", "et", "code"]))
print(string_matching(["blue", "green", "bu"]))