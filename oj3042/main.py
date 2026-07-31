"""หาร10"""

def main():
    """main"""
    N = int(input())
    while N >= 0:
        if not N %10:
            print(N,end =" ")
        N -= 1

main()
