str1 = 'BANANA'
vowel = ['A', 'E', 'I', 'O', 'U']
consonent_str_list = []
vowel_str_list = []

# for idx in range(0, len(str1)):
#     for k in range(idx, len(str1)):
#         if str1[idx] in vowel:
#             vowel_str_list.append(str1[idx:k+1])
#         else:
#             consonent_str_list.append(str1[idx:k+1])

# print(consonent_str_list)
# print(vowel_str_list)

# print(len(consonent_str_list)+len(vowel_str_list))

A = [7,3,6]
# output: [],[3],[3,6],[3,6,7],[6],[6,7],[7]
k = len(str1)
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
