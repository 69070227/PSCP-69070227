"""[LEARNING LOGS] สงคราม...ส่งด่วน"""


def main():
    """kamnuan"""
    first,desi =  map(str,input().upper().split())
    weight = float(input())
    TOTAL = 0
    if first == "BKK" and desi == "CNX":
        fee_start = 10
        fee_weight = 30
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    elif first == "CNX" and desi == "UBP":
        fee_start = 15
        fee_weight = 40
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    elif first == "UBP" and desi == "BKK":
        fee_start = 20
        fee_weight = 40
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    elif first == "BKK" and desi == "PKT":
        fee_start = 25
        fee_weight = 50
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    elif first == "PKT" and desi == "CNX":
        fee_start = 30
        fee_weight = 60
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    elif first == "UBP" and desi == "PKT":
        fee_start = 40
        fee_weight = 70
        TOTAL = (weight * fee_weight) + fee_start
        print(f"{TOTAL:.2f}")

    else:
        print("Error")

main()
