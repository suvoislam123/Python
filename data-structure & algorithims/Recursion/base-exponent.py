def power(base,ex):
    assert ex>=0 and int(ex)==ex,'Exponent has to be positive integer'
    if ex==0:
        return 1
    if ex==1:
        return base
    else:
        return base * power(base, ex - 1)
print(power(2,9))
