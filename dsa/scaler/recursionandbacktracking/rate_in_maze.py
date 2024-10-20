from recviz import recviz

direction = 'DLRU'
di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]

def is_valid_move(next_i, next_j, n, maze):
    if 0 <= next_i < n and 0 <= next_j < n and maze[next_i][next_j] == 1:
        return True
    return False

# @recviz
def rate_in_maze(i, j, n,maze, result, path):
    if i == n-1 and j == n-1:
        result.append(path[:])
        return
    
    for k in range(4):
        next_i = i + di[k]
        next_j = j + dj[k]

        if is_valid_move(next_i, next_j, n, maze):
            maze[i][j] = 0
            path.append(direction[k])
            rate_in_maze(next_i, next_j, n, maze, result, path)
            maze[i][j] = 1
            path.pop()

if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    n = len(maze)
    result = []
    path = []
    i,j = 0,0
    rate_in_maze(i,j,n,maze,result,path)

    if not result:
        print("-1")
    else:
        for i in result:
            print("".join(i))

# def is_valid(maze, x, y):
#   """
#   Checks if a cell is valid.

#   Args:
#     maze: The maze.
#     x: The x-coordinate of the cell.
#     y: The y-coordinate of the cell.

#   Returns:
#     True if the cell is valid, False otherwise.
#   """

#   if x < 0 or x >= len(maze):
#     return False
#   if y < 0 or y >= len(maze[0]):
#     return False
#   if maze[x][y] == 0:
#     return False
#   return True


# def find_path(maze, x, y, path):
#   """
#   Finds a path from the current cell to the destination.

#   Args:
#     maze: The maze.
#     x: The x-coordinate of the current cell.
#     y: The y-coordinate of the current cell.
#     path: The current path.

#   Returns:
#     A list of directions to the destination, or None if there is no path.
#   """

#   if x == len(maze) - 1 and y == len(maze[0]) - 1:
#     return path

#   if not is_valid(maze, x, y):
#     return None

#   path.append('D')
#   if find_path(maze, x + 1, y, path) is not None:
#     return path
#   path.pop()

#   path.append('R')
#   if find_path(maze, x, y + 1, path) is not None:
#     return path
#   path.pop()

#   path.append('U')
#   if find_path(maze, x - 1, y, path) is not None:
#     return path
#   path.pop()

#   path.append('L')
#   if find_path(maze, x, y - 1, path) is not None:
#     return path
#   path.pop()

#   return None


# def solve_maze(maze):
#   """
#   Solves the rat in maze problem.

#   Args:
#     maze: The maze.

#   Returns:
#     A list of directions to the destination, or None if there is no path.
#   """

#   path = []
#   return find_path(maze, 0, 0, path)


# if __name__ == '__main__':
#   maze = [[1, 0, 0, 0],
#           [1, 1, 0, 1],
#           [0, 0, 0, 1],
#           [1, 1, 1, 1]]

#   path = solve_maze(maze)
#   if path is not None:
#     print('The path to the destination is:', path)
#   else:
#     print('There is no path to the destination.')
            

def rateinmaze(m, n):
  
  def solution(i,j,m,n,track, tmp):
    if i == n-1 and j == n-1:
      result.append(tmp)
      return
    
    if i + 1 < n and m[i+1][j] == 1 and not track[i+1][j]:
      track[i][j] = 1
      solution(i+1, j, m, n, track, tmp+"D")
      track[i][j] = 0
    
    if j + 1 < n and m[i][j+1] == 1 and not track[i][j+1]:
      track[i][j] = 1
      solution(i, j+1, m, n, track, tmp+"R")
      track[i][j] = 0
    
    if j - 1 >= 0 and m[i][j-1] == 1 and not track[i][j-1]:
      track[i][j] = 1
      solution(i, j-1, m, n, track, tmp+"L")
      track[i][j] = 0
    
    if i - 1 >= 0 and m[i-1][j] == 1 and not track[i-1][j]:
      track[i][j] = 1
      solution(i-1, j, m, n, track, tmp+"U")
      track[i][j] = 0
    
    
  
  result = []
  track = [[0 for j in range(n)] for i in range(n)]
  i = j = 0
  if m[0][0] == 1: 
    solution(i,j,m,n,track, "")
  return result



n = 4

m = [[1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]]

result = rateinmaze(m,n)
print(result)