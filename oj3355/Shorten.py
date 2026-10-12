"""Shorten"""
box = []

while True:
    num = int(input())

    if num == -1:
        break

    box.append(num)

result = []

# กรณี -1 มาตั้งแต่แรก
if not box:
    print("")
else:
    start = box[0]

    for i in range(len(box) - 1):
        if box[i + 1] - box[i] != 1:
            end = box[i]

            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "-" + str(end))

            start = box[i + 1]

    end = box[-1]

    if start == end:
        result.append(str(start))
    else:
        result.append(str(start) + "-" + str(end))

    print(", ".join(result))
