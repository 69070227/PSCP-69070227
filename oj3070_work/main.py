"""นับเลขคู่และเลขคี่"""

NUM_1 = int(input())
NUM_2 = int(input())
NUM_3 = int(input())
EVEN = 0
ODD = 0
def is_even(x):
    """check is even or not"""
    if not x % 2:
        return True

    return False

if is_even(NUM_1):
    EVEN +=1
else:
    ODD +=1
if is_even(NUM_2):
    EVEN +=1
else:
    ODD +=1
if is_even(NUM_3):
    EVEN +=1
else:
    ODD +=1

print(EVEN)
print(ODD)
