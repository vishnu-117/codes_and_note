def sum_pairs(ints, s):
    for i in range(len(ints)-1):
        for i+1 in range(len(ints)):
            if ints[i] + ints[i+1] == s:
                return [ints[i],ints[i+1]]
                break
print([2,8,9,4,1],3)