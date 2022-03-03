# Types of Variable
# 1.Instance Variable
# 2.Class Variable(Static Variable)
from crypt import methods


class Car:
    wheels:4
    def __init__(self):
        self.com = 'BMW'
        self.mil = 12
c1 = Car()
c2 = Car()
c2.com = 'Toyta'#instance variable
Car.wheels = 6 #if I change class variable then all instace will get  affected on it
print(c1.com, c1.wheels)
print(c2.com, c2.wheels)
# Types of methods 
# 1.Instance methods
# 2.class Method
# 3.static method
class Dream:
    d = 'Block Chain Expert'
    def __init__(self,name):
        self.name = name
    def printName(self):#instance Method
        print(self.name)
    @classmethod
    def printDream(cls):#class Method
        print(cls.d)
    @staticmethod #static method
    def staticDream():
        print('I am lazy Person')
d1 = Dream('shuvo')
d2 = Dream('Shaiful')
d1.printName();
d2.printName()
Dream.printDream()
Dream.staticDream()


