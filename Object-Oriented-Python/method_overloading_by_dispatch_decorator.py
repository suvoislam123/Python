from multipledispatch import  dispatch
@dispatch(int,int,int)
def result(first,second,third):
    print(first+second+third)
@dispatch(float,float,float)
def result(first,second,third):
    print(first*second*third)
@dispatch(int,int)
def result(first,second):
    print(first/second)
result(12.1,2.4,3.12)
result(2,3,4)
result(10,5)
