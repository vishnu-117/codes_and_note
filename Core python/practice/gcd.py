import math
A = 2/3
B = 8/9
def GCD(A,B):
    if B == 0:
        return A
    else:
        return GCD(B,A%B)

lcm = A*B/GCD(A,B)
print(lcm,GCD(A,B))