"""pass or not"""
subject_N = int(input())

total = 0
all_pass = True

for _ in range(subject_N):

    score = int(input())
    total += score

    if score < 50:
        all_pass = False

average = total / subject_N

print(f"{average:.1f}")

if all_pass and average >= 60:
    print("PASS")
else:
    print("FAIL")
