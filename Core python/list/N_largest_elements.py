def nLargetNumber(list1, number):
    new_list = set(list1)
    new_list1 = list(new_list)
    new_list1.sort()
    print(new_list1)
    result = new_list1[-number:]
    print(result)


list1 = [4, 5, 1, 2, 9]
list2 = [81, 52, 45, 10, 3, 2, 96]
nLargetNumber(list1, 2)
nLargetNumber(list2, 3)
