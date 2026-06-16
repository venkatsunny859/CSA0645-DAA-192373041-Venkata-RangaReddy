def fullJustify(words, maxWidth):
    result = []
    i = 0

    while i < len(words):
        line_words = []
        line_len = 0

        while i < len(words) and line_len + len(words[i]) + len(line_words) <= maxWidth:
            line_words.append(words[i])
            line_len += len(words[i])
            i += 1

        spaces = maxWidth - line_len

        if i == len(words) or len(line_words) == 1:
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        else:
            gaps = len(line_words) - 1
            even_space = spaces // gaps
            extra = spaces % gaps

            line = ""
            for j in range(gaps):
                line += line_words[j]
                line += " " * (even_space + (1 if j < extra else 0))
            line += line_words[-1]

        result.append(line)

    return result

words = ["This","is","an","example","of","text","justification."]
maxWidth = 16

for line in fullJustify(words, maxWidth):
    print(f'"{line}"')