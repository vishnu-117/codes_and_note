# A = [7,3,6]
# # output: [],[3],[3,6],[3,6,7],[6],[6,7],[7]
# k = len(A)
# idx = 0
# # temp = []
# temp = ""
# def print_subset(idx, A, k, temp):
#     if idx == k:
#         print(temp)
#         return temp
#     else:
#         # import pdb; pdb.set_trace()
#         print_subset(idx+1, A, k, temp+str(A[idx]))
#         print_subset(idx+1, A, k, temp)

# print_subset(0, A, k, temp)


A = [7,3,6]
# output: [],[3],[3,6],[3,6,7],[6],[6,7],[7]
k = len(A)
idx = 0
result = []
temp = []
def print_subset(idx):
    if idx >= k:
        result.append(temp.copy())
        return
    else:
        temp.append(A[idx])
        print_subset(idx+1)

        #for non seleted variable
        temp.pop()
        print_subset(idx+1)


print_subset(0)

print(result)
