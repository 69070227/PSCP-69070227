"""INK"""

import math
def main():
    """solutime v = s/t"""
    speed,people = map(int,input().split())

    for _ in range(people): #ทำตามค่าคนไปเรื่อยๆ ของแต่ละคน
        x,y = map(int,input().split())
        area = 3.1416 * (x**2 + y**2)
        time = math.ceil(area / speed)
        print(time)

main()
not done