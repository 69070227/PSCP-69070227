"""จำนวนสระ"""

def main():
    """ฟางช่านนนนนนนนนนนนนน"""
    num = int(input())
    list_letter = []
    count = 0

    #รับค่าตามตัวเลขที่ใส่มา
    for i in range(num):
        letters = input().capitalize()
        list_letter.append(letters)

    #เช็คเงื่อนไขว่าตัวที่ตำแหน่งนี้มี a e i o u ไหม
    for i in range(num):
        if list_letter[i] in ("A", "E", "I", "O", "U"):
            count +=1

    print(count)
main()
