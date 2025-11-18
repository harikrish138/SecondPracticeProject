
#Dictionary
#'clear', 'copy', 'fromkeys', 'get', 'items',
# 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


vehicles={'type':'sedan',
          'color' : 'red',
          'milage' : 25,
          'engine' : '1499cc'}

print(type(vehicles))
hari=vehicles.copy()
print(hari['type'])
hari['type']='SUV'
print(hari)
hari['wheel size']='16 inch'
print(hari)
print(hari.get('milage'))
soum=hari.items()
print(soum)
#
# for i,j in vehicles.items():
#     print(i,j)
# for i in vehicles.keys():
#     print(i)
# for i in vehicles.values():
#     print(i)

# hari.pop('color')
# print(hari)
# hari.popitem()
# print(hari)
reddy=[1,2,3,4,5,6]
s=dict.fromkeys(reddy,'Pass')
print(s)
s.setdefault(7,'Fail')
print(s)