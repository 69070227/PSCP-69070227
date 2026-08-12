"""PASS?NOT PASS average"""
import math

subject_N = int(input())
total = []
RESULT = ""
for i in range(subject_N):
    add_subject = int(input())
    total.append(add_subject)

RESULT = "PASS"
for i in total:
    if i <= 50:
        RESULT = "FAIL"
        break

total = sum(total)
average = total /subject_N
average = math.ceil(average * 100) / 100
print(f"{average:.1f}")
print(RESULT)
