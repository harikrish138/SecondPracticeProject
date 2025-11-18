import re
a='hello my name is krish'
b='hello Hello Holla'
s='hello123Welcome2Hyderabad876'
print(re.search(r'\d+',s))
print(re.split(r' ',a))
print(re.match(r'\d+',s))
print(re.findall(r'\d+',s))
print(re.fullmatch(r'\D{5}',b))
# print(re.search(r'\d+',s))
