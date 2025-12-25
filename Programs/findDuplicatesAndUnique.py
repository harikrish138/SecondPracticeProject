nums=[1,1,2,3,4,3,2,1,4]
count={}
result=[]
dup=[]
for i in nums:
    if i not in result and i not in count:
        result.append(i)
        count[i]=1
    else:
        count[i] += 1
        if i not in dup:
            dup.append(i)

print(dup,result,count)