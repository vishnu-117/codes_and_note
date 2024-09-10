# Input:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output:

result = [
    [1, 4],
    [2, 5],
    [3, 6]
]

def transposeMatrix(arr):
    rows = len(arr)
    cols = len(arr[0])

    # result = [[0 for i in range(rows)] for k in range(cols)]

    for i in range(rows):
        for k in range(i+1, rows):
            print(i,k)
            # result[k][i] = arr[i][k]
            arr[i][k], arr[k][i] = arr[k][i], arr[i][k]
    return arr

print(transposeMatrix(matrix))
