"""Basic ATM"""

def main():
    """main"""
    N = int(input())
    #N % 100 != 0 → หาร 100 ไม่ลงตัว (มีเศษ) (N % 100 ถ้าหารลงตัวจะได้ 0 = false)
    if 100 > N or 20000 < N or N % 100:
        print("ERROR")
    else:
        pan_baht = N // 1000
        left = N % 1000
        haroi_baht = left // 500
        left = left % 500
        roi_baht = left // 100
        left = left % 100

        if pan_baht: #ถ้าหากเป็น 0 จะข้ามไม่ทำอันข้างล่าง
            print(f"1000 = {pan_baht}")
        if haroi_baht: #ถ้าหากเป็น 0 จะข้ามไม่ทำอันข้างล่าง
            print(f"500 = {haroi_baht}")
        if roi_baht: #ถ้าหากเป็น 0 จะข้ามไม่ทำอันข้างล่าง
            print(f"100 = {roi_baht}")

main()
