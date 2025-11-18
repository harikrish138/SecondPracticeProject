lst=[1,2,3,4,5,6,7,8,9,10]
a = list(filter(lambda i : i%2==0,lst))
print(a)
b= list(map(lambda x: x**2,filter(lambda y: y%2!=0, lst )))
print(b)




