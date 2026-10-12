"""สะสมเหรียญเวทย์มนตร์"""

n = int(input())
total = 0
fire = 0
water = 0
earth = 0
bonus = "NO"
for _ in range(n):
    F1, W1, E1, F2, W2, E2 = map(int,input().split())
    fire += max(F1,F2)
    water += max(W1,W2)
    earth += max(E1,E2)

total = fire + water + earth
if fire > (water + earth):
    bonus = "YES"

print(f"Total: {total}")
print(f"Fire: {fire}")
print(f"Water: {water}")
print(f"Earth: {earth}")
print(f"Bonus: {bonus}")
