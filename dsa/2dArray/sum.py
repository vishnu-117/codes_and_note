# input

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# output:
result = 45

def sumOfArrayElement(arr):
    sum = 0
    for i in arr:
        for j in i:
            sum += j
    return sum

print(sumOfArrayElement(array))


def sumUsingIndex(arr):
    sum = 0
    lth = len(arr)
    for i in range(lth):
        for j in range(lth):
            print(i,j)
            sum += arr[i][j]
    return sum

print(sumUsingIndex(array))

