a=10

for i in range(a):
    space="* "*(a-i)
    print(space)
# =================================================
for i in range(a):
    print('* '*i)
# =================================================
for i in range(1,10+1):
    print(' ')
    for j in range(1,i+1):
        print(j,end=' ')
print(' ')
# =================================================
l=6
b=6
print('* '*b)
for i in range(1,l-1):
    print('*'+' '*((b*2)-3)+'*')
print('* '*b)
# =================================================
l=6
for i in range(l):
    print()
    for j in range(i+1):
        print(' ', end=' ')
    for k in range(i,l):
        print('*', end=' ')
    for n in range(l-i-1):
        print('*', end=' ')
#   ===========================================================
for i in range(l):
    print()
    for j in range(i,l):
        print(' ',end=' ')
    for k in range(i+1):
        print('*', end = ' ')
    for n in range(i):
        print('*',end=' ')
print()
p=6
for i in range(p):
    print(' '*(p-i-1)+ '*'*(2*i+1))


