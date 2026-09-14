"""Electric_Using"""

nuai = int(input())
total = 0
# บาทต่อหน่วย
for i in range(1,nuai + 1):
    if 1 <= i <=10:
        total += 5
    elif 11 <= i <= 50:
        total +=7
    elif 51 <= i <= 100:
        total +=10
    elif 101 <= i <= 200:
        total +=12
    elif 201 <= i:
        total +=15

ft = nuai * 0.50
VAT = total * 0.07
result = total + VAT + ft
result += 0.000000001
print(f"{result:.1f}")
