"""Bus Seat"""

s = int(input())      # ที่นั่งต่อแถว (เลขคู่)
r = int(input())      # จำนวนแถว
mine = int(input())   # ที่นั่งของนาย ก

for k in range(s, 0, -1):
    row = []
    for c in range(r):
        num = c * s + k
        if num == mine:
            row.append("XX")
        else:
            row.append(f"{num:02d}")
    print(" ".join(row))
    if k % 2 == 1 and k != 1:
        print()
