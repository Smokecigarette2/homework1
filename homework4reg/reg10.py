#Python program to convert a given camel case strong to snake case

import re

def convert(text):

    t = ""
    pattern = "[A-Z]"
    for i in range(len(text)):
        if re.match(pattern,text[i]):
            t+= "_" + text[i].lower()
        else:
            t+=text[i]
    return t

text = input("Enter: ")
print(convert(text))