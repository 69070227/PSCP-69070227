"""แลกเปลี่ยนเงิน"""

def main():
    """main"""
    N = int(input())

    rean_sib = N // 10
    left = N % 10
    rean_ha = left // 5
    left = left % 5
    rean_song = left // 2
    left = left % 2
    rean_nueng = left // 1
    left = left % 1

    print(f"10 = {rean_sib}")
    print(f"5 = {rean_ha}")
    print(f"2 = {rean_song}")
    print(f"1 = {rean_nueng}")

main()
