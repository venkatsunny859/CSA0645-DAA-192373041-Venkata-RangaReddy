# EXP58.py - Text Justification

def full_justify(words, max_width):
    """Full justify text to max_width"""
    result = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= max_width:
            current_line.append(word)
            current_length += len(word)
        else:
            result.append(justify_line(current_line, max_width, False))
            current_line = [word]
            current_length = len(word)
    
    result.append(justify_line(current_line, max_width, True))
    return result

def justify_line(words, max_width, is_last):
    """Justify a single line"""
    if is_last:
        line = ' '.join(words)
        return line + ' ' * (max_width - len(line))
    
    if len(words) == 1:
        return words[0] + ' ' * (max_width - len(words[0]))
    
    total_chars = sum(len(w) for w in words)
    total_spaces = max_width - total_chars
    gaps = len(words) - 1
    spaces_per_gap = total_spaces // gaps
    extra_spaces = total_spaces % gaps
    
    line = ""
    for i, word in enumerate(words[:-1]):
        line += word + ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0))
    line += words[-1]
    
    return line

print("=" * 70)
print("Text Justification")
print()

print("Test Case 1:")
words1 = ["This", "is", "an", "example", "of", "text", "justification."]
max_width1 = 16
result1 = full_justify(words1, max_width1)
print(f"Input: words = {words1}")
print(f"maxWidth = {max_width1}")
print(f"Output:")
for line in result1:
    print(f"  \"{line}\"")
print()

print("Test Case 2:")
words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
max_width2 = 16
result2 = full_justify(words2, max_width2)
print(f"Input: words = {words2}")
print(f"maxWidth = {max_width2}")
print(f"Output:")
for line in result2:
    print(f"  \"{line}\"")
print("=" * 70)
