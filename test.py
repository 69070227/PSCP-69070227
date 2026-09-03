"""aegega"""

letter = input().upper()
kanat = int(input())

#จากที่ลองทด แถวจะเป็น 1 3 5 7 9 11 ไปเรื่อยๆ บวกสอง
taew = (kanat * 2) - 1  
# หาจุดกึ่งกลางของลูกศร (ถ้า taew=9, target=4)
target = taew // 2

if letter == "R":
    #ครึ่งแรก
    for i in range(kanat):
        space = i * 2
        num_rieang_bon = kanat - i
        print(" " * space + "*" * num_rieang_bon)
    
    for i in range(kanat - 1):
        space = (abs((taew // 2)- i) - 1) * 2 
        num_rieang_lang = i + 2
        print(" " * space + "*" * num_rieang_lang)


elif letter == "L":
    for i in range(kanat):
            space = (abs((taew // 2)- i)) * 2
            num_rieang_lang = i + 1
            print(" " * space + "*" * num_rieang_lang)
    for i in range(kanat - 1):
            space = (i + 1) * 2
            num_rieang_bon = kanat - i - 1
            print(" " * space + "*" * num_rieang_bon)
