"""test"""

n = int(input())

inp = input()
box = inp.split()

for i in box:
    if box.count(i) < 1:
        print(i,end="")
    else:
        pass
print()





# """test"""

# s = input()

# for low in "abcdefghijklmnopqrstuvwxyz":
#     up = low.upper()

#     if s.count(low) > 0:
#         print(low, "=", s.count(low))
#     if s.count(up) > 0:
#         print(up, "=", s.count(up))
