"""ค่าน้อยที่สุด (4 ค่า)"""

def main():
    """main"""
    n = int(input())
    Less = int(input())
    for _ in range(n-1):
        Num = int(input())
        if Num < Less:
            Less = Num
    print(Less)

main()
