"""test"""
n, m = map(int,input().split())

a = input().split()
b = input().split()
count = 0

for i in range(max(n,m)):
    if a[i] in b:
        count += 1

print(count)
