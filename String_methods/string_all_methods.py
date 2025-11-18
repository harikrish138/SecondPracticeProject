
s=' hello THIS is my world is '
upper=s.upper()
print(f'upper = {upper}')
lower=s.lower()
print(f'lower = {lower}')
capitalize=s.capitalize()
print(f'captilize = {capitalize}')
Title=s.title()
print(f'Title = {Title}')
strip=s.strip()
print(f'strip = {strip}')
lstrip=s.lstrip()
print(f'lstrip = {lstrip}')
rstrip=s.rstrip()
print(f'rstrip = {rstrip}')
strat=s.startswith(' ')
print(f'startswith = {strat}')
ends=s.endswith(' ')
print(f'endswith = {ends}')
replace=s.replace('is','was')
print(f'replace = {replace}')
split=s.split()
print(f'split = {split}')
lst='wel','come','to','India'
join=' '.join(lst)
print(f'join = {join}')
w='my name is hari krishna'
find=s.find('hello')
print(f'find = {find}')
find1=s.rfind('IS')
print(f'rfind = {find1}')
find2=s.find('is')
print(f'rfind = {find2}')
index=s.index('is')
print(f'index {index}')
rindex=s.rindex('is')
print(f'rindex {rindex}')
count=s.count('is')
print(f'count = {count}')
print("_________________-------------------_________________")

word='UPPER'
word1='lower'
word2='Capitalize'
word3='yskdgfw34k345234s'
word4='2345678'
word5=' '
word6='hgjhsgdkfjgsd'
word7 = '76438'
print(f'alnumeric = {word3.isalnum()}')
print(f'alpha = {word6.isalpha()}')
print(f'digit = {word4.isdigit()}')
print(f'lower = {word1.islower()}')
print(f'upper = {word.isupper()}')
print(f'space = {word5.isspace()}')
print(f'numeric = {word4.isnumeric()}')
print(f'decimal = {word7.isdecimal()}')
