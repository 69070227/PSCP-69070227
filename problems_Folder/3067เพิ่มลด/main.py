"""การเพิ่ม/ลด"""

def main():
    """diff"""
    NUM_1 = float(input())
    NUM_2 = float(input())
    NUM_3 = float(input())

    if NUM_1 < NUM_2 < NUM_3:
        print("increasing")
    elif NUM_1 > NUM_2 > NUM_3:
        print("decreasing")
    else:
        print("neither")
main()
