def solve(A, B):
    data_dict = {}
    sum = 0
    count = 0
    for index, value in enumerate(A):
        if sum == B:
            return A[:index+1]
        sum += value
        # import pdb; pdb.set_trace()
        while sum > B:
            # import pdb; pdb.set_trace()
            sum -= A[count]
            count += 1
            if sum == B:
                return A[count:index+1]
            if sum < B:
                print('inseide second ')
                return -1
        # break
    return -1

# A = [ 5, 10, 20, 100, 105 ]
# B  = 110

# A = [1, 2, 3, 4, 5]
# B = 5

A = [1,4,20,3,10,5]
B = 11

print(solve(A,B))