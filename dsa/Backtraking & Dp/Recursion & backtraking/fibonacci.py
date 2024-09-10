def fibonaacci(number):
    if number <= 1:
        return number
    else:
        return fibonaacci(number - 1) + fibonaacci(number - 2)


number = 5
print("fibonaacci sequence is:")
for i in range(number):
    print(fibonaacci(i))

