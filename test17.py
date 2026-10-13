"""test"""

inp = input()

if len(inp) == 3:
    front = inp[0:2]
elif len(inp) == 2:
    front = inp[0]
last = inp[-1]

if front == "K":
    front = "King"
elif front == "Q":
    front = "Queen"
elif front == "J":
    front = "Jack"
elif front == "A":
    front = "Ace"

if last == "D":
    last = "Diamonds"
elif last == "H":
    last = "Hearts"
elif last == "S":
    last = "Spades"
elif last == "C":
    last = "Clubs"

print(f"{front} of {last}")
