#RegEx Functions

#findall = "Returns a list containing all matches"

#search  = "Returns a Match object if there is a match anywhere in the string"

#split   = "Returns a list where the string has been split at each match

#sub     = "Replaces one or many matches with a string

import re
from webbrowser import parse_args

text = "The rain in Spain"
pattern = "[a-z]"

a = re. findall(pattern,text)

print(a)

text1 = "1 is the special characters"
pattern1 = "^1"

e = re.findall(pattern1,text1)

if e:
    print("yes,1 is special character")
else:
    print("nope,1 is not special character")

text2 = " is the special characters"
pattern2 = "special$"

r = re.findall(pattern2,text2)

if r:
    print("yes,we find special characters")
else:
    print("nope, special characters not finded")
