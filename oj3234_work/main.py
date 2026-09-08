"""ไฟคริสตมาส"""

letter,numbers = input().upper().split()
numbers = int(numbers)
color_list = ["Red", "Green","Blue"]

for i in range(numbers):
    if letter == "R":
        index = (0 + i) % 3
        print(color_list[index],end = " ")
    elif letter == "G":
        index = (1 + i) % 3
        print(color_list[index],end = " ")
    elif letter == "B":
        index = (2 + i) % 3
        print(color_list[index],end = " ")
