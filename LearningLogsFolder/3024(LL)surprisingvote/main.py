"""surp"""
all_three = float(input())
most_num = float(input())

left_num = all_three - most_num
min_num = max(0, left_num - most_num)
diff = most_num - min_num
if diff > 2:
    print("Surprising")
else:
    print("Not surprising")
