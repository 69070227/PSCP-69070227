"""Key_Midterm2014"""

id_inp = input()

total_solu1 = 0
for i in id_inp:
    total_solu1 += int(i)

solu2 = int(id_inp[-3:]) * 10

total = total_solu1 + solu2
if total >= 10000:
    total = str(total)
    total = total[1:]
elif total < 1000:
    total += 1000
print(total)
