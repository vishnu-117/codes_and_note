# def generateMatrix(A):
#     top = 0
#     right = A-1
#     left = 0
#     bottom = A-1
#     val = 1
#     result = [[0] * A] * A
#     if A > 1:
#         while val <= A * A:
#             for i in range(left, right+1, 1):
#                 # import pdb; pdb.set_trace()
#                 result[top][i] = val
#                 val += 1
#             top += 1
#             import pdb; pdb.set_trace()
#             for i in range(top, bottom+1, 1):
#                 # import pdb; pdb.set_trace()

#                 result[i][right] = val
#                 val += 1
#             right -= 1
#             if (top < bottom):
#                 for i in range(right, left+1, -1):
        
#                     result[bottom][i] = val
#                     val += 1
#                 bottom -= 1
#             if (left < right):
#                 for i in range(bottom, top+1, -1):
#                     import pdb; pdb.set_trace()

#                     result[i][left] = val
#                     val += 1
#                 left += 1
#     else:
#         result = [[1]]
#     return result

# print(generateMatrix(3))


def generateMatrix(A):
    top = 0
    right = A
    left = 0
    bottom = A
    val = 1
    # result = [[0] * A] * A
    result = []
    for i in range(A):
        a = []
        for j in range(A):
            a.append(0)
        result.append(a)

    if A > 1:
        while val <= A * A:
            for i in range(left, right):
                result[top][i] = val
                val += 1
            top += 1
            for i in range(top, bottom):
                result[i][right-1] = val
                val += 1
            right -= 1
            for i in range(right-1, left-1, -1):
                result[bottom-1][i] = val
                val += 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                result[i][left] = val
                val += 1
            left += 1
    else:
        result = [[1]]
    return result
print(generateMatrix(3))
	            