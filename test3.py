"""ผลรวมของค่าที่มากกว่า"""

pair_n = int(input()) * 2
num_list = []
firstnum_list = []
secondnum_list = []
big_list = []

for i in range(pair_n):
    numbers = int(input())
    num_list.append(numbers)

for k in range(0, len(num_list), 2):
    firstnum_list.append(num_list[k])

for k in range(0, len(num_list), 2):
    secondnum_list.append(num_list[k + 1])

for count in range(len(firstnum_list)):
    # เปลี่ยนเป็น >= เพื่อเก็บค่ากรณีที่ตัวเลขสองตัวเท่ากันด้วย (เช่น 8 กับ 8)
    if firstnum_list[count] >= secondnum_list[count]:
        big_list.append(firstnum_list[count])
    else:
        big_list.append(secondnum_list[count])

equation = " + ".join(map(str, big_list))

# เพิ่มเงื่อนไขตรวจสอบจำนวนคู่ตามข้อกำหนดของโจทย์
# pair_n // 2 คือจำนวนคู่ (n) ที่แท้จริง
if pair_n // 2 == 1:
    print(equation)  # ถ้ามีคู่เดียว พิมพ์เฉพาะค่าที่มากกว่าออกมาเลย (เช่น 5)
else:
    print(f"{equation} = {sum(big_list)}")  # ถ้ามีหลายคู่ พิมพ์เต็มรูปแบบ (เช่น 9 + 12 = 21)
