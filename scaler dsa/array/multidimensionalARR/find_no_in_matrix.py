def solve(A, B):
    raw_len = len(A)
    col_len = len(A[raw_len-1])
    a = 0
    b = 0
    found = False
    if not (B >= A[0][0] and B <= A[raw_len-1][col_len-1]):
        return -1
    else:
        for i in range(raw_len):
            for j in range(col_len):
                if A[i][j] == B:
                    a = i
                    b = j
                    # import pdb ; pdb.set_trace()
                    print(a,b, '>>>>>>>>', B)
                    found = True
                    break
            if found:
                break
    # import pdb; pdb.set_trace()
    a += 1
    b += 1
    result = a*1009+b
    return result

A = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
B = 2
print(solve(A,B))