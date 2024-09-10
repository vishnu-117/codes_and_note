import math


def isprimenumber(number):
    root = int(math.sqrt(number))
    for i in range(2, root + 1):
        if number % i == 0:
            return False
    else:
        return True


print(isprimenumber(79))
