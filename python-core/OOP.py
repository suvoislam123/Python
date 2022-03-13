class Me:
    def do(self):
        print('programming')
n1 = Me()
n2 = Me()
print(type(n1))
Me.do(n1)
Me.do(n2)
n1.do()
n2.do()
# Two type systax for accessing method
#___init()__ method
class Computer:
    def __init__(self):
        print('init method become automatically call')
c1 = Computer()#Here output is init method become automatically call
# --------------------------------------------
class School:
    def __init__(self,studen,teacher):
        self.student = studen
        self.teacher = teacher
    def showDetails(self):
        print('Number of student : {} and Number of teacher {}'.format(self.student,self.teacher))
s1 = School(1200,30)
s1.showDetails()
#Inheritance(multiple inheritance multi level inheritance)
class A:
    def f1(self):
        print('Feature 1')
    def f2(self):
        print('Feature 2')
class B(A):
    def f3(self):
        print('Feature 3')
    def f4(self):
        print('Feature 4')
b1 = B()
b1.f1()
#abstract class
from abc import ABC,abstractmethod
class Abs(ABC):
    @abstractmethod
    def implementer(self):
        pass
class ChildImp(Abs):
    def implementer(self):
        print('Hello World')#This method should be implemented
    def m1(self):
        print('Hello World')
obj1 = ChildImp()
obj1.m1()   
#My won Iterator
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = TopTen()
print(values.__next__())
print(values.__next__())
print(values.__next__())
for i in values:
    print(i)
        