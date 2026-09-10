"""[LEARNING LOGS] กบน้อยกระโดด"""

can_jump,finish = map(int,input().split())
count = 0
current = 0

if finish > can_jump:
    while current < finish and can_jump > 0:
        current += can_jump
        count += 1
        can_jump -= 2
        if current >= finish:
            print(count)
        else:
            print("-1")
elif finish == can_jump:
    print("1")
