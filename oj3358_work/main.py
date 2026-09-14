"""Pig"""

n_pair = int(input())
num_pigs = n_pair * 2
pigs_weight = input().split()
total = 0
big_list = []

if n_pair == 1:
    print(max(pigs_weight))
else:
    for index in range(0,num_pigs,2):
        first_pig = int(pigs_weight[index])
        second_pig = int(pigs_weight[index + 1])

        bigger = max(first_pig,second_pig)
        total += bigger
        big_list.append(str(bigger))

        symbols = " + ".join(big_list)

    print(f"{symbols} = {total}")
