#write a program to insert spaces between words starting with capital letters
import re


def space(text):

    new_text = ""
    pattern = "[A-Z]"
    for i in range(len(text)):
        if re.match(pattern,text[i]):
            if i == 0:
                new_text += text[i]
            else:
                new_text += " " + text[i]

        else:
            new_text += text[i]
    return new_text

text = input("Enter: ")

print(space(text))