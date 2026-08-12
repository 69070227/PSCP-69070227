"""taxi"""

distance = int(input())
price = 35

for i in range(2, distance + 1):
    if i <= 10:
        price += 5
    else:
        price += 8

print(price)
