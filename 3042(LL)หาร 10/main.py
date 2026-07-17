"""หาร10"""

def main():
    """main"""
    N = int(input())
    total = 0
    while N //10 == 0 and N != 10:
        total -= 10
        if total == 10:
            print(total)
            break
        print(total)
main()