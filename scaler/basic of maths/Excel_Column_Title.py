def convertToTitle(A):
    abcd = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',
            18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',0:'Z'}
    result = []
    while A != 0:
        index = A % 26
        # if index != 0:
        # import pdb ; pdb.set_trace()
        result.insert(0,abcd[index])
        
        if index == 0:
            A = A//26 - 1
        else:
            A = A//26
        
    return ''.join(result)

# a = 28
# a = 19010
# a = 28
a = 943566
print(convertToTitle(a))