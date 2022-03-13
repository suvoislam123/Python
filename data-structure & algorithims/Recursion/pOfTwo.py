def pOfTwo(n):
    if n==0:
        return 1
    else:
        pow =  pOfTwo(n-1)
        return 2*pow
print(pOfTwo(5))
