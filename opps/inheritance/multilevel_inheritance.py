class GrandParent:
    def med1(self):
        print('iam from grand parent')
class Parent(GrandParent):
    def med2(self):
        print('iam from parent')
class Child(Parent):
    def med3(self):
        print('iam from child')
a = Child()
a.med1()