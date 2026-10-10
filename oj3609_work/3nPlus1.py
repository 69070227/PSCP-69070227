"""test"""

while True:
    count = 1
    num = int(input())
    if not num:
        break

    while num != 1:
        if not num % 2:
            num = num // 2
        else:
            num = (num * 3) + 1
        count += 1
    print(count)
