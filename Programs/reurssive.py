def flat(lst):
    s = []
    for i in lst:
        if isinstance(i,list):
            s.extend(flat(i))
        else:
            s.append(i)
    return s

lst1 = [1,2,[2,4,3,[5,3,[4,1],2],10],11,12]
print(flat(lst1))