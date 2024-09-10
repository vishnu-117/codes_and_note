def permutate(A, index):
    """
    Given an integer array A of size N denoting collection of numbers , return all possible permutations.

    input:
    A = [1, 2, 3]

    output:
    [ [1, 2, 3]
    [1, 3, 2]
    [2, 1, 3] 
    [2, 3, 1] 
    [3, 1, 2] 
    [3, 2, 1] ]
    """
    if index == len(A):
        result.append(A.copy())
        return
    for i in range(index, len(A)):
        A[index], A[i] = A[i], A[index]
        permutate(A, index+1)
        A[index], A[i] = A[i], A[index]

result = []
A = [1,2,1]
# A.sort()
permutate(A, 0)
print(result)