"""conan"""

text_input = input().casefold()
k = int(input())

result = ""

for char in text_input:
    #ตั้งค่าให้ a เริ่มที่ 0 ทีแรกใน ASII a จะเท่ากับ97 จากนั้นไล่เสต็ปด้วยการบวกค่า k
    #วนกลับมาที่ 'a'อัตโนมัติด้วย % 26 ถ้าหารแล้วเหลือเศษก็เอาเศษเป็นตำแหน่งของตัวอักษร
    #+97เพื่อให้มันอ่านแบบ ASII อีกครั้ง
    new_char = chr(((ord(char) - 97 + k) % 26) + 97)
    result += new_char

print(result)
