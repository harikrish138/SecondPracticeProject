lst=[-5,2,0,1,0,3]
target=-3
# min_diff=min(abs(x-target) for x in lst if x !=target)    # abs is converting -  to +
# # print(min_diff)
# closest_index=[i for i,x in enumerate(lst) if abs(x-target)==min_diff]
# # print(closest_index)
# print([lst[i] for i in closest_index ])

min_val=[]
for i in lst:
    if i != target:
        min_val.append(abs(i-target))
min_val=min(min_val)
# print(min_val)
indexes=[]
for i,x in enumerate(lst):
    if abs(x-target)==min_val:
        indexes.append(i)

for i in indexes:
    print(lst[i])
