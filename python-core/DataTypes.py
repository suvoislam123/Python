
# 1.None->None
# 2.Numeric ->int , float,complex,bool
# 3.List->
# 4.Touple
# 5.Set
# 6.String
# 7.Range
# 8.Dictionary
# {List,Touple,Set,String,Range} comes under Sequence
x = None
print(type(x))
x = 12 + 8j #complex Numeric
print(type(x))
y = 102.232
print(int(y))#102
print(int('12'))#12
print(complex(4,5))# 4+5j
t = True
print(type(t))
print(int(t))#1
a = [1,2,34,56]
print(type(a)) #list
b= {1,2,4234,2}
print(type(b))#Set
d = (1,23,74)
print(type(d))#touple
e = "Shuvo"
print(type(e)) #str
#Range
print(range(12))
li = range(15)
print(list(li))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
li1 = range(2,20,2)#1st= start, 2nd= end ,3rd= difference
print(list(li1))#[2, 4, 6, 8, 10, 12, 14, 16, 18]
#Dictionary
lang = {1:'C',2:'Java',3:'JavaScript',3:'Python'}
print(lang[3])#if the index is same then it prints last key item. Output:Python
print(lang.keys())
print(lang.values())





