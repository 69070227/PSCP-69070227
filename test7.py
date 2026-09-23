"""สมดุลย์ชีวิต"""

work = int(input())
hard_work = []
light_work = []
DAYS = 0
for _ in range(work):
    hour_each = int(input())
    if hour_each > 18:
        hard_work.append(hour_each)
    elif hour_each <= 18:
        light_work.append(hour_each)

if len(light_work) >= len(hard_work):
    DAYS = len(hard_work) + len(light_work)

elif len(light_work) < len(hard_work):
    # ลบหนึ่งเพราะว่าหาแค่ตัวระหว่าง
    WAN_YUD =  len(hard_work) - len(light_work) - 1
    DAYS = len(hard_work) + len(light_work) + WAN_YUD

print(DAYS)
