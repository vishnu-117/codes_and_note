# Input:
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output:
# [1, 2, 3, 6, 5, 4, 7, 8, 9]

def reverseList(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def zigzagTraversal(arr):
    rows = len(arr)
    # cols = len(arr[0])
    result = []

    for i in range(rows):
        print(i)
        if i == 1:
            result.extend(reverseList(arr[i]))
        else:
            result.extend(arr[i])
    return result

print(zigzagTraversal(array))
