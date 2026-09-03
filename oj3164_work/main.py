"""ผลรวมของค่าที่มากกว่า"""

roun = int(input())
summ = 0
ans = []
for i in range(roun) :
    num1 = int(input())
    num2 = int(input())
    if num1 >= num2 :
        summ += num1
        ans.append(num1)
    else :
        summ += num2
        ans.append(num2)

for i in range(roun) :
    print(ans[i],end=" ")
    if i < roun - 1 :
        print("+",end=" ")

if len(ans) != 1 :
    print(f"= {summ}")
