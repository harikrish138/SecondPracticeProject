lst = [1,-1,2,-3,3,7,9,10,-11]
def abc(l,k):
    res= []
    m=k
    n=0
    for i in range(len(l)):
        dup = l[n:m]
        if k == len(dup):
            dup.sort()
            res.append(dup[-1])
            n+=1
            m+=1
    return res
print(abc(lst,3))
print(sum(lst))
