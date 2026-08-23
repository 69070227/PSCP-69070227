"""INFLATIon"""
n = float(input())
k = int(input())

# วนลูปคิดเงินเฟ้อทีละปี
for year in range(k):
    # คำนวณเงินเฟ้อของปีนั้น
    inflation = n * 0.0381

    # แก้ปัญหาทศนิยมเพี้ยน: แปลงเป็นข้อความที่มีทศนิยมยาวๆ ก่อน
    inf_str = f"{inflation:.10f}"

    # แยกส่วนหน้าจุด และ ส่วนหลังจุดทศนิยม
    before_dot, after_dot = inf_str.split('.')

    # บังคับตัดเอาเฉพาะหลังจุดแค่ 2 ตัวแรกเท่านั้น (เช่น 31999 -> 31)
    clean_inflation = float(before_dot + '.' + after_dot[:2])

    # นำเงินเฟ้อที่ตัดเศษแล้วไปบวกเข้ากับราคาสินค้าเดิม
    n = n + clean_inflation

print(f"{n:.2f}")
