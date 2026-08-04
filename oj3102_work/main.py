"""ภาษีรถยนต์"""

def main():
    """SOLU_TAX"""

    year = int(input())
    cc_size = int(input())
    TAX = 0

    if year <= 1990:
        if cc_size <= 1500:
            TAX = 1250
        elif 1500 < cc_size <= 2000:
            TAX = 1400
        else:
            TAX = 2000

    elif 1991 <= year <= 1999:
        if cc_size <= 1500:
            TAX = 1100
        elif 1500 < cc_size <= 2000:
            TAX = 1300
        else:
            TAX = 1700

    elif year >= 2000:
        if cc_size <= 1500:
            TAX = 1000
        elif 1500 < cc_size <= 2000:
            TAX = 1200
        else:
            TAX = 1500

    print(TAX)

main()
