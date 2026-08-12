"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
import math

status = input().upper()
n = int(input())
total = []

for i in range(n):
    i = i+i-i

    stuff = float(input())
    total.append(stuff)

total = sum(total)

if status =="Y":
    total = total - (total * 0.05)
    #ปัดเลขทศนิยมขึ้นและปัดเศษขึ้นก่อน แล้วค่อยปัดทศนิยมกลับลงมา
    result = math.ceil(total * 100) / 100
    print(f"{result:.2f}")

elif total >= 500:
    total = total - (total * 0.03)
    result = math.ceil(total * 100) / 100
    print(f"{result:.2f}")
else:
    result = math.ceil(total * 100) / 100
    print(f"{result:.2f}")
