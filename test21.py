"""test"""
push_count = 0
satana = False
while True:
    kamsang = input()
    if kamsang == "END":
        break

    if kamsang == "C":
        satana = True
    elif satana == True and kamsang == "P":
        push_count += 1
        satana =False

print(push_count)
