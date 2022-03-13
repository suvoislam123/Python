try:
    print(4/0)
except Exception as e:
    print('You can not do this operation. Formally the error known as : ',e)
print('Good Bye')
# ---------Error Handling By it types -----------
try:
    print(4/'p')
except ZeroDivisionError as e:
    print('You can not divid the value by Zero. Formally the error known as : ',e)
except ValueError as e:
    print('Input Error')
except Exception as e:
    print(e)
print('Good Bye')
# Threading 
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(0.4)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(0.4)
h1 = Hello()
h2 = Hi()
h1.start()
h2.start()
h1.join()
h2.join()
print('Bye') #Main Thread