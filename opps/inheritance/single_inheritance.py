#single inheritance:
class Parent:
    def fun1(self):
        print('i am from Parent fun1')
    def fun2(self):
        print('i am from Parent fun2')
class Child(Parent):
    def fun3(self):
        print('i am from Child fun1')
    def fun4(self):
        print('i am from Child fun2')
a = Child()
a.fun1()
a.fun2()