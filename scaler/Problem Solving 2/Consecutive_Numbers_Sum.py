from math import *
def solve(A):
    count = 0
    k = 1
    sq = int(sqrt(A*2))
    print(sq, '<<<<<<<<,,')
    # import pdb; pdb.set_trace()
    # while (A-k*(k-1)/2) > 0 and (A-k*(k-1)/2) > sq:
    for i in range(1, sq):
        print(i)
        if (A-k*(k-1)/2) % k == 0:
            print((A-k*(k-1)/2) / k)
            count += 1
        k += 1
    return count

# A=5
# A=53084
# A=58048
A=73121
print(solve(A))