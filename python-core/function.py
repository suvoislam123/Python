# call by value and call by refference konta.e python kore na
from pyclbr import Function


def update(x):
    print(id(x))
    x=8
    # when we change the variable value this time the variable alocate new memory 
    print(id(x))
    print('value:',x)
a = 10
print(id(a))
update(a)#//8
update(7)#//8
#---------------Keyword arguments----------------
def person(name,age):
    print(name)
    print(age-5)
# person(28,'Shuvo') we have problem in position sequence..Here keyword arguments comes into picture
person(age=45,name='shakib khan')
#python has deafault arguments which simmilar to javaScript
#variabe length arguments....takes parameter as touple
def sum(a,*b):
    c=a
    for i in b:
        c = c+i
    print(c)
sum(1,2,3,4)
# Keyworded Variable Length Arguments in Python
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('shuvo',age=24,address='kanaksar')
# Global Local Scope
a =10
def v():
    a=15#this a is local if I want to use global a then I have to use global a statement
    print(a)
v()
print(a)
# using global a
a =10
def v():
    global a
    a=15#this a is local if I want to use global a then I have to use global a statement
    print(a)
v()
print(a)
# globals()['a'] = 123 is use for changing the global variable without changing the local variable
# Even odd Counter
def eoCounter(list):
    e = 0
    o= 0
    for i in list:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o
list = [2,1,2,57,4,56,33,56,34]
e,o = eoCounter(list)
print('Even element {} Odd Element {}'.format(e,o))
# Annonymous Function or  lammbda
f = lambda a:a*a
square = f(5)
print(square)
# filter, map ,reduce 
from functools import reduce
# filtering even numbers
li = [1,2,3,53,5,4,78,34,24,433,245]
evens = list(filter(lambda n:n%2==0,li))
print(evens)
# now double evens by map
doubles = list(map(lambda a:a*2,evens))
print(doubles)
# factorial by reduce
numbers = [1,2,3,4,5,6]
fact = reduce(lambda a,b:a*b,numbers)
print(fact)
#decorator in python take a short time on it