"""Bread Slicing"""

w, h, _, _ = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

xs = [0] + xs + [w]
ys = [0] + ys + [h]

widths = []
for i in range(len(xs) - 1):
    widths.append(xs[i + 1] - xs[i])

heights = []
for i in range(len(ys) - 1):
    heights.append(ys[i + 1] - ys[i])

widths.sort(reverse=True)
heights.sort(reverse=True)

# ตัวเลือกพื้นที่ที่เป็นไปได้สำหรับอันดับ 1 และ 2
areas = [widths[0] * heights[0]]

if len(widths) > 1:
    areas.append(widths[1] * heights[0])
if len(heights) > 1:
    areas.append(widths[0] * heights[1])

areas.sort(reverse=True)
print(areas[0], areas[1])
