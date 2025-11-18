# def calculation(arg1, arg2):
#     while arg1 < arg2:
#         print(arg1)
#         arg1+=1
#
# calculation(1,21)


# def calculation(arg1, arg2):
#     for i in iter(int, 1):
#        if arg1 >= arg2:
#            break
#        print(arg1)
#        arg1+=1
# calculation(1,21)

# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#
# obj = A(10, 20)
# print(obj.add())

#
# class A:
#     def add(self, a, b):
#         return a+b
# class B(A):
#     def add(self, c, d):
#         return c-d
# class C(B):
#     def add(self, x, y):
#         return x*y
#     def cal_parent_name(self):
#         return super().add(20,15)
#     def call_parent_name(self):
#         return super(B,self).add(30,10)
# obj = C()
# print(obj.add(10, 20))
# print(obj.cal_parent_name())
# print(obj.call_parent_name())

# from multipledispatch import dispatch
#
# class A:
#     @dispatch(int, int, int)
#     def add(self, a,b,c):
#
#         return a+b+c
#     @dispatch(int, int)
#     def add(self,a, b):
#         return a+b
# obj = A()
#
# print(obj.add(6,6))
# print(obj.add(5, 5, 5))
#
# class A:
#     def __init__(self):
#         self.x = 10
#         self._y = 15
#         self.__z = 20
#     def add(self):
#         return self.x + self._y + self.__z
#     def __mul(self):
#         return self.x * self._y * self.__z
# obj = A()
#
# print(obj.add())
# print(obj._A__mul())
#
# obj.x = 100
# obj._y = 50
# obj._A__z =25
# print(obj.add())
# print(obj._A__mul())
#
# class B:
#     q = 10
#     _w = 15
#     __e =20
#     def ad(self):
#         return self.q + self._w + self.__e
#     def __mu(self):
#         return self.q * self._w * self.__e
# ob = B()
# print(ob.ad())
# print(ob._B__mu())

lst = [0,0,3,1,12,0,4,0]
# o = [1,3,4,12,0,0]
a = sorted(lst)
for i in a:
    if i == 0:
        a.remove(0)
        a.append(0)
print(a)







