class Overload:
    def sum(self,a=None, b=None):
        if a is None:
            print('Hello')
        elif b is None:
            print('A Valve is ',a)
        else:
            print('Total value' ,a+b)

    def sum(self,a,b=1):
        print(a*b)
Overload.sum(self='self')








