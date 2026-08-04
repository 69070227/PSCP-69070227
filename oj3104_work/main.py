"""Ticket"""

age_input, day_input = input().split()

age = int(age_input)
day = day_input

def get_ticket_price():
    """"Return ticket price by age."""
    if age < 5:
        return 0
    if age <= 18:
        return 100
    return 150

TICKET_PRICE = get_ticket_price()

if day =="Wed":
    print(TICKET_PRICE // 2)

else:
    print(TICKET_PRICE)
