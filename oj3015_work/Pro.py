"""Pro"""
def main():
    """"main"""
    x = int(input())
    y = int(input())

    a = int(input()) #สมมติราคาต่อคน
    z = int(input()) #จำนวนคน

    come = z//x
    pay = z % x

    total = (come * y + pay) * a
    print(total)

main()
