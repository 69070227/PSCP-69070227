"""OverlapCircle"""
import math
def main():
    """main"""
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    DISTANCE = math.sqrt(((x1 -x2)**2)+((y1 - y2)**2))
    rad = r1 +r2

    if DISTANCE <= rad:
        print("overlapping")
    else:
        print("no overlapping")

main()
