a = int(input("Enter a number: "))
def prime_number(a):
    if a<=1:
        return False
    for i in range (2, int(a**0.5)+1):
        if a % i==0:
            return False
    return True
if prime_number(a) is True:
    print(f'you entered a prime number: {a}')
else:
    print(f'you entered not a prime number: {a}')

#Method-2:
x = int(input('Enter a number: '))
for i in range(1, x+1):
    if x < 2:
        print('it is not a prime number')
        break
    elif x % i == 0:
        print('it is not a prime number')
else:
    print('It is a prime number')




