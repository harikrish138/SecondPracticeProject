a=[2,20,1,30,4,5,23,25,2,2,5,5]
maxz=a[0]
second=0
for i in a:
    if maxz <i:
        second = maxz
        maxz=i
    elif i >second and i != second:
        second=i
print(second)
b=max(a)
print(max(i for i in a if i!=b))