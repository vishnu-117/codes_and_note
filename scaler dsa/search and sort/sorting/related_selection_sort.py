def solve(A):
    # B = sorted(A)
    result = []
    size = len(A)
    
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if A[i] < A[min_idx]:
                import pdb; pdb.set_trace()
                min_idx = i
                result.append(i)
        (A[step], A[min_idx]) = (A[min_idx], A[step])
    return result

A = [6, 4, 3, 7, 2, 8]

#  [4, 2, 2, 4, 4]

print(solve(A))