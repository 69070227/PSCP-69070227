"""[LEARNING LOGS] A-E-I-O-U"""

WORD = input().casefold()

vowels = ["a","e","i","o","u"]
count = [0, 0, 0, 0, 0]

for ch in WORD:
    if ch == "a":
        count[0]+=1
    elif ch == "e":
        count[1]+=1
    elif ch == "i":
        count[2]+=1
    elif ch == "o":
        count[3]+=1
    elif ch == "u":
        count[4]+=1

for i in range(5):
    if count[i] > 0:
        print(vowels[i], ":", count[i])
