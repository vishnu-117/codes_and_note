# str1 = "geeksforgeeks"
# str2 = "ABeeIghiObhkUul"


# def allVowel(s):
#     a = 0
#     e = 0
#     i = 0
#     o = 0
#     u = 0
#     s = s.lower()
#     s = set(s)
#     for j in s:
#         if j == "a":
#             a += 1
#         elif j == "e":
#             e += 1
#         elif j == "i":
#             i += 1
#         elif j == "o":
#             o += 1
#         elif j == "u":
#             u += 1
#     if a > 0 and e > 0 and i > 0 and o > 0 and u > 0:
#         print("string contain all vowel")
#     else:
#         print("sorry")


# allVowel(str1)
# allVowel(str2)


# def check(string):
#     string = string.lower()
#     vowel = set("aeiou")
#     s = set({})

#     for char in string:
#         if char in vowel:
#             s.add(char)
#         else:
#             pass
#     print(s)
#     if len(s) == len(vowel):
#         print("Accepted")
#     else:
#         print("Not accepted")


# str1 = "geeksforgeeks"
# str2 = "ABeeIghiiobhkUul"
# check(str1)
# check(str2)


def check1(string):
    if len(set(string).intersection("AEIOUaeiou")) >= 5:
        print("Accepted")
    else:
        print("Not accepted")


str1 = "geeksforgeeks"
str2 = "ABeeIghiiobhkUul"
check1(str1)
check1(str2)
