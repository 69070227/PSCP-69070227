"""test"""

seat = int(input())

TICKET_PRICE = 150
discount = 1
total = 0
while seat > 0:

    age, tickets = map(int, input().split())

    if age < 15:
        print(-1)
    elif tickets > seat:
        print(-2)
    else:
        seat -= tickets

        if 15 <= age <= 22:
            discount = 0.80
            total = (TICKET_PRICE * tickets) * discount
            print(f"{int(total)} {seat}")
        elif age >= 60:
            discount = 0.50
            total = (TICKET_PRICE * tickets) * discount
            print(f"{int(total)} {seat}")
        else:
            discount = 1
            total = (TICKET_PRICE * tickets) * discount
            print(f"{int(total)} {seat}")
