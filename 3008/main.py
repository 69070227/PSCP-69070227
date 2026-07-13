"""Heron of Alexandria"""
import math

def main():
    """main"""
    a = float(input())
    b = float(input())
    c = float(input())
    if (a != 0) and (b != 0) and (c != 0):
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(float(f"{area:.3f}"))

main()
