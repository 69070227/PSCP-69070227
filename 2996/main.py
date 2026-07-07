"""สลับตัวอักษร"""

text = input()
makesmall = text.casefold()
if len(text) == 5:
    print(makesmall[::-1])
