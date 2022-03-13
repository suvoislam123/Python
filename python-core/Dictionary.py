from ast import Add
familyMember = {1:'Shaiful',2:'Sahabuddin',3:'Shuvo',4:'Sawon','ma':'Lipy Begum','baba':'Babul Sheikh'}
print(familyMember)
print(familyMember[3])
print(familyMember['ma'])
print(familyMember.get(1))
#get() is same as by index but difference is it won't give error when the key doesn't match
print(familyMember.get(5,'NotFound'))# if keys value exist then return the value otherwise return Not Found
print(familyMember)
#Converting Two List to Dictionary
keys = ['shuvo','sawon','sahabuddin','shiful']
values =['Chicken','Egg','Vorta','Bot']
d = dict(zip(keys,values))
print(d)
# Add Value 
d['ma'] = 'Nodir mach'
print(d)
del d['shuvo']
print(d)
# Nested Dictionary
nd = {'shawon':{'math':'bad','english':'worst','hystory':'good'},'shuvo':['math','programming']}
print(nd['shawon']['hystory'])
