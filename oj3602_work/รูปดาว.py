"""test"""
n = int(input())

print("*" * n)
print("*" * (n - 2) if n - 2 >= 1 else "")
print("*" * (n - 4) if n - 4 >= 1 else "")
