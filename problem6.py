def reverse(s):
    reversed_sentence = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_sentence += s[i]
    return reversed_sentence
print(reverse(input("Write ur sentence: ")))