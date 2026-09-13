"""test"""
salak_result = list(input().strip())
salak_rabit = list(input().strip())

count = 0
#letter_result
letter_result = (salak_result[0]).upper()
letter_rabbit = (salak_rabit[0]).upper()

if letter_result == letter_rabbit:
    for index,i in enumerate(salak_rabit[2:7], start = 2):
        if i == salak_result[index]:
            count += 1

    if count == 5:
        print("1000000")
    # สามตัวท้าย ต้องหาเลขท้ายที่มากกว่าก่อน ไม่งั้นจะไปเข้าเงื่อ
    elif salak_result[4:7] == salak_rabit[4:7]:
        print("2000")
    # สองตัวท้าย
    elif salak_result[5:7] == salak_rabit[5:7]:
        print("1000")
    elif not count:
        print("20")

elif letter_result != letter_rabbit:
    for index,i in enumerate(salak_rabit[2:7], start = 2):
        if i == salak_result[index]:
            count += 1

    if count == 5:
        print("100000")
    # สามตัวท้าย
    elif salak_result[4:7] == salak_rabit[4:7]:
        print("200")
    # สองตัวท้าย
    elif salak_result[5:7] == salak_rabit[5:7]:
        print("100")
    elif not count:
        print("0")
