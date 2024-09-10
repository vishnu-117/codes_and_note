data = {}
def nthFib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        if n-1 in data.keys():
            a = data.get(n-1)
        else:
            a = nthFib(n-1)
            data[n-1] = a
        
        if n-2 in data.keys():
            b = data.get(n-2)
        else:
            b = nthFib(n-2)
            data[n-2] = b
        return a + b

print(nthFib(4))