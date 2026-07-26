"""[LEARNING LOGS] ปราสาท"""

def main():
    """main"""
    x = int(input())
    floor = 1
    while floor **2 < x:
        floor += 1
    far = (floor **2) - x
    room = 2*(floor) - 1 #ใช้หาจำนวนห้องทั้งหมดในชั้นนั้นเป็นเลขคี่
    if not far % 2:
        print(room - 1) #เลขคู่
    else:
        print(room - 2) #เลขคี่

main()
