l = ["yrros","765","irah","432"]
def abc (lst):
    rev = []
    out = []
    for j in lst:
        if j.isalpha():
            s = ''
            for i in range(len(j)-1,-1,-1):
                s += j[i]
            rev.append(s)
        else:
            d = ''
            for i in range(len(j)-1,-1,-1):
                d += j[i]
            out.append(d)
    return rev,out
print(abc(l))
#_____________________________________________________
def rev_digit_char(lst):
    char=[]
    digits=[]
    for i in lst:
        if i.isalpha():
            o=''
            for j in range(len(i)-1,-1,-1):
                o+=i[j]
            char.append(o)
        else:
            l=''
            for j in range(len(i)-1,-1,-1):
                l+=i[j]
            digits.append(l)
    return char,digits
print(rev_digit_char(l))










