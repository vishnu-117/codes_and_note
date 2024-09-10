def solve(A):
    dict1 = {}
    result = 0
    for i in range(len(A)):
        dict1[A[i]] = dict1.get(A[i], 0) + 1
        result = max(result, dict1[A[i]])
    result

A = [ 8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3, 8, 17, 12, 5, 3, 14, 13, 3, 2, 17, 19, 16, 8, 7, 12, 19, 10, 13, 8, 20, 16, 15, 4, 12, 3 ]
print(solve(A))


# # Python3 code for the above approach
# def min_visible_bottles(arr, n):

# 	m = dict()
# 	ans = 0
# 	for i in range(n):
# 		m[arr[i]] = m.get(arr[i], 0) + 1
# 		ans = max(ans, m[arr[i]])

# 	print("Minimum number of",
# 		"Visible Bottles are: ", ans)

# # Driver code
# n = 8
# arr = [1, 1, 2, 3, 4, 5, 5, 4]

# Find the solution
# min_visible_bottles(arr, n)

# This code is contributed
# by Mohit Kumar
