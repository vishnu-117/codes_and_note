# def solve(A):
#     even_max = -1000000000
#     odd_min = 1000000000
    
#     for index, value in enumerate(A):
        
#         if value % 2 == 0 and value != 0 and value > even_max:
#             even_max = value

#         if odd_min < 0 and value <0 and value % 2 != 0 and value < odd_min:
#             odd_min = value
#         elif value % 2 != 0 and value < odd_min:
#             odd_min = value
#         else:
#             pass
#     print(even_max, odd_min)
#     return even_max-odd_min

# # A = [ 72, 16, -61, 99, -74, 34, 87, 96, -29, 97 ]
# A = [-15, -45, 43, 23, -63, 69, 35, 19, 37, -52]
# print(solve(A))

A = [12,12,13]

print(13 in A)