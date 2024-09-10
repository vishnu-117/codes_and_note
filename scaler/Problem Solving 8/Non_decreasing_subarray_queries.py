
def solve(A, B):
    new_list = []
    count = 0
    if len(A) > 1:
        if A[0] == A[1] or A[0] < A[1]:
            count += 1
            new_list.append(count)
        else:
            new_list.append(0)
    result = []
    for i in range(1,len(A)):
        # import pdb; pdb.set_trace()
        if A[i] >= A[i-1]:
            # import pdb; pdb.set_trace()
            new_list.append(count)
        else:
            count += 1
            print(i)
            # import pdb; pdb.set_trace()
            new_list.append(count)
            
    for k in B:
        # import pdb; pdb.set_trace()
        if new_list[k[0]-1] == new_list[k[1]-1]:
            result.append(1)
        else:
            result.append(0)
            
    return result
            
A = [1, 7, 3, 4, 9]
B = [ 
      [1, 2], 
      [2, 4]
    ]

A = [ 20, 7, 12, 3, 13, 2, 13, 18, 4, 1, 7, 13, 11, 17, 20, 8, 6, 14, 3, 2 ]
B = [
  [1, 3]
]

A = [ 7, 7, 1, 6, 9 ]
B =[
  [1, 3],
  [4, 5],
  [1, 2],
  [3, 4],
  [1, 5],
]

A = [ 7, 7, 1, 6, 9 ]
B = [
  [1, 3],
  [4, 5],
  [1, 2],
  [3, 4],
  [1, 5],
]
print(solve(A,B))