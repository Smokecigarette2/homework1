#write a Python program replace all occurrences of space, comma, or dot with a colon
import re

def substitute(text):
    pattern = "[\s,.]"

    return re.sub(pattern, ":", text)

text = input("Enter here: ")
print(substitute(text))