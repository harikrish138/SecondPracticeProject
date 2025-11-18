# s = "hi hello hi how hello hi"
# l = s.split()
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# a = sorted(d.values())
# for x,y in d.items():
#     if a[-1]==y:
#         print(x)

w = [11,22,33,44,11,55,66,11,55]
d = []
c=[]
for i in w:
    if i not in d:
        d.append(i)
    else:
        c.append(i)
print(c)









