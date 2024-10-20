class Solution:
    def nthPoint(self,n):
        if n ==0:
            return 1
        if n < 0:
            return 0
        return self.nthPoint(n-1)+self.nthPoint(n-2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.nthPoint(n)
        print(ans)
# } Driver Code Ends