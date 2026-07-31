"""ค่าตั๋ว"""

def main():
    """smt"""
    AGE = int(input())
    CHAR = str(input())

    if AGE < 18 or (CHAR in ("s", "S")):
        print("20")
    else:
        print("50")

main()
