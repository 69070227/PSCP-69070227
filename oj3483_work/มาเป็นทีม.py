"""มาเป็นทีม"""

team, data = map(int, input().split())

ok = True
all_scores = []

#เช็คว่า N กับ M อยู่ในช่วงไหม
if not (1 <= team <= 10 and 1 <= data <= 20):
    ok = False
else:
    for i in range(team):
        box = list(map(int, input().split()))
        if len(box) != data:
            ok = False
        for s in box:
            if s < 0 or s > 100:
                ok = False
        all_scores.append(box)

if not ok:
    print("Data Incorrect")
else:
    all_total = 0
    for i in range(team):
        box = all_scores[i]
        total = sum(box)
        all_total += total
        print(f"Team {i+1}: Average = {total / data:.2f}, Max = {max(box)}")

    print(f"Total Score of All Teams = {all_total}")
