def find_large_num_in_list(lst):
    mx=0
    for i in lst:
        if i>mx:
            mx=i
    return mx
lst=[1,2,4,6,8,9]
print(find_large_num_in_list(lst))