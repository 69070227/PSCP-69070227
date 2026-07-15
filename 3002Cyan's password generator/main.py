"""Cyan's password generator"""

name = input()
surname = input()
AGE = str(input())

if len(name) >= 5 and len(surname) >= 5:
    password = name[:2] + surname[-1] + AGE[-1]
    print(password)

else:
    password = name[0] + AGE + surname[-1]
    print(password)
