def uniquePaths(A, B):
    
    if A > 1 and B> 1: 
        grid = [[0 for y in range(B)] for x in range(A)]
        
        for i in range(A):
            grid[i][0] = 1
            
        for j in range(B):
            grid[0][j] = 1
            
        for i in range(1,A):
            for k in range(1,B):
                grid[i][k] = grid[i-1][k]+grid[i][k-1]
        print(grid)
        result = grid[i-1][k-1]

    elif A==1 or B == 1:
        return 1
    else:
        return 0
    return result

A = 15
B = 9
print(uniquePaths(A,B))