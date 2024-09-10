# def count(str1, str2):
#     result = []
#     str1 = set(str1)
#     str2 = set(str2)
#     for i in str1:
#         for j in str2:
#             if i == j:
#                 result.append(i)
#     print(len(result))
#     for k in result:
#         print(k, end="")


# count("abcdef", "defghia")
# count("aabcddekll12@", "bb22ll@55k")

import re


def count1(str1, str2):
    count = 0
    str1 = {str1}
    str2 = {str2}
    for i in str1:
        if re.search(i, str2):
            count += 1
            print(i, end="")
    print("Number of macted character is", count)


count1("abcdef", "defghia")
count1("aabcddekll12@", "bb22ll@55k")

