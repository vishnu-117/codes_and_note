import sys
def solve(A, B):
    sum1 = 0
    min_bullet = sys.maxsize
    lenA = len(A)
    for i in range(lenA):
        # import pdb; pdb.set_trace()
        sum1 += max(0, A[i]-B[(i-1+lenA)%lenA])+A[i]

    for i in range(lenA):
        # import pdb; pdb.set_trace()
        min_bullet =  min(min_bullet, sum1-max(0,A[i]-B[(i-1+lenA)%lenA])+A[i])
            
    return min_bullet

A = [ 10, 13, 25, 14, 24, 49, 43, 48 ]
B = [ 38, 23, 47, 20, 49, 40, 22, 39 ]

print(solve(A,B))