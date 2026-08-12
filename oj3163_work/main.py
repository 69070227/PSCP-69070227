"""สินค้าส่งออก"""

SUM = int(input())
even_amount = 0
odd_amount = 0
num_list = []
for i in range(SUM):
    i=i+i-i
    number = int(input())
    if not number % 2:
        even_amount +=1
        num_list.append(number)
    else:
        odd_amount +=1
        num_list.append(number)


result = sum(num_list)

print(f"SUM {result}")
print(f"EVEN {even_amount}")
print(f"ODD {odd_amount}")
