"""Day08-0_02-Backward"""
box = []
while True:
    inp = input()
    if inp == "NULL":
        break
    box.append(inp)
for i in box[::-1]:
    print(i)
