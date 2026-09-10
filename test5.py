"""test"""
salak_result = list(input().strip())
salak_rabit = list(input().strip())

count = 0
#letter_result
letter_result = (salak_result[0]).upper()
letter_rabbit = (salak_rabit[0]).upper()

if letter_result == letter_rabbit:
    for i in range(2, 7):
    # ดึงค่าตำแหน่งที่ i ของทั้งสองลิสต์มาเทียบกัน
        if salak_rabit[i] == salak_result[i]:
            count += 1

    if count == 5:
        print("1000000")
    # สามตัวท้าย ต้องหาเลขท้ายที่มากกว่าก่อน ไม่งั้นจะไปเข้าเงื่อนไขสองตัวท้ายก่อน
    elif salak_result[4:7] == salak_rabit[4:7]:
        print("2000")
    # สองตัวท้าย
    elif salak_result[5:7] == salak_rabit[5:7]:
        print("1000")
    elif not count:
        print("20")

elif letter_result != letter_rabbit:
    for i in range(2, 7):
        if salak_rabit[i] == salak_result[i]:
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
