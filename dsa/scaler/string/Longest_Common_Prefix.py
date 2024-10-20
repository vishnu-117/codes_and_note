def longestCommonPrefix(A):
    if len(A) == 1:
        return A
        
    result = A[0]
    
    for i in range(1, len(A)):
        while A[i].find(result) != 0:
            # import pdb; pdb.set_trace()
            result = result[:-1]
    return result
            

A = [ "abcd", "abcd", "efgh" ]
print(longestCommonPrefix(A))