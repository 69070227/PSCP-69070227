"""taxi"""

def main():
    """smt"""
    distance = int(input())
    price = 35

    if not distance: #distance = 0
        print("0")
    elif distance and distance <= 1:
        print(price)
    else:
        for i in range(2, distance + 1):
            if i <= 10:
                price += 5
            else:
                price += 8
        print(price)

main()
