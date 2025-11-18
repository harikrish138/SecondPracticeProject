lst1=[1,2,3,4,5,6,8]
lst=[x**2 for x in lst1 if x%2==0]
print(lst)

for i in range(10):

    print(i if i%2==0 else i>1 ,end=',')

ii=[i for i in range(10) if i%2==0  ]
print('\n',ii)
