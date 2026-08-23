"""BONUS"""

position, age, salary = input().split()
position = position.upper()
age = int(age)
salary = int(salary)

BONUS = 0
PERSENT = 0

if position == "M":
    BONUS = 1500
elif position == "B":
    BONUS = 1000
elif position == "G":
    BONUS = 500

# ปรับตรงนี้: "ไม่เกิน 5 ปี"เปลี่ยนจาก < 5 เป็น <= 5
if age <= 5:
    if position == "M":
        PERSENT = 0.06
    elif position == "B":
        PERSENT = 0.05
    elif position == "G":
        PERSENT = 0.04

elif 5 < age <= 10:
    if position == "M":
        PERSENT = 0.08
    elif position == "B":
        PERSENT = 0.06
    elif position == "G":
        PERSENT = 0.05

elif age > 10:
    if position == "M":
        PERSENT = 0.10
    elif position == "B":
        PERSENT = 0.07
    elif position == "G":
        PERSENT = 0.06

result = (salary * PERSENT) + BONUS

print(int(result))
