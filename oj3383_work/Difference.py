"""Difference"""

n = int(input())
m = int(input())

set_a = set()
set_b = set()

for i in range(n):
    inp_a = int(input())
    set_a.add(inp_a)
for i in range(m):
    inp_b = int(input())
    set_b.add(inp_b)

AnotB = set_a - set_b
print(*sorted(AnotB))
