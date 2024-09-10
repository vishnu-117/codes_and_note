def solve(A, B):
    count = 0
    for i in range(0, len(A)-1):
        # print(i, 'III')
        for j in range(i+1, len(A)):
            # print(j, 'jjj')
            if A[i] ^ A[j] == B:
                print( A[i], A[j])
                count += 1
    return count

A = [ 17, 18, 8, 13, 15, 7, 11, 5, 4, 9, 12, 6, 10, 14, 16, 3 ]
B = 9
print(solve(A,B), 'result>>>>>>')