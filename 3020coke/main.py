"""coke"""

def main():
    """main"""
    full_price = int(input())
    cap = int(input())
    discount_price = int(input())
    atleast = int(input())

    atleast = atleast-1

    pattern = atleast // cap
    pattern_left = atleast % cap

    price_persets = (cap - 1)* full_price + discount_price
    total_price = full_price + (pattern * price_persets) + (pattern_left * full_price)

    print(total_price)

main()
