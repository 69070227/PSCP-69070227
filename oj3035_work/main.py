"""ฟิลเตอร์ AR TikTok"""

def main():
    """main"""
    r, x, y = map(int,(input().split()))
    if x**2 + y**2 == r**2:
        print("ON")
    elif x**2 + y**2 < r**2:
        print("IN")
    elif x**2 + y**2 > r**2:
        print("OUT")


main()
