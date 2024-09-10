    def solve(self, A):
        n = len(A)
        if n == 1:
            return A[0]
            
        if A[0] != A[1]:
            return A[0]
            
        if A[n-1] != A[n-2]:
            return A[n-1]
            
        low = 0 
        high = n-1
        
        while(low <= high):
            mid = (low + high)//2
            
            if A[mid] != A[mid-1] or A[mid] != A[mid+1]:
                return A[mid]
                
            if A[mid] == A[mid-1]:
                mid = mid-1
                
            if mid % 2 == 0:
                low = mid + 2
                
            if mid % 2 == 1:
                high = mid-1
        return A[mid]
