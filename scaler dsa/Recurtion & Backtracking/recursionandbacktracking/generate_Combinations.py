def combine(A,B):
    """
    Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 ... A.

    Make sure the combinations are sorted.

    To elaborate,

    Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
    Entries should be sorted within themselves.
    WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.

    input:
    A = 4
    B = 2

    output:
     [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [3, 4],
    ]
    """
    arr = []
    for i in range(1, A+1):
        arr.append(i)

    def permutation(arr, index, tmp):
        if len(arr) == index:
            if len(tmp) == B:
                result.append(tmp.copy())
            return
        permutation(arr, index+1, tmp+[arr[index]])
        permutation(arr, index+1, tmp)

    tmp = []
    result = []
    permutation(arr, 0, [])
    return result

A = 4
B = 2
result = combine(1,4)
print(result)
