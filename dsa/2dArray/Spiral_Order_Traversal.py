# Input:
matrixay = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output:
res = [1, 2, 3, 6, 9, 8, 7, 4, 5]

def spiralOrderT(matrix):
    result = []
    left, right = 0, len(matrix[0]) #row
    top, bottom = 0, len(matrix) #col

    while left < right and top < bottom:

        #Traverse from left to right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        #Traverse from top to bottom
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        #Traverse from right to left
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        bottom -= 1

        #Traverse from bottom to top
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1
        
    return result

print(spiralOrderT(matrixay))
