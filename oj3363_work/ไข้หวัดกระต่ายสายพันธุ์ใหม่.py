"""rabbit covid"""


def main():
    """Main function"""
    r, c = map(int, input().split())
    kr, kc = map(int, input().split())

    inf = [tuple(map(int, input().split())) for _ in range(int(input()))]
    grid = [[0] * c for _ in range(r)]

    for pr, pc in inf:
        for i in range(r):
            for j in range(c):
                m = max(abs(i - pr), abs(j - pc))

                if not m:
                    val = 100
                elif m == 1:
                    val = 60
                elif m == 2:
                    val = 20
                else:
                    val = 0

                if val > grid[i][j]:
                    grid[i][j] = val

    safe = sum(row.count(0) for row in grid)

    print(safe)
    print(f"{grid[kr][kc]}%")


if __name__ == "__main__":
    main()
