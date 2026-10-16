"""รหัสต้องไม่ซ้ำกัน"""
#no use
_ = input()
n = list(map(int,input().split()))

# ให้วิ่งเช็คในเซตของ box (เลขซ้ำ ๆ จะโดนยุบรวมเหลือตัวเดียว)
box = set()
for i in n:
    if n.count(i) == 1:
        box.add(i)
print(*sorted(box))
