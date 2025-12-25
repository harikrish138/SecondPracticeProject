str=[1,3,5,7]
result=[]
for i in range(str[0],str[-1]+1):
    if i not in str:
        result.append(i)

print(result)
missing=[i for i in range(str[0],str[-1]+1) if i not in str ]
print(missing)