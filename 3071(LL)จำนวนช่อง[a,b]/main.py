"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

A_start = int(input())
B_stop = int(input())
d_TuaHan = int(input())
r_sead = int(input())

count = 0

for x in range(A_start,B_stop + 1): #ในช่วงขอเอและบี
    if x % d_TuaHan ==r_sead:
        count +=1
print(count)
