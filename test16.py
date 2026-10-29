"""test"""
total_animals = int(input())
total_leg = int(input())

if total_leg % 2 == 1 or total_leg < 2 * total_animals or total_animals > 4 * total_leg:
    print("Impossible")
else:
    rabbit = (total_leg - 2 * total_animals) // 2
    bird = total_animals - rabbit
    print(f"{rabbit} {bird}")
