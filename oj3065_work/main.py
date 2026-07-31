"""ตัวเลขโรมันแบบง่าย"""

NUM = int(input())

def main():
    """smt"""
    if NUM < 0:
        print("Error : Please input positive number")
    elif not NUM or NUM > 9:
        print("Error : Out of range")
    else:
        # Index:    0     1     2      3     4    5     6      7       8   9
        roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "IX"]

        # NUM - 1 เพราะ Index ของ List เริ่มต้นที่ 0 (เช่น ป้อน 1 จะได้ Index 0 คือ "I")
        print(roman[NUM - 1])

main()
