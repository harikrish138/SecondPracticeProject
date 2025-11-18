#List
# 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort'
a = [1,22,456,'abcd',1.60]
b = [10,25,'abcde',21.60]
d=[1,2,3,4,5,6,7,8,9]
c=a+b
print(c)
a.append('bat')
a.extend(['hello','well','come'])
print(a)
a.remove('come')
print(a)
d.reverse()
print(d)
e=a.copy()
print(e)
print(a.count(456))
a.clear()
print(a)