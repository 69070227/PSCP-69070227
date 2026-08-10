"""ลูกน้ำ"""

def main():
    """LOOKNAM"""
    num = input()

    position = len(num) - 3

    #เอาตั้งแต่ position ไปจนถึงท้ายสุด
    spiltting_back = num[position:]

    #เอาตั้งแต่ต้น จนถึงก่อน position
    spiltting_front = num[:position]

    print(f"{spiltting_front},{spiltting_back}")

main()
