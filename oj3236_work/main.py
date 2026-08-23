"""rahas แฝดเทค"""

N = int(input())
p1 = list(input())
p2 = list(input())
NUM_WRONG = 0
for i in range(N):
    if (int(p1[i]) + int(p2[i])) != 9:
        NUM_WRONG +=1

if NUM_WRONG > 0:
    print(f"NO {NUM_WRONG}")
else:
    print("YES")
