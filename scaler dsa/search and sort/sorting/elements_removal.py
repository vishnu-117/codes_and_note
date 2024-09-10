def solve(A):
    A.sort()
    length = len(A)
    if length == 1:
        return A[0]
    elif length == 2:
        return A[1]+A[0]+A[0]
    else:
        result = sum(A)
        sum1 = sum(A)
        for i in range(len(A)-2, -1, -1):
            sum1 -= A[i+1]
            result += sum1
            # import pdb; pdb.set_trace()
    return result

# A = [ 8, 0, 10 ]
A = [ 3, 0, 9, 7, 8 ]
print(solve(A))
