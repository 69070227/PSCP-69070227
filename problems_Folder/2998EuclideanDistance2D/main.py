"""EuclideanDistance2D"""

import math

def main():
    """main"""
    q1 = round(float(input()),2)
    q2 = round(float(input()),2)
    p1 = round(float(input()),2)
    p2 = round(float(input()),2)

    DISTANCE = math.sqrt(((q1-p1)**2)+((q2-p2)**2))
    print(DISTANCE)

main()
