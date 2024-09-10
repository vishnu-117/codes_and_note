def nsum(n):
    import pdb; pdb.set_trace()
    if n == 1:
        return 1
    else:
        return n + nsum(n-1)

print(nsum(4))