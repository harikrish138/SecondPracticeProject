class Father:
    def med1(self):
        print('iam from father')
class Mother:
    def med2(self):
        print('iam from mother')
class Child(Father, Mother):
    def med3(self):
        print('iam from child')
a = Child()
a.med1()