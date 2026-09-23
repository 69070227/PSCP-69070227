""" Arrow """

# รับค่าอินพุตจากผู้ใช้งาน
direction_string = input()  # รับสตริงทิศทาง เช่น "RL" หรือ "LLR"
arrow_size = int(input())   # รับขนาดของลูกธนู (ค่า n)

# ใช้ลูปแกะลูกธนูออกมาวาดทีละดอกตามตัวอักษรในสตริง
for index, side in enumerate(direction_string):
    
    # ถ้าไม่ใช่ลูกธนูดอกแรก ให้พิมพ์บรรทัดว่างเว้นระยะห่างก่อนเริ่มดอกถัดไป
    if index > 0:
        print()

    # ตั้งค่าเริ่มต้นของจำนวนดอกจัน (*) ให้เท่ากับขนาดของลูกธนู
    star_count = arrow_size

    # กรณีที่ 1: ลูกธนูชี้ไปทางขวา (R)
    if side == "R":
        space_count = 0  # บรรทัดแรกสุดของฝั่งขวาจะไม่ห่างจากขอบ (ช่องว่าง = 0)
        
        # ลูปวาดทีละแถว ทั้งหมด 2n - 1 แถว
        for i in range((arrow_size * 2) - 1):
            print((" " * space_count) + ("*" * star_count))
            
            if i + 1 < arrow_size:
                # ครึ่งแรก: ช่องว่างเพิ่มทีละ 2, ดอกจันลดลงทีละ 1
                space_count += 2
                star_count -= 1
            else:
                # ครึ่งหลัง: ช่องว่างลดทีละ 2, ดอกจันเพิ่มขึ้นทีละ 1
                space_count -= 2
                star_count += 1
                
    # กรณีที่ 2: ลูกธนูชี้ไปทางซ้าย (L)
    else:
        space_count = arrow_size - 1  # บรรทัดแรกสุดของฝั่งซ้ายจะห่างจากขอบอยู่ n - 1 ช่อง
        
        # ลูปวาดทีละแถว ทั้งหมด 2n - 1 แถว
        for i in range((arrow_size * 2) - 1):
            print((" " * space_count) + ("*" * star_count))
            
            if i + 1 < arrow_size:
                # ครึ่งแรก: ช่องว่างลดลงทีละ 1, ดอกจันลดลงทีละ 1
                space_count -= 1
                star_count -= 1
            else:
                # ครึ่งหลัง: ช่องว่างเพิ่มขึ้นทีละ 1, ดอกจันเพิ่มขึ้นทีละ 1
                space_count += 1
                star_count += 1
