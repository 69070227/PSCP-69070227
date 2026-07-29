"""เหมือนกันหมด"""

def main():
    """diff"""
    NUM_1 = int(input())
    NUM_2 = int(input())
    NUM_3 = int(input())

    if (NUM_1 == NUM_2) and (NUM_1 == NUM_3) and (NUM_2 == NUM_3):
        print("all the same")
    elif (NUM_1 != NUM_2) and (NUM_1 != NUM_3) and (NUM_2 != NUM_3):
        print("all different")
    else:
        print("neither")
main()
