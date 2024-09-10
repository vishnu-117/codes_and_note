a = [ 96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33, -12, -94, -80, -71, 48, -93, 62 ]



def solve(A):
    sum = 0
    new_list = []
    for i in A:
        sum += i
        print(sum)
        if sum == 0 or sum in new_list:
            import pdb; pdb.set_trace()
            sum = 0
            break
        new_list.append(sum)
            
    if sum == 0:
        return 1
    else:
        return 0


print(solve(a))