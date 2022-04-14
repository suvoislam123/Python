class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name = name
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,age):
        if self.__age<age:
            self.__age = age
        else:
            self.__age = 'Gordhop age kokhno kome naki'


p1 = Person('shuvo',23)
print(p1.Name)
print(p1.Age)
p1.Age = 188
print(p1.Age)

