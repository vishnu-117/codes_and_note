# def largestNumber(A):
#     A = list(A)
#     result = str(A[0])
#     for i in range(1, len(A)-1):
#         result = str(A[0])
#         if len(A) > 2:
#             for i in range(1, len(A)):
#                 # import pdb; pdb.set_trace()
#                 if int(result+str(A[i])) > int(str(A[i])+result):
#                     result = result+str(A[i])
#                 else:
#                     # import pdb; pdb.set_trace()
#                     result = str(A[i])+result
#         elif len(A)==1:
#             return str(A[0])
#         else:
#             if int(result+str(A[1])) > int(str(A[1])+result):
#                 result = result+str(A[1])
#             else:
#                 result = str(A[1])+result
#     return result

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


def largestNumber(A):
    A = list(A)
    largest_num = ''.join(sorted(map(str, A), key=LargerNumKey))
    return '0' if largest_num[0] == '0' else largest_num

    return result
    
# print(largestNumber([3,30,34,5,9]))


# A = [8, 89]
A=[ 3, 30, 34, 5, 9 ]
print(largestNumber(A))
