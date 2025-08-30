#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

text = input("Enter: ").split()

pattern = r"[A-Z][a-z]+"

for i in text:
    match = re.findall(pattern, i)
    if match:
        print(match)