from itertools import count
from typing import List

from pycparser.ply.yacc import resultlimit

a = input("Enter a word: ")
def count_vowels(st):
    v='aeiouAEIOU'
    result = ""
    for i in st:
        if i in v:
            result+=i
    return result
print(len(count_vowels(a)))


str='bananaBaNANA'
s='aeiouAEIOU'
resul={}
for i in str:
    if i in s and i not in resul:
        resul[i]=1
    elif i in s and i in resul:
        resul[i]+=1
print(resul)






