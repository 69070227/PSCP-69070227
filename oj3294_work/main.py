"""Teaching schedule"""

class_N = int(input())
minutes = int(input())

total = class_N * minutes

remains_min = total % 60 # หาว่า หาร 60 จะเหลือเศษเท่าไหร่ เศษนั้นคือนาทีที่เหลือ
total_hour = total // 60 # หาว่า หาร 60 ได้กี่ชั่วโมง โดยไม่เอาเศษ

if not total_hour and remains_min > 0:
    print(f"{remains_min} minute")
elif not remains_min and total_hour > 0:
    print(f"{total_hour} hours")
elif remains_min > 0 and total_hour > 0:
    print(f"{total_hour} hours {remains_min} minute")
elif not total_hour and not remains_min:
    print("No teaching")
