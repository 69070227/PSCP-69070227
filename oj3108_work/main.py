"""คำนวณราคาสินค้าโปรโมชั่น"""
import math
def main():
    """promo"""
    a, b, c = map(int,input().split())
    PENCIL_A = 25
    BOOK_B = 40
    BOX_C = 55

    if (a + b + c) >= 3:
        DISCOUNT = 0.90 #ลด10เปอ เหลือ 90 เปอ
    else:
        DISCOUNT = 1

    total = ((a * PENCIL_A) + (b * BOOK_B) + (c * BOX_C))*DISCOUNT

    print(math.floor(total)) #math.floor หารปัดเศษลง

main()
