"""นวัตกรรมงบประมาณโรงเรียน"""

def main():
    """ASCII คือ รหัสตัวเลขแทนตัวอักษร ดังนั้นใช้ฟังก์ชัน ord() ในการแปลงจากตอศ.เป็นตัวเลข"""
    school_input = input()

    first_ASCII = ord(school_input[0].upper())
    last_ASCII = ord(school_input[-1].upper())

    length = len(school_input)
    list_ascii = []


    for i in range(1,11):
        place_value = i - 1
        if i % 2 :
            value = first_ASCII + place_value
        else:
            value = last_ASCII - place_value

        rem = value % length
        if rem > 9:
            rem = rem % 10

        list_ascii.append(rem)

    middle_6 = list_ascii[2:8]

    print(" ".join(map(str, middle_6)))

main()
