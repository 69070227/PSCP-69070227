"""[LEARNING LOGS] เกมสะสมแต้ม"""

N = int(input())
result = 0
for i in range(N):
    i = i+i-i
    symbol = input()
    if symbol =="+":
        result += 10
    elif symbol =="-":
        result -=5

print(result)
