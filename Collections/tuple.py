#Tuple
#'count', 'index'



a = "apple",'apple', "banana","cherry","mango"
print(a)
print(a[0])
print(a.count('apple'))
print(a.index('cherry'))
print(type(a))
b = ('mango','orange','blueberry','kiwi')

c=a+b
print(c)

d=list(a)
d.pop(0)
d.insert(1,'sapota')
d.append('grape')
print(tuple(d))