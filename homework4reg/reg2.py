#Write a python program that matches a string that has an 'a' followed by two to three 'b'
import re

text = input("Text: ")
pattern = "ab{2,3}"
print(bool(re.match(pattern, text)))

#fullmatch - entire input
#match - start of the string