"""test"""
inp = input()
box = []
box.append(inp)

while inp != "NULL":
    inp = input()
    box.append(inp)
for i in box[::-1]:
    if i == "NULL":
        continue
    print(i)
