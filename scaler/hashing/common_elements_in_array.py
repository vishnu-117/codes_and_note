def solve(A, B):
    set_of_a = set(A)
    dict1 = {}
    dict2 = {}
    result = []
    for i in A:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    for j in B:
        if j in dict2.keys():
            dict2[j] += 1
        else:
            dict2[j] = 1

    for value, count in dict1.items():
        number_of_value_count = dict2.get(value, False)
        # import pdb; pdb.set_trace()
        if number_of_value_count:
            if count < number_of_value_count:
                for i in range(count):
                    result.append(value)
            else:
                for i in range(number_of_value_count):
                    result.append(value)

    return result

A = [ 1, 2, 2, 1 ]
B = [ 2, 3, 1, 2 ]

print(solve(A,B))