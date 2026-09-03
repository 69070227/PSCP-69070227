"""wrhip4h"""

N_jamnuan,K_nub,T = map(int,input().split())

times = 1
current_posi = 1

while True:
    # ถ้า T ตั้งแต่เริ่ม ให้หยุดเลย
    if current_posi == T:
        break

    # ทำให้ถ้าหาแล้วเกินวง สมมติเป็นห้า
    # ถ้าหาได้เก้า พอเอาไปหารจำนวน จะเหลือเศษสี่ จะได้ตำแหน่งที่สี่
    current_posi = (current_posi + K_nub) % N_jamnuan

    if current_posi == T:
        times += 1
        break
    if current_posi == 1:
        break

    #ถ้าไม่ตรงเงื่อนไขข้างบนให้บวกการนับ ถ้าข้างบนใช่ไม่ต้องนับตรงนี้
    times +=1
print(times)
