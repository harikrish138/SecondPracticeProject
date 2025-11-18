# def factorial_num(n):
#     a=1
#     for i in range(1,n+1):
#         a*=i
#     return a
# print(factorial_num(5))
def find_large_num_in_list(lst):
    mx=0
    for i in lst:
        if i>mx:
            mx=i
    return mx
lst=[1,2,4,6,8,9]
print(find_large_num_in_list(lst))



