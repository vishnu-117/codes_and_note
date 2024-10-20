# def partition(start, end, array):
# 	pivot_index = start
# 	pivot = array[pivot_index][0]**2 +  array[pivot_index][1]**2
# 	while start < end:
# 		while start < len(array) and array[start][0]**2 + array[start][1]**2 <= pivot:
# 			start += 1
# 		while array[end][0]**2 + array[end][1]**2 > pivot:
# 			end -= 1
# 		if(start < end):
# 			# import pdb;pdb.set_trace()
# 			array[start], array[end] = array[end], array[start]
# 	array[end], array[pivot_index] = array[pivot_index], array[end]
# 	return end

# def quick_sort(start, end, array):
	
# 	# import pdb; pdb.set_trace()
# 	if (start < end):
# 		p = partition(start, end, array)
# 		quick_sort(start, p - 1, array)
# 		quick_sort(p + 1, end, array)
# 		return array
		
# # Driver code
# array = [ 10, 7, 8, 9, 1, 5 ]
array  = [
  [26, 41],
  [40, 47],
  [47, 7],
  [50, 34],
  [18, 28],
]


# 26 41 40 47 47 7 50 34 18 28

# # import pdb; pdb.set_trace()
# B = 5


# array = [
#   [28, 2],
#   [41, 47],
#   [95, 83],
#   [106, 108],
#   [63, 104],
#   [100, 62],
#   [108, 87],
#   [109, 63],
#   [70, 94],
#   [69, 87],
#   [106, 101],
#   [70, 67],
#   [77, 79],
#   [99, 72],
#   [71, 77],
#   [98, 79],
# ]
# print(quick_sort(0, len(array) - 1, array))

# print(f'Sorted array: {array}')
	






A = [
  [28, 2],
  [41, 47],
  [95, 83],
  [106, 108],
  [63, 104],
  [100, 62],
  [108, 87],
  [109, 63],
  [70, 94],
  [69, 87],
  [106, 101],
  [70, 67],
  [77, 79],
  [99, 72],
  [71, 77],
  [98, 79],
]


def sort(ele):
    	return ele[0]**2+ele[1]**2

sorted_list = sorted(A, key=sort)
print(sorted_list)
# def solve(A, B):
# 	def partition(start, end, A):
# 		pivot_index = start
# 		pivot = A[pivot_index][0]**2 +  A[pivot_index][1]**2
# 		while start < end:
# 			while start < len(A) and A[start][0]**2 + A[start][1]**2 <= pivot:
# 				start += 1
# 			while A[end][0]**2 + A[end][1]**2 > pivot:
# 				end -= 1
# 			if(start < end):
# 				# import pdb;pdb.set_trace()
# 				A[start], A[end] = A[end], A[start]
# 		A[end], A[pivot_index] = A[pivot_index], A[end]
# 		return end

# 	def quick_sort(start, end, A):
# 		# import pdb; pdb.set_trace()
# 		if (start < end):
# 			p = partition(start, end, A)
# 			quick_sort(start, p - 1, A)
# 			quick_sort(p + 1, end, A)
# 			return A
# 	print(A, ',,,,,,,')
# 	return quick_sort(0, len(A) - 1, A)


# print(solve(A, 2))