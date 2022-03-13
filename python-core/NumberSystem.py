# Python program to convert decimal into other number systems
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
# Swapping Two Variabl
# a=3
# b=7
# a = a+b
# b= a-b
# a=a-b
# print(a , b)
# by XOR(XOR doesn't use extra bit)
# a=3
# b=7
# a = a^b
# b= a^b
# a=a^b
# print(a, b)
# ###Another Way
# a= 8
# b= 10
# a,b = b,a
# print(a , b)
# --------BitWise Operator------(Eigula Binary bit dia calculatio kore)
# Complement
print(~14)#-15 {logic 11001 become 00110}
#AND
print(12&13)
# OR
print(12|133)
# XOR (Odds numbers of 1 = 1 otherwise 0)
print(12^6^1)
# Left Shift
print(10<<2)#(1010.00000.... Become 101000.000.....{gaining bits})
print(10>>2)#(1010.000...Become 10.000 ....{losing bits})
# ----------------Math function 
import math
print(math.sqrt(9))
print(math.floor(12.9))
print(math.ceil(2.1))
print(math.pow(3,3))
print(math.pi)
print(math.e)
if 4%2==0:
    print("Even Number")
else :print('Odd number')    

