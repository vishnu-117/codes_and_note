def sumOfDictValue(mydict):
    sum = 0
    # for i in mydict:
    #     sum += mydict[i]
    for i in mydict.values():
        sum += i
    print(sum)


a = {"a": 100, "b": 200, "c": 300}
sumOfDictValue(a)
