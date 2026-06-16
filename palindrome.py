words = ["notapalindrome","racecar"]

for word in words:
    if word == word[::-1]:
        print(word)
        break
else:
    print("")