"""coke"""

def main():
    """main"""
    full_price = int(input())
    cap_jamnuan = int(input())
    discount_price = int(input())
    d_jamnuan = int(input())

    caps = 0
    cost = 0
    bought_bottle = 0

    while bought_bottle < d_jamnuan:
        if cap_jamnuan > 0:
            if caps >= cap_jamnuan:
                cost += discount_price
                caps -=cap_jamnuan
            else:
                cost +=
main()
