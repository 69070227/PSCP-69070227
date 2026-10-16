"""กองชามมม"""

n = int(input())
d = [0] * 305
i = 0
mx = 0
while i < n:
    v = int(input())
    d[v] += 1
    if v > mx:
        mx = v
    i += 1

ans = 0
v = 1
while v <= mx:
    if d[v] > ans:
        ans = d[v]
    v += 1

print(ans)
