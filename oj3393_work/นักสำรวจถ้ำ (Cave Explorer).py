"""นักสำรวจถ้ำ (Cave Explorer)"""


def main():
    """faaaaaaaaaaaaaaaaaaaaaaaa"""
    _ = input()
    mdata = input().split()
    direction = input().upper()

    wheretwo = mdata.index("2") if "2" in mdata else -1
    now = mdata.index("1") if "1" in mdata else 0

    for i in direction:
        if i == "R":
            if now + 1 < len(mdata):
                mdata[now], mdata[now + 1] = mdata[now + 1], mdata[now]
                now += 1
        elif i == "L":
            if now - 1 >= 0:
                mdata[now], mdata[now - 1] = mdata[now - 1], mdata[now]
                now -= 1

        if wheretwo == now:
            break

    if now == wheretwo:
        for idx, val in enumerate(mdata):
            if val == "2":
                mdata[idx] = "0"
                break

    print(*mdata)

main()
