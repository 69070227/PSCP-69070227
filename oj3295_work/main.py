"""test"""

nuai = int(input())
total = 0  # เริ่มต้นที่ 0 บาท

# บาทต่อหน่วย
for i in range(1, nuai + 1):
    if 1 <= i <= 10:
        total += 5
    elif 11 <= i <= 50:
        total += 7
    elif 51 <= i <= 100:
        total += 10
    elif 101 <= i <= 200:
        total += 12
    elif i >= 201:
        total += 15

FT = nuai * 0.50
VAT = total * 0.07
result = total + FT + VAT
result += 1e-9
# บวกค่าเล็กน้อย (1e-9) เพื่อแก้บั๊กการปัดเศษของ Python ให้ปัดขึ้นตามหลักคณิตศาสตร์ทั่วไป
result += 1e-9
print(f"{result:.1f}")
