T = int(input())
list1 = []
i = 2
for j in range(T):
    N = int(input())
    while i > N/i:
        if N % i == 0:
            N = N/i
            list1.append(i)
        else:
            i += 1
    print(max(list1))