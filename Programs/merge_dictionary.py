dic1={'a': 2, 'b':3, 'c':7}
dic2={'f': 2, 'd':3, 'c':4,'a': 9}
def merge (dic1,dic2):
    for i,j in dic2.items():
        if i in dic1:
            dic1[i]= [dic1[i],j]
        else:
            dic1[i] = j
    return dic1
print(merge(dic1,dic2))











