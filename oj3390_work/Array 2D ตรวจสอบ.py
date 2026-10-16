"""arrayyyyyyyyyyyyyyyyyyyyy"""

m = []
i = 0
while i < 5:
    l = input().split()
    row = []
    j = 0
    while j < 5:
        row.append(int(l[j]))
        j += 1
    m.append(row)
    i += 1

er = -1
ec = -1

i = 0
while i < 5:
    s = 0
    j = 0
    while j < 5:
        s += m[i][j]
        j += 1
    if s % 2:
        er = i
        break
    i += 1

j = 0
while j < 5:
    s = 0
    i = 0
    while i < 5:
        s += m[i][j]
        i += 1
    if s % 2:
        ec = j
        break
    j += 1

print(str(er) + " " + str(ec))
