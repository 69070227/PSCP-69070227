"""Safe Password"""

USER_CHAR = input()
USER_NUM = input()

CORRECT_CHAR = "H"
CORRECT_NUM = "4567"

if USER_CHAR != CORRECT_CHAR and  USER_NUM == CORRECT_NUM:
    print("safe locked - change char")
elif USER_CHAR == CORRECT_CHAR and  USER_NUM != CORRECT_NUM:
    print("safe locked - change digit")
elif USER_CHAR == CORRECT_CHAR and  USER_NUM == CORRECT_NUM:
    print("safe unlocked")
else:
    print("safe locked")
