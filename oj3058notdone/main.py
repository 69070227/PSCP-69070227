"""BrickBridge"""

small_brick = int(input())
big_brick = int(input())
GOAL = int(input())

smallB_yao = 1
bigB_yao = 5

total = 0

while total < GOAL:
    if big_brick > 0:
        solu_bigB = big_brick * bigB_yao
        total = GOAL - solu_bigB
        big_brick -= 1

    if not big_brick:
        solu_smallB = small_brick * smallB_yao
        total = GOAL - solu_smallB
        small_brick -= 1

print(total)





