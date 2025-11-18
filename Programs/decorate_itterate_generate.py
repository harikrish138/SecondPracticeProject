def decor(fun):
    def xyz():
        print('Program started')
        fun()
        print('program is ended')
    return xyz
@decor
def name():
    print('my name is harikrishna')
@decor
def emp():
    print('my name is sowmyanadh')
name()


def cognizant(fun):
    def wrapper():
        print('company name is cognizant')
        fun()
        print('Company location hyd')
    return wrapper
def Bosch(fun):
    def wrapper(h):
        print('Company name is bosch')
        fun(h)
        print('Location is banglore')
    return wrapper
@Bosch
def hari(h):
    print('my name is hari emp id ',h)
@cognizant
def sowmyanadh():
    print('my name is sowmyanadh emp id 12')
hari(34567)
sowmyanadh()






