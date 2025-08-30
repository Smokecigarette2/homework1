#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re

text = input("Enter: ").split()

pattern = r"^a.*b$"

for i in text:
    match = re.fullmatch(pattern, i)
    if match:
        print(i)
