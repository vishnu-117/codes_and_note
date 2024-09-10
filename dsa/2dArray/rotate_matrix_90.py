# Input:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

def rotateMatrix90(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[None] * cols for i in range(rows)]
    for i in range(rows):
        col_index = 2
        for k in range(cols):
            print(i, col_index)
            result[i][k] = matrix[col_index][i]
            col_index -= 1
    return result


print(rotateMatrix90(matrix))