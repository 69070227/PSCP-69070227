"""Duplicate I"""

try:
    m = int(input())
    n = int(input())

    group1 = []
    for _ in range(m):
        group1.append(input().strip())

    group2 = []
    for _ in range(n):
        group2.append(input().strip())
except EOFError:
    pass

both = []
for code in group1:
    if code in group2 and code not in both:
        both.append(code)

if not both:
    print("Nope")
else:
    both.sort(reverse=True)
    for code in both:
        print(code)
