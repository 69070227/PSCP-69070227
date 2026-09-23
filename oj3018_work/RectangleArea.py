"""RectangleArea"""

def main():
    """recsolu"""
    xa_pos, ya_pos, width_a, height_a = map(int, input().split())
    xb_pos, yb_pos, width_b, height_b = map(int, input().split())

    # หาจุดเริ่มและจุดจบของพื้นที่ที่ซ้อนทับกัน (ใช้สูตรบวกความกว้าง/สูงตรงนี้เลย)
    overlap_left = max(xa_pos, xb_pos)
    overlap_right = min(xa_pos + width_a, xb_pos + width_b)

    overlap_bottom = max(ya_pos, yb_pos)
    overlap_top = min(ya_pos + height_a, yb_pos + height_b)

    # คำนวณความกว้างและความสูงที่ซ้อนทับกัน
    overlap_w = overlap_right - overlap_left
    overlap_h = overlap_top - overlap_bottom

    # ตรวจสอบเงื่อนไขและแสดงผล
    if overlap_w > 0 and overlap_h > 0:
        print(overlap_w * overlap_h)
    else:
        print("no overlapping")

main()
