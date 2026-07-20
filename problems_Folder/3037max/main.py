"""MAX"""

def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    maximum = 0
    if num3 > num2 and num3 > num1:
        maximum = num3
    elif num2 > num3 and num2 > num1:
        maximum = num2
    elif num1 > num3 and num1 > num2:
        maximum = num1
    elif num1 == num3 and num1 == num2:
        maximum = num1
    elif num1 > (num2 == num3):
        maximum = num1
    elif num2 > (num1 == num3):
        maximum = num2
    elif num3 > (num1 == num2):
        maximum = num3

    print(maximum)
main()
