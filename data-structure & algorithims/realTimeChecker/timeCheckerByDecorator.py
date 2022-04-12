import time
def timed(function):
    def wrapper(*args,**kwargs):
        before = time.time()
        value = function(*args,**kwargs)
        after = time.time()
        f_name = function.__name__
        print(f'{f_name} takes {after - before} seconds to execute')
        return value
    return wrapper
@timed
def hugeCalc(x):
    for i in range(0,x):
        for j in range(i):
            k = i*j
            for x in range(k):
                if(i==x-1):
                    pass
    print('Ahhh! finished')
hugeCalc(200)