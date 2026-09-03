letter = input().upper()
kanat = int(input())

# จำนวนแถวทั้งหมดของลูกศร
taew = (kanat * 2) - 1

if letter == "R":
    for i in range(taew):
        if i < kanat:
            # ครึ่งบน: ช่องว่างเพิ่มทีละ 2, ดอกจันลดทีละ 1
            space = i * 2
            num_stars = kanat - i
        else:
            # ครึ่งล่าง: ช่องว่างลดทีละ 2, ดอกจันเพิ่มทีละ 1
            space = (taew - 1 - i) * 2
            num_stars = i - kanat + 2
            
        print(" " * space + "*" * num_stars)

elif letter == "L":
    for i in range(taew):
        if i < kanat:
            # ครึ่งบน: ช่องว่างลดทีละ 1, ดอกจันลดทีละ 1
            space = kanat - 1 - i
            num_stars = kanat - i
        else:
            # ครึ่งล่าง: ช่องว่างเพิ่มทีละ 1, ดอกจันเพิ่มทีละ 1
            space = i - kanat + 1
            num_stars = i - kanat + 2
            
        print(" " * space + "*" * num_stars)
