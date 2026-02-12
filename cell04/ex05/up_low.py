#!/usr/bin/env python3

str = input()
newstr = ""
for s in str:
    if s.islower():
        newstr += s.upper()
    else:
        newstr += s.lower()

print(newstr)