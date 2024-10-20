result = []
A = 5
for i in range(A):
    a = []
    for j in range(A):
        a.append(0)
    result.append(a)

for i in range(A):
    for j in range(i+1):
        if j == 0:
            result[i][j] = 1
        else:
            # import pdb ; pdb.set_trace()
            result[i][j] = result[i-1][j-1] + result[i-1][j]

print(result)