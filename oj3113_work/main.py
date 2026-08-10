"""กระต่ายน้อยกินราเมน"""

size, type_ramen = input().upper().split()
topping = input().upper().split()
TOTAL = 0
if len(topping) == 2:
    AMOUNT = int(topping[1])
else:
    AMOUNT = 1

if size == "S":
    #tammadar
    TOTAL = 60

elif size == "M":
    #tammadar
    TOTAL = 80

elif size == "L":
    #tammadar
    TOTAL = 100

if type_ramen == "T":
    TOTAL += 20

if topping[0] == "P":
    TOTAL += 15 * AMOUNT
elif topping[0] == "E":
    TOTAL += 10 * AMOUNT

print(TOTAL)
