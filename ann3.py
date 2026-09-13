"""elonmusk"""
x_str, k = input().split()
x = int(x_str)
mid = x // 2

for i in range(x):
    for j in range(x):
        if i == j or i + j == x - 1:
            print("#" if k == "#" else chr(ord(k) + abs(mid - i)), end="")
        else:
            print("-", end="")
    print()
