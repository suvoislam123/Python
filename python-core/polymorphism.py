# import typing


# Polymorphism
# 1.Duck typing
# 2.Opertor Overloading
# 3.Method Overloading
# 4.Method Overriding
# -------------------Duck Typing----------------
# Hints:If there is a bird;it walks like a duck,it quack like a duck,it swim like a duck then it should be a duck
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')
        print('Compiling')
        print('Running')
class VsCode:
    def execute(self):
        print('Spell Check')
        print('Convention Checking')
class Laptop:
    def code(self,ide):
        ide.execute()
e1 = PyCharm()
e2 = VsCode()
l1 = Laptop()
l1.code(e1)
print('------------')
l1.code(e2)
# 2.Operator Overloading
# 3.Method Overriding
def Mover(a=None,b=None,c=None):
    if(a!=None and b!=None and c!=None):
        return a+b+c
    if(a!=None and b!=None):
        return a+b
    else:
        return a
print(Mover(1,23,34))
print(Mover(1,2))
print(Mover(1))
print(Mover())

