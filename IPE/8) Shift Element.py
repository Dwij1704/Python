def shift_left(lst):
    return lst[1:] + [lst[0]]

my_list = [1, 2, 3, 4, 5]
shifted_list = shift_left(my_list)
print(shifted_list) # [2, 3, 4, 5, 1]
