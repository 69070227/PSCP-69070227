"""birthdayyy"""
from datetime import date
y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

person1 = date(y1, m1, d1)
person2 = date(y2, m2, d2)

difference = abs((person1 - person2).days) #เอาday อกกมาใช้

if difference <= 7:
    print(0)
elif person1 < person2: #ปีน้อยกว่า เกิดก่อน
    print(1)
else:
    print(2)
