def reverse(A):
    c = A
    A = abs(A)


    new_number = 0
    while A != 0:
        mod = A % 10
        new_number = new_number * 10 + mod
        A = A//10
    
    if(abs(new_number) > 2 ** 31-1):
            return 0

    if c < 0:
        return -(new_number)
    else:
        return new_number


# A =  -123
# A =  1
# A = -1146467285
A = -3342703511
print(reverse(A))

# import sys
# print(sys.getsizeof(int))
# print(type(reverse(A)))
