def solve(A, B):
    p1 = 0
    p2 = 0
    sum = 0
    while len(A)-1 >= p2:
        if sum < B:
            sum += A[p2]
            p2 += 1
        elif sum > B:
            sum -= A[p1]
            p1 += 1
        elif sum == B:
            return A[p1:p2]
        
    return -1
                

A = [ 5, 10, 20, 100, 105 ]
B = 110

# A = [1, 2, 3, 4, 5]
# B = 5
print(solve(A, B))