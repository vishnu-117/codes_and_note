import time
import math

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(args, kwargs)
        func(*args, **kwargs)
        end = time.time()

        print('Total execution time took by function', func.__name__, 'is', end-start)
    return wrapper

@calculate_time
def printname(abc, **kwarge):
    time.sleep(2)
    print(abc)

printname('vishnu', **{'vtu': 'vishnu'})
# or
printname('vishnu', vtu='vishnu')
