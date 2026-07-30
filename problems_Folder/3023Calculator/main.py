"""Calculator"""

NUM = int(input())

total_symbols = NUM - 1

result = 0


if NUM == 1:
    TOTAL_PRESS = 1
else:
    for i in range(1,NUM + 1): #เริ่มที่1 หยุดก่อน num + 1
        #นับตัวเลย ถ้าเป็นหลักเดียวอย่าง 1 2 3 จะนับกดหนื่งครั้ง ถ้าหลักสิบจะกดสองครั้ง
        total_num = len(str(i))
        result += total_num

    TOTAL_PRESS = result + total_symbols + 1

print(TOTAL_PRESS)
