
def solve(A,B):
    n = len(A)
    j = B
    arr = A
    k = 1000
    count = 0
    def count_sixlets(i, length, k, arr, b):
        print(i, '<<<<<<<')
        if i >= length:
            # import pdb; pdb.set_trace()
            if k <= 1000:
                return count + 1
            else:
                return 0
        # import pdb; pdb.set_trace()
        count_sixlets(i+b, length, sum(arr[i:b+1]), arr, b)
        # case2 = count_sixlets(i+j, length, k, arr, b)
        return count

    return count_sixlets(0, n, k, arr, j)

A = [1,2,8]
B = 2

# A = [5, 17, 1000, 11]
# B = 4
print(solve(A,B))