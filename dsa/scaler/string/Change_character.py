
def solve(A, B):
    store_data = {}
    
    if len(A) == 2 and A[0] == A[1]:
        return 0
    elif len(A) == 2 and A[0] != A[1]:
        return 2
    else:
        pass

    for i in A:
        if i in store_data.keys():
            store_data[i] += 1
        else:
            store_data[i] = 1
    
    count = 0
    values = 0
    # k = dict(sorted(s.items(),key=lambda x:x[0],reverse = True))
    # store_data = dict(sorted(store_data.items(),key=lambda x:x[1], reverse = True))
    from collections import OrderedDict
    # store_data = OrderedDict(sorted(store_data.items(),key=lambda x:x[1], reverse = True))
    store_data = OrderedDict(sorted(store_data.items(),key=lambda x:x[1]))

    print(len(store_data), "B", B)
    print(store_data)
    for key, value in store_data.items():
        # import pdb; pdb.set_trace()
        if values == B:
            if count == 0:
                count += 1
            return len(store_data)-count
        elif values+value <= B:
            print(key, value, '<<<<<<<<<<')
            values += value
            count += 1
        else:
            pass

    # import pdb; pdb.set_trace()
    # if count == B:
    return len(store_data)-count

    # convert_to_set = set(A)
    # length = len(convert_to_set)
    # return length-B
    
    # if count == 0:
    #     return len(A)
            
# A = "abcabbccd"
# B = 3

# A = "wfnfozvsrt"
# B = 4

# A = "ircvscxggbwkfnqd"
# B = 2

A = "qghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxfxtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknlyjyhfixjswnkkufnuxxzrzbmnmgqooketlyhnkoaugzqrcddiuteiojwayyzpvscmpsajlfvgubfaaovlzylntrkdcpwsrtesjwhdizcobzcnfwlqijtvdwvxhrcbldvgylwgbusbmborxtlhcsmpxohgmgnkeufdxotogbgxpeyanfetcukepzshkljugggekjdqzjenpevqgxiepjsrdzjazujllchhbfqmkimwzobiwybxduunfsksrsrtekmq"
B = 119

# A = "ircvscxggbwkfnqd"
# B = 2
print(solve(A,B))      
