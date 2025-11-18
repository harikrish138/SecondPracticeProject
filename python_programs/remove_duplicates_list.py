l = [11,22,44,55,11,11,45,45,78,99,45]
s = []
for i in l:
    if i not in s:
        s.append(i)
print(s)

a = set(l)
b = list(a)
b.sort()
print(b)
c = list(a)
d = c.sort(reverse=True)
print(c)
