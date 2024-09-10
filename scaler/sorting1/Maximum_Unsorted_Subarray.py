
def subUnsort(A):
    i = 0
    j = len(A)-1
    
    for k in range(len(A)-1):
        if A[k] + 1 != A[k+1]:
            i += 1
            break
        
    for k in range(len(A)-1, -1):
        if A[k] - 1 != A[k-1]:
            j -= 1
            break
    
    if i ==0 and j == len(A)-1:
        return [-1]

    return [i, j]
            
	        
A = [ 1, 3, 2, 4, 5 ]      
print(subUnsort(A))
