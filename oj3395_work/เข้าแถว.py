"""เข้าแถว"""
d1 = input().split()
n = int(d1[0])
_ = int(d1[1])

h = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

mx_pref = [0] * n
mx = -1
i = 0
while i < n:
    if h[i] > mx:
        mx = h[i]
    mx_pref[i] = mx
    i += 1

for idx in q:
    pos = idx - 1
    req = 0
    if pos > 0:
        tallest = mx_pref[pos - 1]
        if tallest >= h[pos]:
            req = tallest - h[pos] + 1
    print(req)
