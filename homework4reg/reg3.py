#Write a python program to find sequences of lowercase letters joined with an underscore.
import re

text = input("Enter text: ").split() # to transfer input to a list

pattern = "[a-z]+_[a-z]+" #[a-z]+ one or more lowercase characters


for i in text:
    print(re.findall(pattern, i))


#findall returns a list of matches
#search gives u the first match