def solve(A, B, sum1, count, index):
    sum1 = 0
    count = 0
    index = 0
    length = len(A)
    if sum1 >= 100:
        return 0
    if count == B:
        count += 1
        return 0
    if index == length:
        return 0
    solve(A, B, sum1+A[index], count+1, index+1)
    solve(A, B, sum1, count, index+1)
    return count


A = [ 1, 2, 8 ]
B = 2

print(solve(A, B, 0, 0, 0))
