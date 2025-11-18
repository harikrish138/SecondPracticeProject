class Mother:
    def med1(self):
        print('iam from mother')
class Child1(Mother):
    def med2(self):
        print('iam from child1')
class Child2(Mother):
    def med3(self):
        print('iam from child2')
a = Child1()
b = Child2()
b.med1()
a.med1()