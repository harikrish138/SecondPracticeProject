s='banana'

result={}
for i in s:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1
print(result)