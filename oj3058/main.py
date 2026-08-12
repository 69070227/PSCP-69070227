"""BrickBridge"""

small_brick = int(input())
big_brick = int(input())
GOAL = int(input())

bigB_used = min(big_brick,GOAL // 5)
#ถ้า อิฐน้อยกว่า ค่าที่goal หารด้วย 5 แสดงว่ามีอิฐน้อยกว่า เลยใช้ไม่ได้

remain_smallB = GOAL - (bigB_used * 5)

if remain_smallB <= small_brick:
    print(remain_smallB)
else:
    print("-1")
