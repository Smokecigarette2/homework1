 # Write a python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = ""
pattern = r"ab*"

print(bool(re.search(pattern, text)))