"""นวัตกรรมงบประมาณโรงเรียน"""

def main():
    """ASCII คือ รหัสตัวเลขแทนตัวอักษร ดังนั้นใช้ฟังก์ชัน ord() ในการแปลงจากตอศ.เป็นตัวเลข"""
    school_input = input()

    first_letter = school_input[0].upper()
    last_letter = school_input[-1].upper()

    length = len(school_input)
    list_ascii = []


    ASCII_first = ord(first_letter)
    ASCII_last = ord(last_letter)

    for i in range(1,11):
        place_value = i - 1
        if i % 2 != 0 :
            value = ASCII_first + place_value
            list_ascii.append(value)
        else:
            value = ASCII_last - place_value
            list_ascii.append(value)

    rem = value % length
    if rem > 9:
        rem = rem % 10

        list_ascii.append(rem)

    middle_6 = list_ascii[2:8]

    print("".join(map(str, middle_6)))

main()
