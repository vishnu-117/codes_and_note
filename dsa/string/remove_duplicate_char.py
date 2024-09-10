from collections import OrderedDict


def removeDuplicateWithoutOrder(str):
    print("".join(set(str)))


removeDuplicateWithoutOrder("geeksforgeeks")


def removeDuplicateWithOrder(str):
    print("".join(OrderedDict.fromkeys(str)))

    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t += i
    print("using for loop", t)


removeDuplicateWithOrder("geeksforgeeks")
