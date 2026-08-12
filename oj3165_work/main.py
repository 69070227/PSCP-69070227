"""เดินเล่นในงานเทศกาล"""

direction = input().upper()
jamnuan = len(direction)
Y = 0
X = 0

for i in range(jamnuan):
    if "N" in direction[i]:
        Y += 1
    elif "S" in direction[i]:
        Y -= 1
    elif "E" in direction[i]:
        X += 1
    elif "W" in direction[i]:
        X -= 1

D = abs(X) + abs(Y)

print(f"{X} {Y} {D}")
