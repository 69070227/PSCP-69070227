"""สลับหมายเลข"""
number = input()
reverse = int(number[::-1])
symbol = input()
if 10 <= int(number) <= 99:
    if symbol == "+":
        result = int(number) + int(reverse)
        print(f"{number} {symbol} {reverse} = {result}")
    elif symbol =="*":
        result = int(number) * int(reverse)
        print(f"{number} {symbol} {reverse} = {result}")
    else:
        print("ERROR")
else:
    print("ERROR")
