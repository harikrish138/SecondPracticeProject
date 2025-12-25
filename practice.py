s='hello456sowmyanadh987'
result='hello654sowmyanadh789'

res=[]
temp=''
isalpha = s[0].isalpha()
for i in s:
    if i.isalpha()==isalpha:
        temp+=i
    else:
        res.append(temp)
        temp=i
        isalpha=i.isalpha()
res.append(temp)
for i in range(len(res)):
    if res[i].isnumeric():
        res[i]=res[i][::-1]
print(''.join(res))
