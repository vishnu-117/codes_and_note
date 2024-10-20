def getLargest(A):
    new_arr = A.split('_')
    string = new_arr[0]
    result = list(string)
    to_replace = new_arr[1]
    sorted_string = list(to_replace)
    
    count = 0

    for index, i in enumerate(result):
        # if len(sorted_string) > 0:
        for index1, k in enumerate(sorted_string):
            import pdb; pdb.set_trace()
            if ord(i) < ord(k):
                result[index] = k
                sorted_string.remove(sorted_string[index1])
                count += 1
                break
        # else:
        #     break
    
    return ''.join(result)

# A = "abb_c"
A = "abcdefgh_zzz"
print(getLargest(A))