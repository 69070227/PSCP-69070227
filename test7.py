"""wfj"""

seat = int(input())
discount = 1
list_ticket = []
while seat > 0:
    age,amount = map(int,input().split())
    if age >= 15:
        ticket = 150
    elif 15 <= age <=22:
        discount = 0.20
    elif age > 60:
        discount = 0.50
    else:
        result = -1
    result = (ticket * amount)*discount
    seat -= amount
    
    print(result,amount)