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


# 1. #Name = "ผิด" # เพราะมีตัวพิเศษ
# 2. True = "ผิด" # เพราะเป็นค่าbooleen
# 3. name = "ถูก"
# 4. return = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# 5. first name = "ผิด" # เพราะมีการเว้น space
# 6. first_name = ถูก"
# 7. “haha” = "ผิด" # เพราะมี double quoat
# 8. 15 = "ผิด" # เพราะเป็นตัวเลข
# 9. 1ion = "ผิด" # เพราะมีตัวเลขข้างหน้าสุด
# 10. gr@de = "ผิด" # เพราะมีตัวพิเศษ
# 11. if = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# 12. while = "ผิด" # เพราะเป็นคำสงวน เป็นฟังก์ชัน
# 13. [b] = "ผิด" # เพราะมี []
# 14. _name = "ถูก"
# 15. pyThon = "ถูก"

# C = int(input())
# f = ((9/5)*(C)) + 32
# k = C + 273.15
# print(f"{f} {k}")

# base = float(input())
# height = float(input())
# print(f"{((1/2)*base*height):.6f}")

"""บทที่ 6 data types"""


# 1. เกรดเฉลี่ยของนักเรียน รับเป็น#float เพราะ หารแล้วจะได้ทศนิยมเสมอ
# 2. อายุของนักศึกษา รับเป็น#int เพราะ อายุนับเป็นจำนวนเต็ม
# 3. ชื่อผู้ใช้งานระบบ รับเป็น#string เพราะ เป็นชื่อ
# 4. เงินเดิอนสะสมรายปีของพนักงาน รับเป็น#int เพราะเป็นเลข
# 5. รหัสบัตร ATM รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# 6. รหัสประจำตัวประชาชน รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# 7. หมายเลขโทรศัพท์มือถือ รับเป็น str เพราะอาจมีเลข 0 ข้างหน้า คอมจะตัด 0 อัตโนมัตืถ้าเป็น int 
# 8. พื้นที่ของวงกลม รับเป็น float เพราะเป็นเลขที่คูณด้วย 3.14
# 9. น้ำหนัก รับเป็น float เพราะมีทศนิยมได้
# 10. ราคาสินค้า รับเป็น float เพราะอาจมีสตางค์

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


w = float(input("Enter width:"))
l = float(input("Enter length:"))
d = float(input("Enter depth:"))
volumn = w * l * d  # กว้าง x ยาว x ลึก
total_minute = (volumn * 15)/60
print(f"Time to fill a pool is {total_minute:.2f} minutes.")

