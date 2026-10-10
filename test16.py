"""test"""
boy = 0
girl = 0
while True:
    key = input()
    lastdigit = key[-1]
    if int(key) < 0:
        break
    if lastdigit in ("1","3","5","7","9"):
        boy += 1
    elif lastdigit in ("0","2","4","6","8"):
        girl += 1

print(f"{boy} {girl} {boy + girl}")
