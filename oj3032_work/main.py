"""kanansob"""

def main():
    """main"""
    n = int(input())
    num = []

    for _ in range(n):
        score = int(input())
        num.append(score)

    maximum = max(num)

    print(maximum)
    print(num.count(maximum))

main()
