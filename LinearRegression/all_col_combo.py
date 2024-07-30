from itertools import combinations


digits = [0, 1, 2, 3, 4]
combinations_list = []
combinations_list.extend(combinations(digits, 3))
combinations_list.extend(combinations(digits, 2))

def all_col_combo(col_num = 5, comb = 5 ):
    dig = [x for x in range(col_num)]
    # print(dig)
    combinations_list = []
    for i in range(1, comb):
        # print(i)
        combinations_list.extend(combinations(dig,i))
    return combinations_list

# print(all_col_combo(5))
# print(all_col_combo(6))
# print(all_col_combo(6,4))


