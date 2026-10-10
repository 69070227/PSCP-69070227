"""Meteorite"""
namnak = float(input())
pieces = int(input())
safe = float(input())
shot_count = 0
meteor_count = 1

while True:
    if namnak < safe:
        break

    # ในรอบนี้มีอุกกาบาตอยู่เท่าไหร่ ต้องยิงจรวดใส่ทุกลูก ลูกละ 1 นัด
    shot_count += meteor_count
    
    # น้ำหนักรอบต่อไป
    namnak = namnak / pieces

    # ทุกลูกจะแตกตัวออกเป็นชิ้นเล็กชิ้นน้อยเรื่อยๆ
    meteor_count = meteor_count * pieces


print(shot_count)
