tup=(1,2,3,4,5,6,8)
st=tuple(x**2 for x in tup if x%2==0)
print(st)

print(tuple(x for x in range(12)))