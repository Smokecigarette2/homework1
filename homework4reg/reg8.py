#Write a program to split a string at uppercase letters

import re

def split_upper(text):
    pattern = "?=[A-Z]"        # it means a position where the next character is an uppercase
    return re.split(pattern, text)

text = input("Enter text: ")
print(split_upper(text))


