"""test"""

team,data = map(int,input().split())
all_total = 0
for i in range(team):
    box = list(map(int,input().split()))
    avr = sum(box) / data
    big = max(box)
    total = sum(box)
    all_total += total

    print(f"Team {i+1}: Average = {avr:.2f}, Max = {big}")

print(f"Total Score of All Teams = {all_total}")
