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

    # num = int(input())
    # syms1 = input()
    # syms2 = input()

    # if num % 2 ==0:
    #     result = (syms1 + syms2) * int(num / 2)

    #     print(result)
    # else:
    #     result = (syms1 + syms2) * int(num / 2)
        
    #     print(result + syms1)

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
# s = (u * t) + ((1/2) * (a * t)**2)
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

a = int(input("a = "))
b = int(input("b = "))

reverse_a = a
a = b
b = reverse_a

print(f"a = {a}")
print(f"b = {reverse_a}")