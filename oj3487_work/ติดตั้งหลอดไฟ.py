"""lord faiiiiii"""
def lordfai():
    """fangchan"""
    n = int(input())
    poles = [int(input()) for _ in range(n)]

    # เรียงลำดับความสูงของเสาจากน้อยไปมาก
    poles.sort()

    current_height_sum = 0
    total_distance = 0

    for height in poles:
        current_height_sum += height
        total_distance += current_height_sum * 2

    print(total_distance)


lordfai()
