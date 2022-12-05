from singleton import Singleton

class B():
    some_value= 1005

class A(Singleton, B):
    pass
a1=A()
a2=A()
print(id(a1))
print(id(a2))
print(a1.some_value)

