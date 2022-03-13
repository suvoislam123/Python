tup = (1,23,45,34)
print(tup)
print(tup[0])#give 1
# tup[3] = 33 douple doesn't support item assignment
print(tup)
# Now Set
s = {1,2,32,222,222,2}#set elements sequence is their position randomly
print(s)
# s[2] = 66 it also doesn't support item assignment

# ----------------------------------------------------------
x = 'Shuvo'
y=x
print(id(x)) # for getting memory address of the variable
print(id(y))
x = 10.123
print(id(x))
print(type(x))
