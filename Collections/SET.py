#Set
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
# 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

a = {1, 2, 'apple','banana',1}
b ={2,8,'zxcv','vbnm',1,'apple'}
print(a)
c = a.union(b)
print(c)
e={7,9,3,4}
f={5,6,7}
g=e.isdisjoint(f)
print(g)
# a.add('hello')
# a.update({'sd','sdd','wet'})
# print(a)
# a.discard('hello')
# a.remove(1)
# print(a)
h=a.difference(b)
print(h)
j=a.intersection(b)
print(j)
k={7,4}
l=k.issubset(e)
print(l)
z=a.symmetric_difference(b)
print(z)
a.symmetric_difference_update(b)
print(a)
