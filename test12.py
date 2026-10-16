"""บุพเพสันนิวาส"""


def main():
    """ฟางช่านนนนน"""
    a = input().strip()
    b = input().strip()

    if len(a) > len(b):
        diff = len(a) - len(b)
        b += b[0] * diff
    elif len(b) > len(a):
        diff = len(b) - len(a)
        a += a[0] * diff

    r = ""
    w_count = 0

    for c1, c2 in zip(a, b):
        if c1.lower() in "love" or c2.lower() in "love":
            r += "w"
            w_count += 1
        else:
            r += "$"

    if w_count % 2:
        max_consecutive = 0
        current_consecutive = 0
        for char in r:
            if char == "w":
                current_consecutive += 1
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
            else:
                current_consecutive = 0
        r += str(max_consecutive)
    else:
        has_consecutive_w = "ww" in r
        if not has_consecutive_w:
            r += "#"

    print(r)


if __name__ == "__main__":
    main()
