# a ='hello'
# b=""
# for i in range(len(a)):
#     b+= a[(-1-i)]
# print(b)
#
#
# z ='happy'
# o = ""
# d=len(z)-1
# for i in range(d,-1,-1):
#     o +=z[i]
# print(o)
import re

string ='hello123Welcome2Hyderabad876'
m=re.findall(r'\d+|\D+',string)
print(m)

def reverse_the_only_string(st):
    parts=[]
    temp=''
    is_element = st[0].isalpha()
    for i in st:
        if i.isalpha() == is_element:
            temp+=i
        else:
            parts.append(temp)
            temp = i
            is_element = i.isalpha()
    parts.append(temp)
    print(parts)
    output=''
    for i in parts:
        if i.isalpha():
            for j in range(len(i)-1,-1,-1):
                output+=i[j]
        else:
            output+=i
    return output

print(reverse_the_only_string(string))


