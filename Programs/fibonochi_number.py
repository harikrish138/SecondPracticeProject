a= int(input("Enter number : "))
b=0
c=1
for i in range(a):
    print(b,c,end=',')
    b,c=c,b+c

# for i in range(1,a+1):
#     if a<2:
#         print('given number is not a prime')
#         break
#     elif a%i == 0:
#         print('given number is not a prime')
#         break
# else:
#     print('it is a prime number')

def fibonacci_series(n):
    a=0
    b=1
    for _ in range(n):
        print(a,b, end=', ')
        a,b=b,b+a
fibonacci_series(5)