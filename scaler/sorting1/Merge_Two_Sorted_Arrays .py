
def solve(self, A, B):
    i=j=k=0
    len_a = len(A)
    len_b = len(B)
    new_len = len_a + len_b
    result = [0 for i in  range(new_len)]
    while len_a > i and len_b > j:
        if A[i] > B[j]:
            result[k] = B[j]
            k += 1
            j += 1
        else:
            result[k] = A[i]
            k += 1
            i += 1
            
    while len_a > i:
        result[k] = A[i]
        k += 1
        i += 1
        
    while len_b > j:
        result[k] = B[j]
        K += 1
        j += 1
        
    return result