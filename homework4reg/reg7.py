#write a python program to convert snake case string to camel case string.

import re

def converter(text):

    pattern = "_"
    new_text = ""
    sub = re.sub(pattern, " ", text).split()
    for i in sub:
        new_text += i.capitalize()

    print(new_text[0].lower() + new_text[1:])




text = input("Enter: ")
converter(text)
