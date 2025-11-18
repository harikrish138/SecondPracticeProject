#single inheritance:
class Parent:
    def fun1(self):
        print('i am from Parent fun1')
    def fun2(self):
        print('i am from Parent fun2')
class Child(Parent):
    def fun1(self):
        print('i am from Child fun1')
        super().fun1()
    def fun2(self):
        print('i am from Child fun2')
        super().fun2()
a = Child()
# a.fun1()
# a.fun2()
class Bank:
    def rate_of_interest(self):
        return 0
class AxisBank(Bank):
    def rate_of_interest(self):
        return '12%'
class StateBank(Bank):
    def rate_of_interest(self):
        return '8%'
class YesBank(Bank):
    def rate_of_interest(self):
        return '18%'
x = AxisBank()
y = StateBank()
z = YesBank()
print(x.rate_of_interest())
print(y.rate_of_interest())
print(z.rate_of_interest())








