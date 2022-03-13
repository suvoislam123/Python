# x = -8
# if x<2:
#     print('Greter Than Two')
#     if x<3:
#         print('Greater Than Three')
#         if x<4:
#             print('Greter than Four')
#         else:print('Big Number')
#     else:print('Hello Alien ')
# else:print('Less than 2')
# ------------------While loop --------------------
# i= 1
# while i<=5:
#     print('Allahu Akbar ',end='')#for preventing line break
#     j=1
#     while j<=2:
#         print('Allahu Rahim ',end='')
#         j = j+1
#     i= i+1
# --------------------For in loop------------- 
# x = ['shuvo','programming','watching Movie','Yo Yo']
# for i in x:
#     print(i,' ',end='')
#------------------- Foor Loop----------------------
# for i in range(1,100,1):
#     if i%3!=0 and i%5!=0:
#         print(i)
# --------------For Else Loop-------------------
li = [1,3,25,55,51]
for i in range(1, len(li),1):
    if li[i]%5 ==0:
        print(li[i])
        break
else:#ekta break thaka lagbe ar else endentation hobe for loop er baire
    print('Not Found')
# -------------Prime Number By For Else Loop--------------
def Myfunc(n):
    for i in range(2,6):
        if n==2:
            print('Prim Number')
            break
        elif n%i==0:
            print('Not Prime Number')
            break
    else:
        print('Prime Number')
Myfunc(200)
