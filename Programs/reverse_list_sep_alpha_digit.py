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
# ---------------------------------------------------------

str="sandrapalli sowmy sree"
# lst=str.split()
# word=lst[1]
# lst[1]=word[::-1]
# print(' '.join(lst))

def reverse_word(words,sub_word):
    lst_words=words.split()
    for word in range(len(lst_words)):
       if lst_words[word] == sub_word:
           revers_word=lst_words[word]
           lst_words[word]=revers_word[::-1]
    return ' '.join(lst_words)

print(reverse_word(str,'sree'))

# _______________________________
st='sowmyanadh'
rev_st=''
for i in st:
    rev_st=i+rev_st

print(rev_st)

# =================================================
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







