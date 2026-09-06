"""pai"""

card = input()

if len(card) == 2:
    front = card[0]
    last = card[1]
if len(card) == 3:
    front = card[:2]
    last = card[2]

print(front)
print(last)
