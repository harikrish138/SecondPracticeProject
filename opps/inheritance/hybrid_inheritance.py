class GrandMother:
    def med1(self):
        print('iam from grandmother')
class Father(GrandMother):
    def med2(self):
        print('iam from father')
class Mother(GrandMother):
    def med3(self):
        print('iam from mother')
class Child(Father, Mother):
    def med4(self):
        print('iam from child')

a = Child()
a.med1()
a.med2()
a.med3()
a.med4()
