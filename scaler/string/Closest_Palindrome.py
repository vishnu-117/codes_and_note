def solve(A):
    length = len(A)
    count = 0
    for i in range(0, length//2):
        if count > 1:
            return "NO"

        if A[i] != A[length-1-i]:
            count += 1

        # import pdb; pdb.set_trace()
        if count==0 and length % 2 == 0:
            return "No"
        else:
            return "YES"

A = "abba"
print(solve(A))