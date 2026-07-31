"""ปีอธิกสุรทิน"""

YEAR = int(input())

if YEAR < 1582:
    if not YEAR % 4: #ถ้าหารแล้วเศษเหลือ 0
        print("yes")
    else:
        print("no")
else:
    if not YEAR % 100 and YEAR % 400: # ถ้าหาร100ลงตัว และ หาร400 ไม่ ลงตัว
        print("no")
    else:
        print("yes")
