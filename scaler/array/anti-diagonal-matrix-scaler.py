# Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details

# Python3 implementation to return
# an array of its anti-diagonals
# when an N*N square matrix is given

# function to print the diagonals


def diagonal(A):

    N = 3
    list1 = []
    for i in range(N*2-1):
        a = []
        for j in range(N):
            a.append(0)
        list1.append(a)
    raw = 0
    column = 0
    for col in range(N):

        startcol = col
        startrow = 0

        while(startcol >= 0 and
            startrow < N):
            list1[raw][column] = A[startrow][startcol]
            column += 1
            startcol -= 1
            startrow += 1
        raw += 1
        column = 0
    for row in range(1, N):
        startrow = row
        startcol = N - 1

        while(startrow < N and
            startcol >= 0):
            list1[raw][column] = A[startrow][startcol]
            column += 1

            startcol -= 1
            startrow += 1
        raw += 1
        column = 0
    print(list1, '<<<<<<<<<<<<<')


# Driver code
if __name__ == "__main__":

	# matrix iniliasation
	A = [[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]]

	diagonal(A)

# This code is contributed by AnkitRai01
