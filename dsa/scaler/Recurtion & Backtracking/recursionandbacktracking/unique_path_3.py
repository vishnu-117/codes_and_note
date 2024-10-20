
def rateinmaze(matrix):
    ans = 0
    cell = 0
    start,end = None, None

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != -1: cell = cell+1
            if matrix[i][j] == 1: start = (i,j)
            if matrix[i][j] == 2: end = (i,j)

    def solution(i,j,count):
        nonlocal ans
        if (i,j) == end:
            if count == cell: 
                ans = ans+1
            return

        if not(0 <= i < m and 0 <= j < n) or track[i][j] or matrix[i][j] == -1:
            return

        track[i][j] = 1
        solution(i+1, j, count+1)
        solution(i-1, j, count+1)
        solution(i, j+1, count+1)
        solution(i, j-1, count+1)
        track[i][j] = 0

    track = [[0 for j in range(n)] for i in range(m)]
    solution(start[0],start[1],1)
    return ans

# matrix = [[1, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 2, -1] ]

matrix = [[2,-1],
     [0,0],
     [-1,1]]
result = rateinmaze(matrix)
print(result)

class Solution:
    def uniquePathsIII(self, grid):
        # SETUP
        m, n = len(grid), len(grid[0])
        cells = 0
        start = None
        end = None
        for x in range(m):
            for y in range(n):
                if grid[x][y] != -1: cells += 1
                if grid[x][y] == 1: start = (x, y)
                if grid[x][y] == 2: end = (x, y)
                    
        # BACKTRACKING LOGIC
        def dfs(x, y, count):
            nonlocal ans
            if (x, y) == end: 
                if count == cells: ans += 1
                return
            if not (0 <= x < m and 0 <= y < n) or visited[x][y] or grid[x][y] == -1: 
                return
            
            visited[x][y] = 1
            dfs(x+1, y, count+1)
            dfs(x-1, y, count+1)
            dfs(x, y+1, count+1)
            dfs(x, y-1, count+1)
            visited[x][y] = 0

        # PREP FOR BACKTRACKING 
        visited = [[0]*n for _ in range(m)]
        ans = 0
        dfs(start[0], start[1], 1)
        return ans

obj = Solution()

# m = [[1, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 2, -1] ]

m = [[2,-1],
     [0,0],
     [-1,1]]
# print(obj.uniquePathsIII(m))
