addition = lambda x, y : x + y
result = addition(5,5)
print(result)

check= lambda x: 'Even num' if x%2==0  else 'Odd'
print(check(3))

mul = lambda z : z * 5
res = mul(5)
print(res)

lst=[1,2,3,4,5]

mu=list(map(lambda x:x*2,lst))
print(mu)

fl=list(filter(lambda x:x%2==0,lst))
print(fl)

items = [(2, 'b'), (1, 'a'), (3, 'c')]
print(sorted(items,key=lambda x:x[0] ))

students = [
    {"name": "Hari", "age": 25},
    {"name": "Krishna", "age": 20}
]

print(sorted(students,key=lambda x:x['age']))

