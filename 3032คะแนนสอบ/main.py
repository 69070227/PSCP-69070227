"""kanansob"""

def main():
    """main"""
    n = int(input())
    num = []

    for _ in range(n):
        score = int(input())
        num.append(score)
    print(max(num))
    print(num.count(max(num)))

main()
