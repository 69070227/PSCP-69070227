"""box"""
w, l, m, n = map(int, input().split())
left = w * l
CURRENT_LEFT = 0

for i in range(m, n + 1):
    # แนว W
    # เกินกรอบยัดไม่ได้
    if i > w and i > l:
        CURRENT_LEFT = w * l
    # ถ้าหารลงตัวแสดงว่ายัดได้พอดีทุกช่อง ไม่มีเหลือ
    elif not w % i:
        CURRENT_LEFT = 0

    else:
        if not l % i:
            CURRENT_LEFT = 0
        # เหลือเศษ
        elif l % i:
            area_L = w * ((l // i) * i)
            area_W = (l % i) * ((w // i) * i)
            CURRENT_LEFT = (w * l) - (area_L + area_W)

    if CURRENT_LEFT < left:
        left = CURRENT_LEFT


print(left)
