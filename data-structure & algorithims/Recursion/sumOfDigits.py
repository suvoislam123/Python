def sum(n):
    assert n>=0 and int(n)==n,'The number has to be positive integer only'
    if n==0:
        return 0
    else:
        return int(n%10)+sum(int(n/10))
print(sum(158321))

