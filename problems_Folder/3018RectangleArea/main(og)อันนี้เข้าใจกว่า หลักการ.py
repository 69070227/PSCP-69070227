"""RectangleArea"""

def main():
    """recsolu"""
    xA,yA,widthA,heightA = map(int,(input().split()))
    xB,yB,widthB,heightB = map(int,(input().split()))

    #มุมสี่เหลี่ยมของ A
    leftA = xA
    rightA = xA + widthA
    bottomA = yA
    topA = yA + heightA

    #มุมสี่เหลี่ยมของ B
    leftB = xB
    rightB = xB + widthB
    bottomB = yB
    topB = yB + heightB

    overlap_left = max(leftA,leftB)
    overlap_right = min(rightA,rightB)

    overlap_top = min(topA,topB)
    overlap_bottom = max(bottomA,bottomB)

    solu_width = overlap_right - overlap_left
    solu_height = overlap_top - overlap_bottom

    if solu_width > 0 and solu_height > 0:
        print(solu_height * solu_width)
    else:
        print("no overlapping")

main()
