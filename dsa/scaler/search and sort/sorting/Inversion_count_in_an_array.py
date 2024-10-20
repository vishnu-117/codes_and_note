# class Solution:
#     # @param A : list of integers
#     # @return an integer
def solve(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        solve(L)
        solve(R)
        
        i = j = k = 0
        inv_count = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
                k += 1
            else:
                print()
                A[k] = R[j]
                j += 1
                k += 1
                # import pdb; pdb.set_trace()
                inv_count += (mid - i)

                print(inv_count, '<<<<<<<')
                
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
        return inv_count

# A = [ 45, 10, 15, 25, 50 ]

# A = [3, 2, 1]

# A = [1, 2, 3]

# A = [33, 12, 32, 20]
A = [1, 20, 6, 4, 5]
print(solve(A))


# # Python 3 program to count inversions in an array

# # Function to Use Inversion Count
# def mergeSort(arr, n):
# 	# A temp_arr is created to store
# 	# sorted array in merge function
# 	temp_arr = [0]*n
# 	return _mergeSort(arr, temp_arr, 0, n-1)

# # This Function will use MergeSort to count inversions

# def _mergeSort(arr, temp_arr, left, right):

# 	# A variable inv_count is used to store
# 	# inversion counts in each recursive call

# 	inv_count = 0

# 	# We will make a recursive call if and only if
# 	# we have more than one elements

# 	if left < right:

# 		# mid is calculated to divide the array into two subarrays
# 		# Floor division is must in case of python

# 		mid = (left + right)//2

# 		# It will calculate inversion
# 		# counts in the left subarray

# 		inv_count += _mergeSort(arr, temp_arr,
# 									left, mid)

# 		# It will calculate inversion
# 		# counts in right subarray

# 		inv_count += _mergeSort(arr, temp_arr,
# 								mid + 1, right)

# 		# It will merge two subarrays in
# 		# a sorted subarray

# 		inv_count += merge(arr, temp_arr, left, mid, right)
# 	return inv_count

# # This function will merge two subarrays
# # in a single sorted subarray
# def merge(arr, temp_arr, left, mid, right):
# 	i = left	 # Starting index of left subarray
# 	j = mid + 1 # Starting index of right subarray
# 	k = left	 # Starting index of to be sorted subarray
# 	inv_count = 0

# 	# Conditions are checked to make sure that
# 	# i and j don't exceed their
# 	# subarray limits.

# 	while i <= mid and j <= right:

# 		# There will be no inversion if arr[i] <= arr[j]

# 		if arr[i] <= arr[j]:
# 			temp_arr[k] = arr[i]
# 			k += 1
# 			i += 1
# 		else:
# 			# Inversion will occur.
# 			temp_arr[k] = arr[j]
# 			inv_count += (mid-i + 1)
# 			print(inv_count, ',,,,,,,')
# 			k += 1
# 			j += 1

# 	# Copy the remaining elements of left
# 	# subarray into temporary array
# 	while i <= mid:
# 		temp_arr[k] = arr[i]
# 		k += 1
# 		i += 1

# 	# Copy the remaining elements of right
# 	# subarray into temporary array
# 	while j <= right:
# 		temp_arr[k] = arr[j]
# 		k += 1
# 		j += 1

# 	# Copy the sorted subarray into Original array
# 	for loop_var in range(left, right + 1):
# 		arr[loop_var] = temp_arr[loop_var]
		
# 	return inv_count

# # Driver Code
# # Given array is
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# result = mergeSort(arr, n)
# print("Number of inversions are", result)

# # This code is contributed by ankush_953
