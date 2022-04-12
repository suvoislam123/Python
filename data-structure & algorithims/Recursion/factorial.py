def fact(n):
    assert n>0 and int(n)==n,'Please enter possitive number'
    if n==1 or n==0:
        return 1
    else:
        print(n)
        return n*fact(n-1)

fact(10)
