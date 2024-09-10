lst = ["cat", "bat", "sat", "cat", "mat", "cat", "sat"]
print([[l, lst.count(l)] for l in set(lst)])
print(dict((l, lst.count(l)) for l in lst))
