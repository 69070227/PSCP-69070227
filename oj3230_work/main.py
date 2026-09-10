"""13"""

rahas = input()
result = []

#1
if int(rahas[0]) > 5:
    result.append(9)
elif int(rahas[1]) > 5:
    result.append(10)
elif int(rahas[2]) > 5:
    result.append(11)
elif int(rahas[3]) > 5:
    result.append(12)
elif int(rahas[4]) > 5:
    result.append(14)
else:
    result.append(13)

#2
#palindrome อ่านสลับกันได้
if str(rahas) == str(rahas[::-1]):
    if int(rahas[0]) + int(rahas[4]) > 5:
        result.append(1)
    elif int(rahas[1]) * int(rahas[3]) > 5:
        result.append(2)
    else:
        result.append(0)
else:
    #ที่มี and เพื่อเช็คว่าตัวหารมากกว่า 0 ถ้าเป็น 0 แปลว่า false
    if int(rahas[4]) and int(rahas[0])// int(rahas[4]) > 5:
        result.append(1)
    elif int(rahas[1]) - int(rahas[4]) > 5:
        result.append(2)
    else:
        result.append(0)

#3
total_add = 0
for i in str(rahas):
    total_add += int(i)

total_multi = 1
for j in str(rahas):
    total_multi *= int(j)

if total_add > 25:
    result.append(1)
elif total_multi > 55:
    result.append(2)
else:
    result.append(0)

print(*result,sep= "")
