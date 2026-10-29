"""test"""

while True:
    inp = input()
    total = 0

    if inp == "0":
        break
    while len(inp) != 1:
        for i in range(len(inp)):
            total += int(inp[i])

    print(total)
        

