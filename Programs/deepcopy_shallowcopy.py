import copy

# shallow copy
list1 = [[1, 2, 3, 4]]
lst2=copy.copy(list1)
lst2[0][1]=12
# deep copy
list3 = [[1, 2], [3, 4]]
lst4=copy.deepcopy(list3)
lst4[0][0]=10
print(list1,list3)
