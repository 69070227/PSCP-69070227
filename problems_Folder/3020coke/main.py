"""coke"""

def main():
    """main"""
    og_price = int(input())
    cap_jamnuan = int(input())
    new_price = int(input())
    d_jamnuanbottle = int(input())

    if d_jamnuanbottle > 0 and cap_jamnuan > 0:
        promotion = (d_jamnuanbottle - 1) // cap_jamnuan
        fullprice = d_jamnuanbottle - promotion

        total = (fullprice * og_price) + (promotion * new_price)
        print(total)

    elif not cap_jamnuan: #cap_jamnuan == 0
        total = d_jamnuanbottle * og_price
        print(total)


    elif not d_jamnuanbottle: #d_jamnuanbottle == 0
        total = 0
        print(total)

main()
