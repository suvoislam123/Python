from array import array
from multiprocessing.dummy import Array
#same type er datatype hoite hobe
#prothome data type er type code daoa lagbe
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
