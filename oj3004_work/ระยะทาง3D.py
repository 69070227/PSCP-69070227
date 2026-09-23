"""ระยะทาง3D"""

import math

def main():
    """main"""
    input_1 = input()
    input_2 = input()

    tuaplae_1 = input_1.split()
    tuaplae_2 = input_2.split()
    x1 = int(tuaplae_1[0])
    y1 = int(tuaplae_1[1])
    z1 = int(tuaplae_1[2])

    x2 = int(tuaplae_2[0])
    y2 = int(tuaplae_2[1])
    z2 = int(tuaplae_2[2])

    DISTANCE = math.sqrt(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))
    print(f"{DISTANCE:.2f}")

main()
