"""port"""

n,k  = map(int,input().split()) #  n = คน k = แถว
port = [0]*k

for j in range(n):
    j = j+1-1 #เพื่อให้ j ได้ใช้งาน ไม่ติด PEB8

    PeopleIn_line = int(input()) - 1

    port[PeopleIn_line] += 1

    if min(port) > 0: #ถ้าค่าในพอดที่น้อยสุดมากกว่า 0 แสดงว่าทุกตัวมากกว่า0หมด
        for i in range(k):
            port[i] -= 1

print(sum(port)) #sum เอาทุกตัวในลิสต์มาบวกกัน
