"""seven"""

x = int(input())
number = x% 4
RESULT = 0
if number==1:
    RESULT = 7
elif number==2:
    RESULT = 9
elif number==3:
    RESULT = 3
elif not number:
    RESULT = 1

print(RESULT)
