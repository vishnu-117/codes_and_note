# Generate all Binary Strings of length N with equal count of 0s and 1s


# Input: N = 2  
# Output: “01”, “10”
# Explanation: All possible binary strings of length 2 are: 01, 10, 11, 00. Out of these, only 2 have equal number of 0s and 1s  

# Input: 4  
# Output:  “0011”, “0101”, “0110”, “1100”, “1010”, “1001”


# def generate_n_lenght_string(count, result):
#     # import pdb; pdb.set_trace()
#     if count == 0:
#         print(result)
#         return result
#     else:
#         generate_n_lenght_string(count-1, result.append('0'))
#         generate_n_lenght_string(count-1, result.append('1'))

# print(generate_n_lenght_string(3, [])) 

from traceback import print_tb


N = 3
result = []
temp = []

def generate_binary_str(N):
    if N == 0:
        result.append(temp.copy())
        return
    else:
        temp.append(0)
        generate_binary_str(N-1)
        temp.pop()
        temp.append(1)
        generate_binary_str(N-1)
        temp.pop()

generate_binary_str(N)
print(result)