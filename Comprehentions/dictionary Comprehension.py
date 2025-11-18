# Dictionary Comprehension:-------
dict = {x: x**2 for x in range(1,16) if x % 2 == 0}
print(dict)

# Set Comprehension:--------
st1={1,2,3,4,5,6,8,9,10,11,12,13,14,15,16}
st={x**2 for x in st1 if x%2==0}
print(st)