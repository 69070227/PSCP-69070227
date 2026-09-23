"""Elo"""
def main():
    """main"""
    RA = int(input())
    RB = int(input())
    WINNER = str(input())
    EA = 0
    EB = 0
    if WINNER == "A":
        EA = 1/(1+10**((RB-RA)/400))
        print(f"{EA:.2f}")
    elif WINNER =="B":
        EB = 1/(1+10**((RA-RB)/400))
        print(f"{EB:.2f}")
main()
