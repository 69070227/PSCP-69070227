"""rahas แฝดเทค"""

N = int(input())
p1 = list(input())
p2 = list(input())
NUM = 0
for i in range(N):
    if (int(p1[i]) + int(p2[i])) != 9:
        NUM +=1

if NUM > 0:
    print(f"NO {NUM}")
else:
    print("YES")
