"""ไฟส่อง"""
def solve():
    """fangchan"""
    n = int(input())
    x = [False] * 360
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            for i in range(a, b):
                x[i] = True
        else:
            for i in range(a, 360):
                x[i] = True
            for i in range(0, b):
                x[i] = True
    if all(x):
        print(360)
        return
    y = x + x
    m = 0
    c = 0
    for s in y:
        if s:
            c += 1
            if c > m:
                m = c
        else:
            c = 0
    print(m)


solve()
