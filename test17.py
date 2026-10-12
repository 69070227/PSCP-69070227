"""test"""

jamnuan = int(input())
for i in range(jamnuan):
    plastic, can, glass = map(float, input().split())
    total = plastic + can + glass
    print(f"{total:.2f}", end="")
    if total > 50:
        print(", Overload", end="")
        if plastic > 20:
            print(", Check Type Plastic", end="")
        if can > 20:
            print(", Check Type Can", end="")
        if glass > 20:
            print(", Check Type Glass", end="")
    print()