
class Class1:
    x = 100
    y = 200
    def addition(self, x, y):
        print(x + y)
    def sub(self, x, y):
        print(x - y)
    def multi(self, x, y):
        print(x * y)
    def expo(self, x, y):
        print(x ** y)
eg1 = Class1()

# eg1.addition(3, 4)
#______________________________________________
x, y= 100, 200
class Class2:
    x = 300
    y = 400
    def addition(self):
        global x,y
        print(self.x + self.y)
        print(x + y)

eg2 = Class2()
#eg2.addition()

class Class3:
    x = 600
    y = 700

    def addition(self,x,y):

        print(x + y)

        print(self.x + self.y)

        print(globals()['x']+globals()['y'])

eg3 = Class3()
# eg3.addition(40,50)


class Con:
    def __init__(self,q,w):
        print('i am from constructor',q,w)
    def addd(self,a,b):
        print(a+b)

co=Con(2,2)
co.addd(20,30)
