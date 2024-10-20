def combine(A,B):
    arr = []
    for i in range(1, A+1):
        arr.append(i)
    length = len(arr)

    print(arr, 'arr')
    def permutation(arr, index, tmp):
        if len(arr) == index:
            if len(tmp) == 2:
                result.append(tmp.copy())
            return
        permutation(arr, index+1, tmp+[arr[index]])
        permutation(arr, index+1, tmp)

    permutation(arr, 0, [])
    return result

A = 4
B = 2
result = []
combine(4,2)
print(result)