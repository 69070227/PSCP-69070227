"""rabbit"""

def main():
    """main"""

    carrot,cabage,tomato = map(int,input().split())
    carrot_price = 10
    cabage_price = 25
    tomato_price = 3

    TOTAL = (carrot * carrot_price) + (cabage*cabage_price) + (tomato*tomato_price)
    print(TOTAL)

main()
