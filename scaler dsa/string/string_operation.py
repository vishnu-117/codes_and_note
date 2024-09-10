def solve(A):
    result = ''
    for i in A:
        ascii_value = ord(i)
        if not ascii_value in range(65, 91):
           result += i
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        import pdb ; pdb.set_trace()
        if i in  vowel_list:
            result = result.replace(i, '#')
    return result*2

A = "ihgUeK"
print(solve(A))