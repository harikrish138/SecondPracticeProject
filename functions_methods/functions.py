def my_function():
    print('hello, this is my function') #(no arguments no return)
my_function()
#_______________________________
def addition(x, y):
    print(x + y)                    #(arguments no return)
addition(3, 4)
#________________________________
def addition1(x, y):
    return x + y                    #(arguments and return)
a = addition1(3, 4)
print(a)
#___________________________________
def function():
    return 3 * 4                    #(no arguments but return)
print(function())
#___________________________________
#eg 1:- positional arguments:
def addition(x, y):
    print(x*y)
addition(4 ,5)
#___________________________________
# keyword arguments:
def add2(x,y):
    print(x+y)
add2(y=2, x=3)
#__________________________________________
#eg 2:- default values assigned to positive arguments
def fun(i, j=10):
    print(i, j)
fun(100, 200)
#___________________________________
def fun1(i=100, j=100):
    print(i, j)
fun1(200, 200)
#___________________________________
# variable length arguments:-
def hari(*args):
    print(*args)
hari(1,2,3,4,5,6)
#___________________________
# eg:-
def eg( *args):
    intial=0
    for i in args:
        intial +=i
    print(intial)
eg(8,4,5,6,7)
#________________________________
# Keyword variable length arguments:-
def keyword_word_length_arguments(*kwargs):
    for i in kwargs:
        print(i, end=" ")
keyword_word_length_arguments("hari",1, "sowmyanadh",2,"reddy",3,"prasanna")




