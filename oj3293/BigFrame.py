"""[LEARNING LOGS] BigFrame"""
text = []

#รับมาห้าบรรทัด
for i in range(5):
    #strip  ตัดช่องว่าง
    inp = input().strip()
    text.append(inp)

max_text = 0
for i in text:
    if len(i) > max_text:
        max_text = len(i)

top_bottom_sign = "*" * (max_text + 4)

print(top_bottom_sign)

for i in text:
    print(f"* {i:<{max_text}} *")

print(top_bottom_sign)
