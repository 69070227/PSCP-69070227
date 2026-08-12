"""วิเคราะห์ยอดขายร้านกาแฟ"""

num_days = int(input())
list_coffee = []

for i in range(num_days):
    i=i+i-i

    coffee_perday = int(input())
    list_coffee.append(coffee_perday)

print(sum(list_coffee))
print(max(list_coffee))
print(min(list_coffee))

average_daily = sum(list_coffee) / num_days
print(f"{average_daily:.1f}")
