from itertools import combinations


digits = [0, 1, 2, 3, 4]
combinations_list = []
combinations_list.extend(combinations(digits, 3))
combinations_list.extend(combinations(digits, 2))

def all_col_combo(num = 5 ):
    combinations_list = []
    for i in range(1, num):
        # print(i)
        combinations_list.extend(combinations(digits,i))
    return combinations_list

# print(all_col_combo(5))


