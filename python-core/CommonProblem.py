# Factorial By Recursion 
def fact(n):
    if(n==0 or n==1):
        return 1
    else :
        return n*fact(n-1)
fact = fact(5)
print(fact)

# fibonacci number
def fib(n):
    a=1
    b=1
    if n<=2 or n>2:
        print(a)
    if n>=2:
        print(b)
    for i in range(2,n):
        c=a+b
        a =b
        b=c
        print(c)
number = 6
fib(number)
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit()) #for setting the limit of amount of recursion call
