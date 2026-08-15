"""[LEARNING LOGS] ไพ่ 44 ใบ"""

card = input().upper()
FORNT = 0
if len(card) == 2:
    #ถ้านับได้สอง ให้เอาแค่ตำแหน่ง 0
    FORNT = card[0]
elif len(card) ==3:
    #ถ้านับได้สาม ให้เอาตำแหน่ง 0 กับ 1
    FORNT = card[:2]

LAST = card[-1]

if FORNT == "A":
    FORNT = "ace"
elif FORNT == "J":
    FORNT = "jack"
elif FORNT == "Q":
    FORNT = "queen"
elif FORNT == "K":
    FORNT = "king"

if LAST =="D":
    LAST = "diamonds"
elif LAST =="H":
    LAST = "hearts"
elif LAST =="S":
    LAST = "spades"
elif LAST =="C":
    LAST = "clubs"

print(f"{FORNT} of {LAST}")
