
"""
https://www.geeksforgeeks.org/find-number-times-string-occurs-given-string/

Given two strings, find the number of times the second string occurs in the first string, whether continuous or discontinuous.
Input:  
string a = "GeeksforGeeks"
string b = "Gks"

Output: 4

Explanation:  
The four strings are - (Check characters marked in bold)
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
GeeksforGeeks
"""
def count(str1, str2, m, n):

    if (m == 0 and n == 0) or n == 0:
        return 1
    
    if m == 0:
        return 0
    
    if (str1[m-1] == str2[n-1]):
        return count(str1, str2, m-1, n-1) + count(str1, str2, m-1, n)
    else:
        return count(str1, str2, m-1, n)

def subsequence_count(str1, str2):
    result = count(str1, str2, len(str1), len(str2))
    return result

print(subsequence_count('GeeksforGeeks', 'Gks'))