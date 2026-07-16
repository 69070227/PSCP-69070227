"""กระต่ายน้อยล้อมรั้วลวดหนาม"""

def main():
    """main"""
    Width,Length,level = map(int,input().split())
    PRICE = int(input())

    RECTANGLE = ((Width+Length)*2)*level
    total_price = RECTANGLE * PRICE
    print(RECTANGLE)
    print(total_price)

main()
