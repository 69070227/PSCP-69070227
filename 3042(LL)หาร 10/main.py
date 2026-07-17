"""หาร10"""

def main():
    """main"""
    N = int(input())
    while N >= 0:
        if N %10 ==0:
            print(N,end =" ")
        N -= 1

main()