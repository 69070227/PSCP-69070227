"""PickThemAgain"""

num = input().split()
num = num[::-1]
ans = []
for i in num:
    val = int(i)
    if not val % 3 or not val % 5:
        ans.append(val)

#ถ้ามีคำตอบในกล่องให้พิมพ์ออกมา ถ้าไม่มีให้พิมพ์ Nope
if ans:
    for x in ans:
        print(x)
else:
    print("Nope")
