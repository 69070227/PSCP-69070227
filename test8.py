"""test"""

seat = int(input())
age_list = []
tickets_list = []

tickets_price = 150
discount = 1
total = 0
while seat > 0:
    age,tickets = map(int,input().split())

    age_list.append(age)
    tickets_list.append(tickets)
    if tickets > seat:
        print(-2)
    else:
        seat -= tickets

#len จำนวนสมาชิกใน list
for i in range(len(age_list)):

    if age_list[i] < 15:
        print(-1)
    if 15 <= age_list[i] <= 22:
        discount = 0.80
        total = (tickets_price * tickets_list[i]) * discount
        print(total)
    elif age_list[i] >= 60:
        discount = 0.50
        total = (tickets_price * tickets_list[i]) * discount
        print(total)
    else:
        discount = 1
        total = (tickets_price * tickets_list[i]) * discount
        print(total)
