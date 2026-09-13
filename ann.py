"""[LEARNING LOGS] สลากกินแบ่ง"""


def main():
    """aeghaj"""
    winning_number = input().split()
    rabbit_lott = input().split()

    if rabbit_lott[0] == winning_number[0] and rabbit_lott[1] == winning_number[1]:
        print(1000000)
    elif rabbit_lott[1] == winning_number[1]:
        print(100000)
    elif rabbit_lott[0] == winning_number[0] and rabbit_lott[1][-3:] == winning_number[1][-3:]:
        print(2000)
    elif rabbit_lott[0] == winning_number[0] and rabbit_lott[1][-2:] == winning_number[1][-2:]:
        print(1000)

    elif rabbit_lott[0] != winning_number[0] and rabbit_lott[1][-3:] == winning_number[1][-3:]:
        print(200)
    elif rabbit_lott[0] != winning_number[0] and rabbit_lott[1][-2:] == winning_number[1][-2:]:
        print(100)
    elif rabbit_lott[0] == winning_number[0]:
        print(20)
    else:
        print(0)


main()
