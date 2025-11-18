s ="sowmyanadh"
a = set(s)
print(a)

s ="sowmyanadh"
a = list(s)
print(a)

s ="sowmyanadh"
a = tuple(s)
print(a)

s ="sowmyanadh"
a = dict.fromkeys(list(s), 1)
print(a)

s ="sowmyanadh"
a = {i:ch for i,ch in enumerate(s)}
print(a)

lst=[1,2,4,6,8,9,34,5]
for i,j in enumerate(lst):
    print(i,' : ',j,end=' , ')
