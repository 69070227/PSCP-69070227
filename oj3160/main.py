"""[LEARNING LOGS] หาจำนวนเฉพาะ"""

start, stop =map(int,(input()).split())

for i in range(start,stop + 1):
    start_i = 2
    if not i / start_i :
        result = "notjamnuan_chapor"
    else:
        result = "isjamnuan_chapor"


print(result)
















