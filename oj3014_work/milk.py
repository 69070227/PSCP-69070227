"""milk"""
a = int(input()) # ราคานมต่อขวด
b = int(input()) # จำนวนฝาที่ต้องใช้แลก
c = int(input()) # จำนวนนมที่จะได้จากการแลก b ฝา
d = int(input()) # เงินที่ลูกค้ามี

#คำนวณการซื้อรอบแรก
initial_bottles = d // a   # หารเอาเศษ เพื่อดูว่าเงิน d บาท ซื้อนมได้กี่ขวด
total_bottles = initial_bottles # นมทั้งหมดที่ได้รับ ณ ตอนนี้
caps = initial_bottles          # ฝาขวดตั้งต้น = จำนวนขวดที่ซื้อได้

#โปรโมชัน
if b > 0 and c > 0:
    while caps >= b:
        exchanges = caps // b # จำนวนครั้งที่สามารถนำฝาไปแลกได้
        new_bottles = exchanges * c

        total_bottles += new_bottles

        caps = (caps % b) + new_bottles

print(total_bottles)
