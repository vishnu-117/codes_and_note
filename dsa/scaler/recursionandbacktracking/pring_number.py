b = [3,5]

# def print_number(a):
#     if a[0] > a[1]:
#         return
#     print(a[0])
#     print_number([a[0]+1, a[1]])

# def print_number(a):
#     if a[0] > a[1]:
#         return
#     print(a[1])
#     print_number([a[0], a[1]-1])


def print_number(a):
    if a[0] > a[1]:
        return
    print_number([a[0]+1, a[1]])
    print(a[0])

print(print_number(b))