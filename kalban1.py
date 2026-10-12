"""บทที่ 4 input output"""

# a = 25
# b = 1253.59845
# c = "python"

# print("hello %s programiming" % c)
# print("a = %d" % a)
# print("b = %d" % b)
# print("%s is easy" % c)
# print("%d" % (b - 100))
# print("b = %f" % b)
# print("b %.2f" % b)
# print("%d %.2f" % (a, b))


# print(f"hello {c} programming")
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"{c} is easy")
# print(f"{int(b - 100)}")
# print(f"{float(b)}")
# print(f"{float(b):.2f}")
# print(f"{int(a)} {float(b):.2f}")

# print("Hello World")
# print("\"I don't have a car\"")
# print("You got a new job!? That's so exciting")
# print("a\nan\nant")
# print("Just because something\n" \
#     "thinks differently from you,\n" \
#     "does that mean it's not thinking?")

# a = 12.5
# print(a)

# a = 2
# b = 3
# print(f"{a} x {b} = {a * b}")

# a = 2.4
# b = 2.5
# print(f"{a} + {b} = {(a + b):.4f}")

# a = 5
# b = 2
# print(f"{a:.2f} - {b:.2f} = {(a - b):.5f}")

# bday = 25
# print(f"ฉันเกิดวันที่ {bday}")

# a = 5
# b = 100
# print(f"{a} เท่าของ {b} มีค่าเท่ากับ {a * b}")

#print("\"Good moring\"")

# print("*")
# print("**")
# print("***")

# a = int(input())
# b = int(input())
# print(a + b)

# a = input()
# b = int(input())
# print(a * b)

# a = int(input())
# b = int(input())
# c = int(input())
# print((a + b + c) / 3)

# weight = int(input())
# height = int(input())
# print(f"{weight} {height}")

# inp = input()
# print(f"You press {inp}")

# m = int(input())
# n = int(input())
# print(m - n)

# name = input("Enter your first name: ")
# surname = input("Enter your last name: ")
# age = input("Enter your age: ")
# print(f"Hello {name} {surname}")
# print(f"You're {age} years old")

"""บทที่5 Variable & Casting"""


# #Name = "ผิด" # เพราะมีตัวพิเศษ
# True = "ผิด" # เพราะเป็นค่าbooleen
# name = "ถูก"
# return = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# first name = "ผิด" # เพราะมีการเว้น space
# first_name = ถูก"
# "haha" = "ผิด" # เพราะมี double quoat
# 15 = "ผิด" # เพราะเป็นตัวเลข
# 1ion = "ผิด" # เพราะมีตัวเลขข้างหน้าสุด
# 1gr@de = "ผิด" # เพราะมีตัวพิเศษ
# 1if = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# 1while = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# 1[b] = "ผิด" # เพราะมี []
# 1_name = "ถูก"
# 1pyThon = "ถูก"

# C = int(input())
# f = ((9/5)*(C)) + 32
# k = C + 273.15
# print(f"{f} {k}")

# base = float(input())
# height = float(input())
# print(f"{((1/2)*base*height):.6f}")

"""บทที่ 6 data types"""


# เกรดเฉลี่ยของนักเรียน รับเป็น#float เพราะ หารแล้วจะได้ทศนิยมเสมอ
# อายุของนักศึกษา รับเป็น#int เพราะ อายุนับเป็นจำนวนเต็ม
# ชื่อผู้ใช้งานระบบ รับเป็น#string เพราะ เป็นชื่อ
# เงินเดิอนสะสมรายปีของพนักงาน รับเป็น#float เพราะมีดอกาสเป็นทศนิยม
# รหัสบัตร ATM รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# รหัสประจำตัวประชาชน รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# หมายเลขโทรศัพท์มือถือ รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# พื้นที่ของวงกลม รับเป็น float เพราะเป็นเลขที่คูณด้วย 3.14
# น้ำหนัก รับเป็น float เพราะมีทศนิยมได้
# 1ราคาสินค้า รับเป็น float เพราะอาจมีสตางค์

# a = int(input())
# b = int(input())
# print(f"Addition: {a+b}")
# print(f"Concatenation: {str(a) + str(b)}")


# midterm = float(input())
# final = float(input())
# total = midterm + final
# avg = total / 2
# print(f"Total: {total}")
# print(f"Average: {avg}")


# w = float(input("Enter width:"))
# l = float(input("Enter length:"))
# d = float(input("Enter depth:"))
# volumn = w * l * d  # กว้าง x ยาว x ลึก
# total_minute = (volumn * 15)/60
# print(f"Time to fill a pool is {total_minute:.2f} minutes.")
##output:
##Enter width:18.5
## Enter length:38.75
## Enter depth:1.35
## Time to fill a pool is 241.95 minutes.

"""บทที่ 7 Operators"""

# จงกำหนดลำดับการทำงานตามลำดับความสำคัญของตัวดำเนินการด้วยการใส่วงเล็บ
# เช่น a = b + c * d จะได้เป็น a = (b + (c * d))

# a = a + b – c + a
# a = a + ((b * c) / a)
# a = ((c * a) / d) + b
# a = ((a % b) / c) + d
# a = ((a % b) / c) % d
# 6 a = a + ((b % c) * d)
# a = a – ((b / c) % (d ** e))

# จงหาค่าของตัวแปร x เมื่อกำหนด x = 0, a = 10, b = 7, c = 3, d = 6, e = 1, f = 2

# x = (a / f) – (c * b) + e
    ## ตอบบ = -15.0
# x = b + (c * e) – (f % a)
    ## ตอบบ =  x = 7 + 3 - 2 = 8
    ### print(2 % 10) ➡️ ได้ 2
    ### ถ้าตัวตั้งน้อยกว่าตัวหาร ผลลัพธ์ของ % จะได้เท่ากับตัวตั้งเสมอครับ (เช่น 3 % 10 ได้ 3, 5 % 10 ได้ 5)
# 1x = ((e * b) * d) – (f % a)
    ## ตอบบ = 42 - 2 = 40
# 1x = ((f * a) – d) + (e * d)
    ## ตอบบ = 14 + 6 = 20
# 1x = b + f – ((b % e) * f)
    ## ตอบบ = 9
# 1x = a – (((b * e) / b) % d)
    ## ตอบบ = 10 - 1 = 9.0

#1จงเขียนโปรแกรมรับค่า n ซึ่งเป็นเลขจำนวนเต็มบวก และรับอักขระ 2 ตัว บรรทัดละตัว แล้วพิมพ์อักขระ
#ความยาว n ตัวในบรรทัดเดียวกัน โดยให้พิมพ์อักขระ 2 ตัว สลับกัน โดยไม่ใช้ if-else or loop

    # n = int(input())
    # s1 = input()
    # s2 = input()
    # print(((s1 + s2) * (n // 2 + 1))[:n])   

# 1จงเขียนโปรแกรมเพื่อรับค่าเศษ (numerator) และค่าส่วน (denominator) ของเศษส่วน (fraction)
# สองจำนวน แล้วคำนวณหาผลรวมของเศษส่วนทั้งสอง
# สมมติให้เศษส่วนแรกอยู่ในรูป a/b และเศษส่วนที่สองอยู่ในรูป c/d ในที่นี้ให้แสดงผลลัพธ์ p/q ซึ่งเป็นผลรวมที่ได้
# ในรูปเศษส่วนเช่นกัน และไม่ต้องทำให้เป็นเศษส่วนอย่างต่ำ

    # first_num = int(input("Enter a numerator a: "))
    # first_deno = int(input("Enter a denominator b: "))

    # first = first_num / first_deno

    # second_num = int(input("Enter a numerator a: "))
    # second_deno = int(input("Enter a denominator b: "))

    # numerator = (first_num * second_deno) + (first_deno * second_num)
    # denominator = first_deno * second_deno

    # print(f"Summation of the two fractions is {numerator} / {denominator}")

# 1จงเขียนโปรแกรมเพื่อรับจำนวนวินาทีที่ใช้ออกกำลังกาย 2 ครั้ง แล้วแสดงผลเวลารวมที่ใช้ในการออก
# กำลังกายในรูปของจำนวนชั่วโมง นาที และวินาที ตามลำดับ
# ข้อมูลเข้า
# บรรทัดแรก แสดงข้อความ "Enter your exercise time 1" และรอรับจำนวนเต็ม s1 แทนจำนวน
# วินาทีที่ใช้ออกกำลังกาย ครั้งที่ 1
# บรรทัดสอง แสดงข้อความ "Enter your exercise time 2" และรอรับจำนวนเต็ม s2 แทนจำนวนวินาที
# ที่ใช้ออกกำลังกาย ครั้งที่ 2

    # inp1 = int(input("Enter your exercise time 1: "))
    # inp2 = int(input("Enter your exercise time 2: "))

    # total_seconds = (inp1 + inp2)
    # # คำนวณหาชั่วโมง นาที และวินาที
    # hour = total_seconds // 3600
    # remaining_seconds = total_seconds % 3600
    # minu = remaining_seconds // 60
    # sec = remaining_seconds % 60

    # print(f"It is {hour} hours {minu} minutes and {sec} seconds.")


"""บทที่ 8 MATH"""

# import math
# x = 1
# y = math.sqrt(16 - (4 * x))
# y = math.sqrt(16 - (4 * x)**2)
# y = abs(15-50)
# s = (u * t) + ((1/2) * a * t**2)
# x = (math.sqrt(-b + (math.sqrt(b**2 - (4 * a * c))))) / (2 * a)

# จงเขียนโปรแกรมเพื่อแปลงเลขจำนวนเต็มลบ ให้เป็นจำนวนเต็มบวก
# ข้อมูลเข้า
# บรรทัดแรก รับตัวเลขจำนวนเต็มลบ
# ข้อมูลออก
# แสดงตัวเลขที่เป็นจำนวนเต็มบวก

    # num_inp = int(input())
    # print(abs(num_inp))

# จงเขียนโปรแกรมเพื่อแปลงเลขจำนวนจริงลบ ให้เป็นจำนวนเต็มบวก
# ข้อมูลเข้า
# บรรทัดแรก รับตัวเลขจำนวนจริงลบ
# ข้อมูลออก
# แสดงตัวเลขที่ปัดทศนิยมขึ้น และเป็นจำนวนเต็มบวก 

    # import math
    # num_inp = float(input())

    # print(math.ceil(abs(num_inp)))

# จงเขียนโปรแกรมเพื่อคำนวณหาพื้นที่วงกลมและเส้นรอบวงของวงกลมที่มีรัศมี r
# กำหนดให้ข้อมูลเข้าเป็นเลขจำนวนเต็มเท่านั้น แสดงพื้นที่และเส้นรอบวงเป็นเลขจำนวนจริงทศนิยมสองตำแหน่ง
# ข้อมูลเข้า
# บรรทัดเดียว แสดงข้อความ "Enter a radius:" และรอรับจำนวนเต็ม r ซึ่งไม่เป็นลบ แทนรัศมีของ
# วงกลม
# ข้อมูลออก
# บรรทัดแรก แสดงข้อความ "Area of a circle with radius" ตามด้วยค่า r ตามด้วย "is" ตามด้วยพื้นที่
# ของวงกลมรัศมี r
# บรรทัดที่สอง แสดงข้อความ "Circumference of a circle with radius" ตามด้วยค่า r ตามด้วย "is"
# ตามด้วยเส้นรอบวงของวงกลมรัศมี 

    # import math
    # r = int(input("Enter a radius: "))

    # area_cir = math.pi * (r)**2
    # circum = 2 * math.pi * r

    # print(f"Area of a circle with radius {r} is {area_cir:.2f}")
    # print(f"Circumference of a circle with radius {r} is {circum:.2f}")


"""บทที่ 9 BOOLEEN"""


# จงแสดงผลลัพธ์ต่อไปนี้กำหนดให้
a = 15
b = 25
c = 15
e = "Hello"
f = ""
g = " "
h = 0

# print(a > b)   >>> False
# print(a > b or c > b)   >>> False
# print(a > b or c < b)   >>> True
# print(c > b and b < a)   >>> False
# print(c < b and b > a)   >>> True
# print(a == c)   >>> True
# print(a >= c and b >= a or e == "Hello")   >>> True
# print(e == "Hello" or a < c and b >= a)   >>> True
# print(bool(h))   >>> False
# print(bool(e))   >>> True
# print(bool(h) and bool(f))   >>> False
# print(bool(h) or bool(f))   >>> False
# print(bool(g) and bool(a))   >>> True
# print(bool(not(h)))   >>> True
# print(bool(not(h)) and bool(not(f)))   >>> True

# 16. รับค่า a และ b เป็นเลขจำนวนเต็ม จากนั้นทำการสลับค่าตัวแปร
# ข้อมูลนำเข้า
# บรรทัดแรก รับ a เป็นเลขจำนวนเต็ม
# บรรทัดที่ 2 รับ b เป็นเลขจำนวนเต็ม
# ข้อมูลส่งออก
# บรรทัดแรก สลับค่าจากตัวแปร a ให้เป็น b
# บรรทัดที่ 2 สลับค่าจากตัวแปร b ให้ เป็น a

    # a = int(input("a = "))
    # b = int(input("b = "))

    # reverse_a_for_b = a
    # a = b
    # b = reverse_a_for_b

    # print(f"a = {a}")
    # print(f"b = {reverse_a_for_b}")


"""unit10 if/else เงื่อนไข"""

# จงพิจารณาชุดคำสั่งต่อไปนี้ พร้อมตอบคำถาม
# if y == 8:
# if x == 5:
# print("@@@@@")
# else:
# print("#####")
# print("$$$$$")
# print("&&&&&")
    # 1. ถ้า x = 5 และ y = 8   >>> @@@@@,$$$$$,&&&&&
    # 2. ถ้า x = 5 และ y = 5   >>> $$$$$,&&&&&
    # 3. ถ้า x = 8 และ y = 8   >>> #####,$$$$$,&&&&&
    # 4. ถ้า x = 8 และ y = 5   >>> $$$$$,&&&&&


# 5. รับค่าคะแนน เป็นเลขจำนวนเต็ม แล้วทำการเขียนโปรแกรมเพื่อคำนวณเกรด โดยมีเกณฑ์การให้เกรด
# ดังนี้
# - ถ้าคะแนนมากกว่าหรือเท่ากับ 80 ได้เกรด A
# - ถ้าคะแนนอยู่ในช่วง 70 – 79 ได้เกรด B
# - ถ้าคะแนนอยู่ในช่วง 60 – 69 ได้เกรด C
# - ถ้าคะแนนอยู่ในช่วง 50 – 59 ได้เกรด D
# - ถ้าคะแนนต่ำกว่า 50 ได้เกรด F

    # kanan = int(input())
    # if kanan >= 80:
    #     print("A")
    # elif 70 <= kanan <= 79:
    #     print("B")
    # elif 60 <= kanan <= 69:
    #     print("C")
    # elif 50 <= kanan <= 59:
    #     print("D")
    # elif 50 > kanan:
    #     print("F")

# 6. รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าจำนวนนั้นมากกว่า 31 หรือไม่
    # num = int(input())
    # if num > 31:
    #     print(True)

# 7. รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าจำนวนนั้นน้อยกว่า 90 หรือไม่
    # num = int(input())
    # if num < 90:
    #     print(True)

# 8. รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าเป็นจำนวนคู่หรือคี่
    # num = int(input())
    # if num % 2 == 0:
    #     print("even")
    # else:
    #     print("odd")

# 9. รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าเป็นจำนวนที่หารด้วย 3 ลงตัวหรือไม่
    # num = int(input())
    # if num % 3 == 0:
    #     print(True)
    # else:
    #     print(False)

# 10. รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าเป็นจำนวนคู่ที่หารด้วย 3 ลงตัวหรือไม่
    # num = int(input())
    # if num % 6 == 0:
    #     print(True)
    # else:
    #     print(False)

# 11. รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่าจำนวนนั้นมีเลขแต่ละหลักเหมือนกันหรือ
# ต่างกัน
    # num = input()
    # firstnum = num[0]
    # secondnum = num[1]
    # if firstnum == secondnum:
    #     print("เลขเหมือนกัน")
    # else:
    #     print("เลขต่างกัน")

# 12. รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่าจำนวนนั้นมีเลขโดดในหลักสิบมากกว่าเลข
# โดดในหลักหน่วยหรือไม่
    # num = int(input())

    # tens = num // 10 # หลักสิบ
    # nuai = num % 10 # หลักหน่วย

    # if tens > nuai:
    #     print(f"หลักสิบ ({tens}) มากกว่าหลักหน่วย ({nuai})")
    # else:
    #     print(f"หลักสิบ ({tens}) ไม่ได้มากกว่าหลักหน่วย ({nuai})") 

# 13. รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่า หลักหน่วยน้อยกว่า (หรือมากกว่า หรือ
# เท่ากับ) หลักสิบอยู่เท่าไหร่

    # num = int(input())

    # tens = num // 10 # หลักสิบ
    # nuai = num % 10 # หลักหน่วย
    # symbols = ""
    # if nuai > tens:
    #     symbols = ">"
    # elif nuai < tens:
    #     symbols = "<"
    # elif nuai == tens:
    #     symbols = "="

    # print(f"หน่วย {nuai} {symbols} สิบ {tens}")

# 14. รับจำนวนเต็มบวกที่เป็นเลขสองหลักหนึ่งจำนวน แล้วหาว่าผลรวมของเลขโดดมีค่าเท่ากับ 15 หรือไม่
    
    # num = int(input())

    # tens = num // 10 # หลักสิบ
    # nuai = num % 10 # หลักหน่วย

    # solu = tens + nuai

    # if solu == 15:
    #     print(True)
    # else:
    #     print(False)

# 15. รับจำนวนเต็ม 3 จำนวน แล้วหาจำนวนที่มากที่สุด

    # num1,num2,num3 = map(int,input().split())
    # print(max(num1,num2,num3))

# 16. รับจำนวนเต็ม 3 จำนวน แล้วหาว่าจำนวนที่มากที่สุดมากกว่าจำนวนที่น้อยที่สุดอยู่เท่าไหร
    # num1,num2,num3 = map(int,input().split())
    # solu = max(num1,num2,num3) - min(num1,num2,num3)
    # print(solu)


# 17. สูตรในการเปลี่ยนค่าจากองศาเซลเซียสเป็นองศาฟาเรนไฮต์และเคลวิน มีดังนี้
# 𝐹 =
# 9
# 5
# 𝐶 + 32
# 𝐾 = 𝐶 + 273.15
# ให้อ่านข้อมูลอุณหภูมิ (หน่วยองศาเซลเซียส) แล้วคำนวณหาค่าองศาฟาเรนไฮต์และเคลวิน เมื่อ C คือ องศา
# เซลเซียส F คือ องศาฟาเรนไฮต์ และ K คือเคลวิน
# ข้อมูลเข้า
# บรรทัดแรก รับค่าอุณหภูมิหน่วยองศาเซลเซียส เป็นจำนวนจริง
# บรรทัดที่สอง รับตัวอักษรหนึ่งตัว ตัวใหญ่หรือตัวเล็กก็ได้

    # c = float(input())
    # name = input().upper()

    # if name == "F":
    #     solu = (9/5)*c + 32
    # elif name == "K":
    #     solu = c + 273.15
    # else:
    #     solu = "Error"

    # print(solu)

# 18. ค่า BMI เป็นค่าที่ใช้วัดความอ้วน เพื่อประเมินหาไขมันส่วนเกินในร่างกาย เพื่อคำนวณความเสี่ยงในการ
# เป็นโรค
# สูตรการคำนวณ คือ
# 𝑤𝑒𝑖𝑔ℎ𝑡
# ℎ𝑒𝑖𝑔ℎ𝑡
# 2
# ซึ่ง weight มีหน่วยเป็น กิโลกรัม (kg) และ height มีหน่วยเป็น เมตร (m)
# จงเขียนโปรแกรมหาค่า BMI โดยบอกว่าค่า BMI ที่ได้นั้นเป็นเช่นไรเมื่อเทียบกับเกณฑ์ ดังนี้
# - Underweight เมื่อค่า BMI น้อยกว่า 18.5
# - Normal weight เมื่อค่า BMI มีค่าตั้งแต่ 18.5 แต่ไม่ถึง 25
# - Overweight เมื่อค่า BMI มีค่าตั้งแต่ 25 แต่ไม่ถึง 30
# - Obesity เมื่อค่า BMI มีค่าไม่ต่ำกว่า 30

    # weight = float(input())
    # height = float(input())

    # bmi = weight/(height**2)

    # if bmi < 18.5:
    #     result = "Underweight"
    # elif 18.5 <= bmi < 25:
    #     result = "Normal weight"
    # elif 25 <= bmi < 30:
    #     result = "Overweight"
    # elif bmi >= 30:
    #     result = "Obesity"

    # print(f"BMI is {bmi:.1f}")
    # print(result)

# 19. บริษัท ABC จำกัด ต้องการให้ส่วนลดลูกค้าที่ซื้อสินค้าในมูลค่าตั้งแต่ 1000 บาทขึ้นไป โดยถ้าลูกค้าซื้อ
# สินค้าตั้งแต่ 1000 บาทขึ้นไป แต่น้อยกว่า 3000 บาท ให้ส่วนลด 10% และถ้าซื้อสินค้าตั้งแต่ 3000 บาทขึ้นไป ให้
# ส่วนลด 15%
# จงเขียนโปรแกรมที่รับจำนวนราคาสินค้าแล้วคำนวณเงินสุทธิที่ลูกค้าต้องชำระ

    # buying = float(input("Enter buying amount: "))
    # discount = 1
    # if buying >= 1000 and buying < 3000:
    #     discount = 0.90
    # elif buying >= 3000:
    #     discount = 0.85
    # solu = buying * discount
    # print(f"Amount due after discount is {solu:.2f} baht")

# 20. จงเขียนโปรแกรมสำหรับเล่นเกมทายตัวเลข โดยกำหนดให้โปรแกรมสร้างเลขเป้าหมาย (target) ที่มีค่า
# ตั้งแต่ 0 – 100 แล้วรับตัวเลขจากผู้เล่นที่ทายเข้ามา กำหนดให้เป้าหมาย (target) เท่ากับ 72

    # num = int(input("Enter your guess (0 - 100): "))
    # correct_num = 72
    # if num > 100 or num < 0:
    #     print("Sorry, out of range, try again later")
    # elif num == correct_num:
    #     print("Congratulations, your guess is correct.")
    # else:
    #     print("Sorry, your guess is wrong, try again later")

# 21. เขียนโปรแกรมเพื่อตรวจสอบ Username และ Password เพื่อตรวจสอบว่าเป็น Admin หรือไม่
# กำหนดให้
# - username คือ admin
# - password คือ Ad13n@23t

    # userinp = input("Username: ")
    # passwordinp = input("Password: ")

    # correctuser = "admin"
    # correctpassword = "Ad13n@23t"

    # if userinp == correctuser and passwordinp == correctpassword:
    #     print("Welcome, admin")
    # else:
    #     print("You are not admin")

# 22. เขียนโปรแกรมเพื่อช่วยร้านอาหารคำนวณราคา โดย Japanese buffet ราคา 1000 บาท และ Korean
# buffet ราคา 1500 บาท ถ้าวันนี้เป็นวันพุธจะได้รับส่วนลด 15%

    # country = input("Enter your buffet choice: ")
    # day = input("s today Wednesday (yes/no): ")

    # price = 0
    # discount = 1

    # if country == "Korean":
    #     price = 1500
    #     if day == "yes":
    #         discount = 0.85
    # elif country == "Japanese":
    #     price = 1000
    #     if day == "yes":
    #         discount = 0.85

    # result = price * discount
    # print(f"Your payment is {result:.2f} baht")

# 23. ร้านขายเครื่องใช้ไฟฟ้าแห่งหนึ่ง นำเครื่องใช้ไฟฟ้าสามชนิดมาลดราคา ดังนี้
# - TV ราคา 6000 บาท
# - DVD player ราคา 1500 บาท
# - Audio System ราคา 3000 บาท
# ร้านค้ามอบส่วนลดพิเศษ 20% ให้กับลูกค้าที่มียอดซื้ออย่างน้อย 24,000 บาท
# จงเขียนโปรแกรมเพื่อรับจำนวนสินค้าแต่ละชนิดที่ลูกค้าจะซื้อ (เป็นจำนวนเต็มบวกหรือศูนย์) แล้ว
# คำนวณยอดซื้อ และแสดง ยอดซื้อรวม (total price) ส่วนลด (discount) ถ้ามี และ ราคาที่ต้องชำระ
# (payment) โดยราคาแสดงด้วยทศนิยม 2 ตำแหน่ง

    # tv = 6000
    # dvd = 1500
    # audio = 3000

    # tvinp = int(input("How many TVs: "))
    # dvdinp = int(input("How many DVD players: "))
    # audioinp = int(input("How many Audio System: "))

    # total = (tv * tvinp) + (dvd * dvdinp) + (audio * audioinp)
    # if total >= 24000:
    #     discountprice = total * 0.20
    #     newprice = total - discountprice

    #     print(f"Total price is {total:.2f} baht")
    #     print(f"You've got a discount of {discountprice:.2f} baht")
    #     print(f"Your payment is {newprice:.2f} baht")
    # else:
    #     print(f"Total price is {total:.2f} baht")
    #     print(f"Your payment is {total:.2f} baht")


"""unit11 while loop"""

# เขียนคำสั่งโดยใช้ลูป while เพื่อให้แสดงผลลัพธ์ต่อไปนี้ออกทางหน้าจอ
# 1. 1, 3, 5, 7, 9, 11, 13, 15,
    # i = 1
    # while i <= 15:
    #     print(i)
    #     i += 2

# 2. 2, 5, 8, 11, 14, 17,
    # i = 2
    # while i <= 17:
    #     print(i)
    #     i +=3

# 3. 30, 20, 10, 0, -10,-20, -30
    # i = 30
    # while i >= -30:
    #     print(i)
    #     i -= 10

# 4. 15, 23, 31, 39, 47, 55
    # i = 15
    # while i <= 55:
    #     print(i)
    #     i += 8

# 5. พิมพ์จำนวนเต็มตั้งแต่ 0 ถึง 100
# num = 0
# while True:
#     print(num)    
#     num += 1
#     if num > 100:
#         break


# 6. รับจำนวนเต็มบวกมา 1 จำนวน แล้วพิมพ์จำนวนเต็มตั้งแต่ 0 ถึง จำนวนเต็มบวกที่รับเข้ามา
# num = int(input())
# i = 0
# while i <= num:
#     print(i)
#     i += 1

# 7. พิมพ์จำนวนเต็มตั้งแต่ 100 ถึง 0
# num = 100
# while num >= 0:
#     print(num)
#     num -= 1

# 8. รับจำนวนเต็มบวกมา 1 จำนวน แล้วพิมพ์จำนวนเต็มตั้งแต่จำนวนเต็มบวกที่รับเข้ามา ถึง 0
# num = int(input())
# while num >= 0:
#     print(num)
#     num -= 1

# 9. รับข้อมูลเข้าจำนวนจริงบวกบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จำนวนจริงบวก แล้วหาผลบวกของจำนวนจริงบวกทั้งหมดที่รับเข้ามา
# total = 0
# while True:
#     num = float(input())
#     if num <= 0:
#         break
#     total += num
# print(total)

# 10. รับข้อมูลเข้าจำนวนจริงบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าเป็น 0 แล้วหาว่าจำนวนจริงที่รับเข้ามามีจำนวนจริงบวกกี่จำนวน และจำนวนจริงลบกี่จำนวน
# minustotal = 0
# plustotal = 0
# while True:
#     num = float(input())
#     if num == 0:
#         break
#     if num > 0:
#         plustotal += 1
#     elif num < 0:
#         minustotal += 1
# print(f"จำนวนลบ: {minustotal}")
# print(f"จำนวนบวก: {plustotal}")

# 11. รับข้อมูลเข้าจำนวนจริงบวกบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จำนวนจริงบวก แล้วหาค่าเฉลี่ยของจำนวนจริงบวกทั้งหมดที่รับเข้ามา
# countjamnuan = 0
# total = 0
# while True:
#     num = float(input())
#     if num <= 0:
#         break
#     total += num
#     countjamnuan += 1
# if countjamnuan > 0:
#     print(total/countjamnuan)

# 12. รับข้อมูลเข้าจำนวนจริงบวกบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จำนวนจริงบวก แล้วหาจำนวนจริงบวกที่มีค่ามากที่สุดจากจำนวนจริงบวกทั้งหมดที่รับเข้ามา
# box = []
# while True:
#     num = float(input())
#     if num <= 0:
#         break
#     box.append(num)
# if box:
#   print(max(box))

# 13. รับข้อมูลเข้าจำนวนจริงบวกบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จำนวนจริงบวก แล้วหาจำนวนจริงบวกที่มีค่าน้อยที่สุดจากจำนวนจริงบวกทั้งหมดที่รับเข้ามา
# box = []
# while True:
#     num = float(input())
#     if num <= 0:
#         break
#     box.append(num)
# if box:
#    print(min(box))

# 14. รับข้อมูลเข้าจำนวนจริงบวกบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จำนวนจริงบวก แล้วหาผลต่างของ จำนวนจริงบวกที่มีค่ามากที่สุด และจำนวนจริงบวกที่มีค่าน้อยที่สุด จากจำนวนจริงบวกทั้งหมดที่รับเข้ามาโดยใช้ Loop เดียว
# box = []
# while True:
#     num = float(input())
#     if num<=0:
#         break
#     box.append(num)
# if box:
#   print(max(box) - min(box))

# 15. รับข้อมูลเข้าจำนวนเต็มบรรทัดละจำนวน หยุดรับเมื่อข้อมูลเข้าเป็น -1 จากนั้นทำการหาผลรวมของข้อมูลที่รับเข้ามา
# total = 0
# while True:
#     num = int(input())
#     if num == -1:
#         break
#     total += num
# print(total)

# 16. เขียนโปรแกรมรับเลขจำนวนเต็มเข้ามา ถ้าเป็นเลขจำนวนเต็มบวกให้พิมพ์หลักเลขออกมาทีละหลักต่อ
# หนึ่งบรรทัด โดยเริ่มจากหลักที่มีค่าน้อยสุด (หลักหน่วย) ถ้ารับอินพุตเป็นเลข 0 หรือจำนวนเต็มลบ ให้พิมพ์คำว่า
# “ERROR”
    # num = int(input())

    # if num <= 0:
    #     print("ERROR")
    # else:
    #     # วนลูปเพื่อดึงเลขออกมาทีละหลักจากขวาสุด (หลักหน่วย)
    #     while num > 0:
    #         digit = num % 10  # ใช้การหาเศษด้วย 10 เพื่อดึงเลขหลักสุดท้ายออกมา
    #         print(digit)
    #         num = num // 10   # ใช้การหารตัดเศษด้วย 10 เพื่อตัดเลขหลักสุดท้ายทิ้งไป

# 17. เขียนโปรแกรมรับค่าจำนวนเต็มเข้ามาจนกว่าจะเป็นเลขติดลบ จากนั้นตรวจสอบว่ามีตัวเลขที่เป็นเลขคี่ทั้งหมดกี่จำนวน
    # counteven = 0
    # countodd = 0
    # while True:
    #     num = int(input())
    #     if num < 0:
    #         break
    #     if num % 2 == 0:
    #         counteven += 1
    #     else:
    #         countodd += 1

    # print(f"Received {countodd} odd numbers")

# 18. จำนวนเต็มบวกที่หารด้วย 9 ลงตัว ตรวจสอบได้โดยการนำผลบวกของเลขโดดในจำนวนเต็มบวก หาร
# ด้วย 9 ถ้าผลบวกนั้นหารด้วย 9 ลงตัว แสดงว่าจำนวนเต็มบวกนั้นหารด้วย 9 ลงตัว แต่ถ้าผลบวกนั้นหารด้วย 9 ไม่
# ลงตัว แสดงว่าจำนวนเต็มบวกนั้นจะหารด้วย 9 ไม่ลงตัว และเศษจากการหารผลบวกของเลขโดดด้วย 9 จะเท่ากับ
# เศษจากการหารจำนวนเต็มบวกด้วย 9 เช่นกัน
# เขียนโปรแกรมเพื่อรับจำนวนเต็มบวก 1 จำนวน แล้วตรวจสอบว่า จำนวนที่รับเข้ามาหารด้วย 9 ลงตัวหรือไม่ โดย
# ใช้กฎของเก้า ถ้าหารลงตัวให้แสดง “Yes” และผลบวกของเลขโดด แต่ถ้าหารไม่ลงตัวให้แสดง “No” และเศษ
# ของการหาร
# หมายเหตุ: ไม่อนุญาตให้ใช้ string หรือ list

num = int(input())

total = 0
while num > 0:
    total += num % 10
    num //= 10

if total % 9 == 0:
    print(f"Yes {total}")
else:
    print(f"No {total % 9}")











"""Unit 16 Lists"""
#  Method            Meaning
# append()          เพิ่มelement ไปที่ล าดับสุดท้ายของ list
# clear()           ลบ elementทั้งหมดใน list
# copy()            คัดลอก list
# count()           นับจ านวน element ใน list ด้วยค่าที่ระบุ
# extend()          เพิ่มelement(หลายตัว) ไปที่ล าดับสุดท้ายของ 
# list
# Index()           คืนค่าต าแหน่งของ element ใน list
# insert()          เพิ่ม element โดยอ้างอิงต าแหน่ง
# pop()             ลบ element โดยอ้างอิงต าแหน่ง
# remove()          ลบ element ด้วยค่าที่เจาะจง
# reverse()         กลับล าดับ element ใน list
# sort()            เรียงล าดับelement ใน list

# x = ["dog","cat","hamster",["horse","donkey"],"fish"]
# print(x)
# print(len(x))
# print(type(x))
# print(x[0])
# print(x[3][1])
# if "cat" in x:
#     print("yes")
# else:
#     print("no")

# x.append("bird")
# print(x)

# x.extend("wolf") # ใส่แบบแยก อันนี้จะได้ ['w', 'o', 'l', 'f']
# print(x)

# x.insert(1, "bird")
# print(x)

# x.remove("dog") # remove ให้ใส่ค่า
# print(x)

# x.pop(1) # pop ให้ใส่ตำแหน่ง
# print(x)

# del x[0] # ลบแบบหายไปตลอดกาล
# print(x)

#แปลง str ให้เป็น list แบบแยกตัว
# x = "kitty"
# y = list(x)
# print(y)
# >>>['k', 'i', 't', 't', 'y']

#แปลง str ให้เป็น list
# x1 = "cat"
# x2 = "cat dog bird"
# print(x1.split())
# print(x2.split())
# >>>['cat']
# >>>['cat', 'dog', 'bird']

# x = ['cat', 'dog', 'bird']
# for i in x:
#     print(i)
# >>>cat
# >>>dog
# >>>bird