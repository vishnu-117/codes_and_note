#sort(key=(anyfunction),reverse=True|False)

def length(i):
    return len(i)

car = ['ford','marutisuzuki','blint','mazarati']
car.sort(key=length)
print(car)