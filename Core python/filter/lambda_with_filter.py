seq = [0, 1, 2, 3, 5, 8, 13]

# find odd number:
result = list(filter(lambda x : x % 2 != 0, seq))
print(result)

# find even number:
result = list(filter(lambda x : x % 2 == 0, seq))
print(result)

#find multiple of 3:
def is_multiple_of_3(num):
    return num % 3 == 0

result = list(filter(lambda x: is_multiple_of_3(x), seq))
print(result)