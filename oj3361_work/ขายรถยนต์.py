"""car car car"""
n = int(input())
box = []
for i in range(n):
    _,good = input().split()
    box.append(int(good))

ans = 0
mx = -1
i = n - 1
while i >= 0:
    if box[i] < mx:
        ans += 1
    else:
        mx = box[i]
    i -= 1

print(ans)
