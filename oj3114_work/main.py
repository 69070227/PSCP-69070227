"""eskge"""
#รับค่าและแปลงเป็นตัวเลขทศนิยม (เช่น 9.00 -> 9.0)
time_in = float(input())
time_out = float(input())

#คำนวณหาจำนวนชั่วโมง และ เศษนาที (แปลงค่าทศนิยมเป็นนาที)
# ตัวอย่าง: 9.09 -> 9 ชั่วโมง กับ 9 นาที
h_in, m_in = int(time_in), round((time_in - int(time_in)) * 100)
h_out, m_out = int(time_out), round((time_out - int(time_out)) * 100)

#รวมเวลาทั้งหมดเป็นหน่วย "นาที" เพื่อหาผลต่าง
total_in = (h_in * 60) + m_in
total_out = (h_out * 60) + m_out
diff = total_out - total_in

#เช็คเงื่อนไขตามที่โจทย์สั่ง
if diff < 0 or h_in > 23 or m_in > 59 or h_out > 23 or m_out > 59:
    print("ERROR")
elif diff <= 15:
    print("FREE")
else:
    # คำนวณชั่วโมงจอด (เศษนาทีปัดขึ้นเป็น 1 ชม.)
    hours = int(diff // 60) + (1 if diff % 60 > 0 else 0)

    # ใช้ List เก็บราคา index 1-7 (index 0 ใส่ 0 ไว้เฉยๆ)
    prices = [0, 25, 50, 80, 110, 145, 180]

    if 1 <= hours <= 6:
        print(prices[hours])
    elif 7 <= hours <= 24:
        print(250)
    else:
        print("ERROR")
