"""RGB Mixed"""

def pasom_2color(c1,c2):
    """หาค่าเฉลัี่ย"""
    return (c1 + c2) // 2

def pasom_rgb(color1,color2):
    """เอาแต่ละสีใส่ฟังก์ชันผสม"""
    #แบ่งสีจาก tuple
    # สมมติ r1 = 100 g1 = 200 b1 = 50 (จะเรียงตามที่ใส่)
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    #เอาแต่ละสีไปทำในฟังก์ชันผสมสองสี เช่นเอาสีแดงที่ 1 กับ สอง มาผสมกัน
    r_mix = pasom_2color(r1, r2)
    g_mix = pasom_2color(g1, g2)
    b_mix = pasom_2color(b1, b2)
    return r_mix, g_mix, b_mix

def inp():
    """ตั้งค่าตัวแปรแยกเป็นแต่ละสี"""
    # เรียงค่าแต่ละตัวใน tuple พอจะใช้ก็เอาตัวแรกละเรียงไปเรื่อยๆ
    color1 = tuple(map(int,input().split()))
    color2 = tuple(map(int,input().split()))
    r_mix, g_mix, b_mix = pasom_rgb(color1, color2)
    print(r_mix, g_mix, b_mix)

inp()
