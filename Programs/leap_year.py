a = int(input("enter a year: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('it is a leap year')
else:
    print('it is not  a leap year')
lst={1:2.3,2:4}
print(dir(lst))




