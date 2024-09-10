import math

def is_perfect_squre(num):
    return True if (math.sqrt(num) - int(math.sqrt(num)) == 0) else False

def is_squarefull(arr):
    for i in range(0, len(arr)-1):
        if not is_perfect_squre(arr[i]+arr[i+1]):
            return False
    return True

def squarefull_arr(arr, index):
    """
    Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

    Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

    Input: [1,17,8]
    Output: 2
    Explanation: 
    [1,8,17] and [17,8,1] are the valid permutations.
    """
    if index == len(arr):
        if is_squarefull(arr):
            result.add(tuple(arr.copy()))
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        squarefull_arr(arr, index+1)
        arr[index], arr[i] = arr[i], arr[index]

result = set()
index = 0
squarefull_arr([1,17,8], index)
print(result)

##########################################
# improved
##########################################
import math

def is_perfect_squre(num):
    if (math.sqrt(num) - int(math.sqrt(num)) == 0):
        # print(num)
        return True
    else:
        False
    # return True 

def is_squarefull(arr):
    for i in range(0, len(arr)-1):
        if not is_perfect_squre(arr[i]+arr[i+1]):
            return False
    return True

def squarefull_arr(arr, index):
    """
    Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

    Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

    Input: [1,17,8]
    Output: 2
    Explanation: 
    [1,8,17] and [17,8,1] are the valid permutations.
    """
    if index == len(arr):
        # if is_squarefull(arr):
        result.add(tuple(arr.copy()))
        return

    for i in range(index, len(arr)):

        #skipping duplicates
        if i > index and arr[i] == arr[index]:
            continue

        arr[index], arr[i] = arr[i], arr[index]
        if index == 0 or (index > 0 and is_perfect_squre(arr[index]+arr[index-1])):
            squarefull_arr(arr, index+1)
        arr[index], arr[i] = arr[i], arr[index]

result = set()
index = 0
A = [2,2,2]
A.sort() #sort array to skip duplicate numbers
squarefull_arr(A, index)
print(result)



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        def is_perfect_squre(num):
            if (math.sqrt(num) - int(math.sqrt(num)) == 0):
                return True
            else:
                return False

        result = set()
        A.sort()
        def permutate(arr, index):   
            if index == len(arr):
                result.add(tuple(arr.copy()))
                return

            for i in range(index, len(arr)):

                #skipping duplicates
                if i > index and arr[i] == arr[index]:
                    continue

                arr[index], arr[i] = arr[i], arr[index]
                if index == 0 or (index > 0 and is_perfect_squre(arr[index]+arr[index-1])):
                    permutate(arr, index+1)
                arr[index], arr[i] = arr[i], arr[index]
        
        permutate(A, 0)
        return len(result)

obj = Solution()

print(obj.solve([10]))