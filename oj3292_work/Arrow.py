"""Arrow"""
k = input()
n = int(input())
sign = n
chk = False
for side in k:
    if chk is False:
        chk = True
    else:
        print()
        sign -= 1
    if side == "R":
        space = 0
        for i in range((n * 2) - 1):
            print((" " * space) + ("*" * sign))
            if i + 1 < n:
                space += 2
                sign -= 1
            else:
                space -= 2
                sign += 1
    else:
        space = n - 1
        for i in range((n * 2) - 1):
            print((" " * space) + ("*" * sign))
            if i + 1 < n:
                space -= 1
                sign -= 1
            else:
                space += 1
                sign += 1
