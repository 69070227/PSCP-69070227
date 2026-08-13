"""PASS?NOT PASS average"""
import math

subject_N = int(input())
total = []
RESULT = ""
for i in range(subject_N):
    add_subject = float(input())
    total.append(add_subject)

result_total = sum(total)
average = result_total /subject_N
average = math.ceil(average * 100) / 100

RESULT = "PASS"
for i in total:
    if i <= 50:
        if average <= 50:
            RESULT = "FAIL"
            break
    else:
        if average > 60:
            RESULT = "PASS"


print(f"{average:.1f}")
print(RESULT)
