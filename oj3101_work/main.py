"""สถานะน้ำ"""

temp_num = int(input())
temp_unit = input()
result = ""

if temp_unit in ("c", "C"):
    if temp_num <= 0:
        result = "solid"
        print(result)
    elif temp_num == 100:
        result ="gas"
        print(result)
    elif 0 < temp_num < 100:
        result ="liquid"
        print(result)


elif temp_unit in ("f", "F"):
    if temp_num <= 32:
        result = "solid"
        print(result)
    elif temp_num == 212:
        result ="gas"
        print(result)
    elif 32 < temp_num < 212:
        result ="liquid"
        print(result)
