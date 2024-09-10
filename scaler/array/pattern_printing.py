# for i in range(3, 0, -1):
#     print(i)


result = []
A = 3
for i in range(A):
    a = []
    for j in range(A):
        a.append(0)
    result.append(a)

k = A-2
for i in range(A):
    count = 1
    for v in range(A-1, k, -1):
        result[i][v] = count
        count += 1
    k -= 1
    count = 0
print(result)