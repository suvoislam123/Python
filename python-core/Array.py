from array import array
from lib2to3.pgen2.literals import simple_escapes
from multiprocessing.dummy import Array
#same type er datatype hoite hobe
#prothome data type er type code daoa lagbe
# This is simple_escapes
vals = array('i',[1,2,3,4,233])
newArr = array(vals.typecode,(a*a for a in vals))#square operation
print(newArr)
print(vals)
vals1 = array('L',[1,34,45,3324,55])
print('Sorted Array Kora lagbe')
print(vals1)
print(vals1.buffer_info())
print(vals1[1])
char = array('u',['A','B','C','D','E'])
print(char)
# ---------------Array Input-------------------
arr = array('i',[]);
size = int(input('Enter the size of the array'))
for i in range(size):
    x= int(input('element'))
    arr.append(x)
print(arr)
# ---------Multi-Dimensional Array(Numpy)------------
# By defaul python array package doesn't support multidimensional array that's where numpy comes
from  numpy import *
arr = array([1,2,32,2])
arr = arr + 5
print(arr)
# -----------Copying Array--------
arr = array([1,2,32,2])
arr2 = arr.copy() #deep copy
# arr2 = arr.view()#shallow copy
arr2[1]=30
print(arr2)
print(id(arr2))
print(id(arr))
# ---------------------------Matrix------------------
arr = array([
    [1,2,3,4],
    [3,5,64,3],
    [2,3,42,3]
])
print(arr)
print('data type:',arr.dtype)
print('Dimension:',arr.ndim)#2d
print('row X coloumn :',arr.shape)
print('Size:',arr.size)#12
oneD = arr.flatten();
print(oneD)
threeD = oneD.reshape(2,2,3)
print(threeD)
# matrix opertion
a = array([
    [1,2,3,4],
    [4,5,68,7]
])
#if I make variable matrx then I will get some extra matric
#converting array to matrix
m = matrix(a)
print(m)
#direct matix
mat = matrix('1,2,3,4;4,5,6')
print(m.diagonal())
