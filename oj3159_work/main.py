"""factorial"""

NUM = int(input())
total = 1
for i in range(1,NUM + 1):
    total *= i

print(total)
