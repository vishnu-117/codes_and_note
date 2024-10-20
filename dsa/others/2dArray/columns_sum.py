# Input:

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output:
# [12, 15, 18]

def columnSum(arr):
    rows = len(arr)
    cols = len(arr[0])

    result = [0] * rows
    for i in range(rows):
        for k in range(cols):
            result[k] = result[k] + arr[i][k]
    return result

print(columnSum(array))
