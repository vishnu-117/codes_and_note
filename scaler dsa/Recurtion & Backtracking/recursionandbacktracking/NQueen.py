
# global N
# N = 4
# result = []

# def is_valid_position(row, col, board):

#     for i in range(col):
#         if board[row][i] == 'Q':
#             return False

#     for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[i][j] == 'Q':
#             return False

#     for i,j in zip(range(row, N, 1), range(col, -1, -1)):
#         if board[i][j] == 'Q':
#             return False

#     return True

# def NQ(board, col):
#     if col == N:
#         result.append(list(board))
#         return 

#     for row in range(N):
#         if is_valid_position(row, col, board):
#             # board[row][col] = "Q"
#             board[row] = board[row][:col] + 'Q' + board[row][col+1:]
#             NQ(board, col+1)
#             board[row] = board[row][:col] + '.' + board[row][col+1:]
#             # board[row][col] = 0
#     return False

# def solveNQ():
#     # board = [ [0, 0, 0, 0],
#     #           [0, 0, 0, 0],
#     #           [0, 0, 0, 0],
#     #           [0, 0, 0, 0]
#     #          ]
#     board = ['.'*N for _ in range(N)]
#     # if NQ(board, 0) == False:
#     #     print ("Solution does not exist")
#     #     return False
    
 
#     result = NQ(board, 0)
#     print(result)
#     # return True
# solveNQ()
# print(result)

# class Solution:
#     # @param A : integer
#     # @return a list of list of strings
#     def solveNQueens(self, A):
#         def is_valid_position(board, row, col):

#             for i in range(col):
#                 if board[row][i] == 'Q':
#                     return False

#             for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
#                 if board[i][j] == 'Q':
#                     return False

#             for i,j in zip(range(row, A, 1), range(col, -1, -1)):
#                 if board[i][j] == 'Q':
#                     return False

#             return True

#         def NQ(board, col):
#             if col == len(board):
#                 ans.append(list(board))
#                 return

#             for row in range(A):
#                 if is_valid_position(board, row, col):
#                     board[row] = board[row][:col] + 'Q' + board[row][col+1:]
#                     NQ(board, col+1)
#                     board[row] = board[row][:col] + '.' + board[row][col+1:]

#         ans = []
#         if A == 1:
#             return [['Q']]
#         board = ['.'*A for _ in range(A)]
#         print(board)
#         NQ(board, 0)
#         return ans

# obj = Solution()
# result = obj.solveNQueens(8)
# print(result)


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        def is_valid_position(board, row, col):

            for i in range(col):
                if board[row][i] == 'Q':
                    return False

            for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            for i,j in zip(range(row, A, 1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True

        def NQ(board, col):
            if col == A:
                ans.append(list(board))
                return
            
            for row in range(A):

                if is_valid_position(board, row, col):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    NQ(board, col+1)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

        ans = []
        if A == 1:
            return [['Q']]
        board = ['.'*A for _ in range(A)]
        
        NQ(board, 0)
        print(ans, 'ans')
        return ans
obj = Solution()
print(obj.solveNQueens(4))
