"""[Recommend] สามเหลี่ยม"""

n = int(input())

for i in range(1,n+1):

    if (n > 3 and i > 2) and i != n:
        print(f"0{"1"*(i - 2)}0")
    else:
        print("0"*i)
