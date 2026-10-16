"""Bridge Crossing"""
def main():
    """main"""
    length, count = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(count)]
    best = max(
        sum(1 for start, end in bridges if start <= x < end)
        for x in range(length)
    )
    print(best)
main()
